import customtkinter as ctk
from PIL import Image, ImageTk
import config
import scraper
import button_generator

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

class App(ctk.CTk):
    
    def __init__(self):
        super().__init__()

        #config
        self.iconbitmap('assets/logo.ico')
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

        self.search_bar = ctk.CTkEntry(self.search_frame,font=('',15),placeholder_text='What\'s on your mind?',width=400,height=40)
        self.search_bar.grid(row=0,column=0,padx=10)
        self.search_button = ctk.CTkButton(self.search_frame,text="search",height=40,width=50,command=lambda: self.search(self.search_bar.get()),fg_color="#424242")
        self.search_button.grid(row=0,column=1)

        self.image_and_button_frame=ctk.CTkFrame(self.main_frame,height=510)
        self.image_and_button_frame.pack(pady=0)

        self.search_results_frame = ctk.CTkFrame(self.image_and_button_frame,fg_color='transparent',width=1200)
        self.search_results_frame.pack(fill='x',expand=True)

        self.search_results = ctk.CTkLabel(self.search_results_frame,font=('',20),text="Search your favourite anime character!")
        self.search_results.pack(side='left',padx=30,pady=(20,10))

        self.image_frame=ctk.CTkFrame(self.image_and_button_frame,fg_color='transparent')
        self.image_frame.pack(expand=True, fill="both",pady=0)

        self.buttons = []
        self.curr_img_row = self.curr_img_column = 0

        self.navigation_frame=ctk.CTkFrame(self.main_frame,fg_color='transparent',width=1200)
        self.navigation_frame.pack()

        self.previous_button = ctk.CTkButton(self.navigation_frame,text="previous",height=40,width=50,fg_color='#424242')
        self.previous_button.grid(row=0,column=0, padx=30, pady=10)

        self.page_label = ctk.CTkLabel(self.navigation_frame,text="1")
        self.page_label.grid(row=0,column=1, padx=10, pady=10)

        self.next_button = ctk.CTkButton(self.navigation_frame,text="next",height=40,width=50,fg_color='#424242')
        self.next_button.grid(row=0,column=2, padx=30, pady=10)

    def search(self,search_string:str)->None:
        web_scraper = scraper.Scraper()
        web_scraper.scrape(search_string)
    
    def create_button(self,path:str)->None:
        image = ctk.CTkImage(Image.open(path),size=(230,135))
        self.buttons.append(ctk.CTkButton(self.image_frame,height=150,width=244,text='',fg_color='#424242', image = image))
        if self.curr_img_column< config.IMG_ROWS: 
            self.buttons[-1].grid(column=self.curr_img_column,row=self.curr_img_row,pady=10,padx=10)
            self.curr_img_column+=1
        else:
            self.curr_img_row+= 1
            self.curr_img_column= 0

        for i in range(self.curr_img_column):
            self.image_frame.grid_columnconfigure(i, weight=1, minsize=200)