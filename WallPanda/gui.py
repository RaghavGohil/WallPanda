import threading
import time
from pathlib import Path
import shutil
import ctypes
import customtkinter as ctk
import file_manager
from PIL import Image
import config
import scraper

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

class App(ctk.CTk):
    
    def __init__(self):
        super().__init__()

        #exit
        self.protocol("WM_DELETE_WINDOW",lambda: self.on_exit())

        #other
        self.create_lock = threading.Lock()
        self.search_lock = threading.Lock()

        #scraper
        self.web_scraper = scraper.Scraper()

        #config
        self.wm_iconbitmap('assets/logo.ico')
        self.wm_title(config.APPLICATION_NAME)
        self.wm_minsize(config.APPLICATION_GEOMETRY_MINSIZE[0],config.APPLICATION_GEOMETRY_MINSIZE[1])
        self.after(200,lambda:self.wm_state('zoomed'))

        self._set_appearance_mode('system')

        self.main_frame = ctk.CTkScrollableFrame(self,fg_color='transparent')
        self.main_frame.pack(fill="both",expand=True)

        self.header_frame = ctk.CTkFrame(self.main_frame,fg_color='transparent')
        self.header_frame.pack(pady=(20,10))

        self.header_image = ctk.CTkImage(Image.open('assets/logo.png'), size=(598, 200))
        self.header_image_label = ctk.CTkLabel(self.header_frame,image=self.header_image,text='')
        self.header_image_label.pack()

        self.search_frame = ctk.CTkFrame(self.main_frame,fg_color='transparent')
        self.search_frame.pack(pady=(0,20))

        self.last_search = ''
        self.search_bar = ctk.CTkEntry(self.search_frame,font=('',15),placeholder_text='What\'s on your mind?',width=400,height=40)
        self.search_bar.grid(row=0,column=0,padx=10)
        self.search_button = ctk.CTkButton(self.search_frame,text="search",height=40,width=50,command=lambda: self.search(),fg_color="#424242")
        self.search_button.grid(row=0,column=1)

        self.image_and_button_frame=ctk.CTkFrame(self.main_frame,height=510)
        self.image_and_button_frame.pack(pady=0)

        self.search_results_frame = ctk.CTkFrame(self.image_and_button_frame,fg_color='transparent',width=1200)
        self.search_results_frame.pack(fill='x',expand=True)

        self.search_results_label = ctk.CTkLabel(self.search_results_frame,font=('',20),text='Search for your favorite movie/anime!')
        self.search_results_label.pack(padx=30,pady=(20,10))

        self.image_frame=ctk.CTkFrame(self.image_and_button_frame,fg_color='transparent')
        self.image_frame.pack(expand=True, fill="both",pady=0)

        self.buttons = []
        self.curr_img_row = self.curr_img_column = 0
        self.button_generator_thread = threading.Thread(target=self.web_scraper.create_buttons,args=(self,))
        self.web_scraper.threads.append(self.button_generator_thread)

        self.navigation_frame=ctk.CTkFrame(self.main_frame,fg_color='transparent',width=1200)
        self.navigation_frame.pack()

        #self.previous_button = ctk.CTkButton(self.navigation_frame,text="previous",height=40,width=50,fg_color='#424242',command=lambda:self.prev_page())
        #self.previous_button.grid(row=0,column=0, padx=30, pady=10)

        #self.curr_page = 1
        #self.page_label = ctk.CTkLabel(self.navigation_frame,text=self.curr_page)
        #self.page_label.grid(row=0,column=1, padx=10, pady=10)

        #self.next_button = ctk.CTkButton(self.navigation_frame,text="next",height=40,width=50,fg_color='#424242',command=lambda:self.next_page())
        #self.next_button.grid(row=0,column=2, padx=30, pady=10)

    def search(self)->None:
        
        search_string = self.search_bar.get().lower()
        if search_string.strip() == '' or self.last_search == search_string:
            return
        self.curr_img_column = self.curr_img_row = 0
        for button in self.buttons:
            button.destroy()
        self.buttons.clear()

        self.web_scraper.pause_threads = True

        threads_are_alive = True

        while threads_are_alive:
            if len(self.web_scraper.threads) == 0:
                threads_are_alive = False
            else:
                for thread in self.web_scraper.threads:
                    if thread.is_alive():
                        threads_are_alive = True
                        self.web_scraper.stop_threads = True
                        break 
                    else:
                        threads_are_alive = False
        
        self.web_scraper.stop_threads = False
        self.web_scraper.pause_threads = False
        file_manager.image_stack.clear()
        self.web_scraper.scrape(search_string)

        if not self.button_generator_thread.is_alive():
            self.button_generator_thread.daemon = True
            self.button_generator_thread.start()
        
        self.search_results_label.configure(text=f'Search results for \'{search_string}\'')
        self.last_search = search_string

    def create_button(self,path:str)->None:
        self.create_lock.acquire()
        if self.curr_img_column != config.IMG_COLUMNS: 
            image = ctk.CTkImage(Image.open(path),size=(230,135))
            self.buttons.append(ctk.CTkButton(self.image_frame,height=150,width=244,text='',fg_color='#424242', image = image,command=lambda:self.download_and_set_window(path)))
            print(path)
            self.buttons[-1].grid(column=self.curr_img_column,row=self.curr_img_row,pady=10,padx=10)
            file_manager.image_stack.pop()
            self.curr_img_column += 1
            print(self.curr_img_column)
        else:
            self.curr_img_row += 1
            self.curr_img_column= 0

        for i in range(self.curr_img_column):
            self.image_frame.grid_columnconfigure(i, weight=1, minsize=200)
        
        #if len(self.buttons) == config.IMG_PER_PAGE:
        #    self.web_scraper.pause_threads = True

        self.create_lock.release()
    
    def next_page(self)->None:
        self.curr_page += 1
        self.page_label.configure(text=f'{self.curr_page}')

    def prev_page(self)->None:
        pass

    def on_exit(self)->None:
        threads_are_alive = True
        while threads_are_alive:
            if len(self.web_scraper.threads) == 0:
                threads_are_alive = False
            else:
                for thread in self.web_scraper.threads:
                    if thread.is_alive():
                        threads_are_alive = True
                        self.web_scraper.stop_threads = True
                        break 
                    else:
                        threads_are_alive = False
        file_manager.clean_temp()
        self.destroy()

    def download_and_set_window(self,path:str)->None:
        self.download_window=ctk.CTkToplevel(self)
        self.download_window.geometry(config.APPLICATION_DNS_GEOMETRY_SIZE)
        self.download_window.attributes('-topmost', 'true')
        self.download_window.resizable(False,False)
        self.download_window.wm_iconbitmap('assets/logo.ico')
        self.download_window.title("Download/Set Image")
        download_image = ctk.CTkImage(Image.open(path),size=(600,350))
        self.photo_label = ctk.CTkLabel(self.download_window,image=download_image,text='')
        self.photo_label.pack()

        self.download_button = ctk.CTkButton(self.download_window,text="Download",height=40,width=200,fg_color='#424242',command=lambda:self.download_wallpaper(path))
        self.download_button.pack(padx=10, pady=10)

        self.set_button = ctk.CTkButton(self.download_window,text="Set as desktop",height=40,width=200,fg_color='#424242',command=lambda:self.set_wallpaper(path))
        self.set_button.pack(padx=10, pady=(0,10))

    def set_wallpaper(self,path:str)->None:
        ctypes.windll.user32.SystemParametersInfoW(20, 0, path , 0)
    
    def download_wallpaper(self,path:str)->None:
        self.destination = str(Path.home() / "Downloads")
        self.source=path
        shutil.copy(self.source, self.destination)