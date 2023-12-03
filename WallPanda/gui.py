import customtkinter as ctk
from PIL import Image, ImageTk
import config
import scraper

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

class App(ctk.CTk):
    def search(self,search_string:str)->None:
        web_scraper = scraper.Scraper()
        web_scraper.scrape(search_string)

    def __init__(self):
        super().__init__()

        #other
        self.num_images = 16 
        
        #ctkinter
        self.wm_title(config.APPLICATION_NAME)
        self.wm_geometry(config.APPLICATION_GEOMETRY)
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

        self.image_and_button_frame=ctk.CTkFrame(self.main_frame,width=1200,height=510)
        self.image_and_button_frame.pack(pady=0)

        self.search_results_frame = ctk.CTkFrame(self.image_and_button_frame,fg_color='transparent',width=1200)
        self.search_results_frame.pack(fill='x',expand=True)

        self.search_results = ctk.CTkLabel(self.search_results_frame,font=('',20),text="Search results for \'Overflow\'")
        self.search_results.pack(side='left',padx=30,pady=(20,10))

        self.image_frame=ctk.CTkFrame(self.image_and_button_frame,fg_color='transparent')
        self.image_frame.pack(expand=True, fill="both",pady=0)

        self.navigation_frame=ctk.CTkFrame(self.main_frame,fg_color='transparent',width=1200)
        self.navigation_frame.pack()

        self.button1=ctk.CTkButton(self.image_frame,text='image1',height=150,width=244,fg_color='#424242')
        self.button1.grid(column=0,row=0,pady=0,padx=10)
        self.button2=ctk.CTkButton(self.image_frame,text='image2',height=150,width=244,fg_color='#424242')
        self.button2.grid(column=0,row=1,pady=0,padx=10)
        self.button3=ctk.CTkButton(self.image_frame,text='image3',height=150,width=244,fg_color='#424242')
        self.button3.grid(column=0,row=2,pady=0,padx=10)
        self.button4=ctk.CTkButton(self.image_frame,text='image4',height=150,width=244,fg_color='#424242')
        self.button4.grid(column=0,row=3,pady=0,padx=10)
        self.button5=ctk.CTkButton(self.image_frame,text='image5',height=150,width=244,fg_color='#424242')
        self.button5.grid(column=1,row=0,pady=10,padx=10)
        self.button6=ctk.CTkButton(self.image_frame,text='image6',height=150,width=244,fg_color='#424242')
        self.button6.grid(column=1,row=1,pady=10,padx=10)
        self.button7=ctk.CTkButton(self.image_frame,text='image7',height=150,width=244,fg_color='#424242')
        self.button7.grid(column=1,row=2,pady=10,padx=10)
        self.button8=ctk.CTkButton(self.image_frame,text='image8',height=150,width=244,fg_color='#424242')
        self.button8.grid(column=1,row=3,pady=10,padx=10)
        self.button9=ctk.CTkButton(self.image_frame,text='image9',height=150,width=244,fg_color='#424242')
        self.button9.grid(column=2,row=0,pady=10,padx=10)
        self.button10=ctk.CTkButton(self.image_frame,text='image10',height=150,width=244,fg_color='#424242')
        self.button10.grid(column=2,row=1,pady=10,padx=10)
        self.button11=ctk.CTkButton(self.image_frame,text='image11',height=150,width=244,fg_color='#424242')
        self.button11.grid(column=2,row=2,pady=10,padx=10)
        self.button12=ctk.CTkButton(self.image_frame,text='image12',height=150,width=244,fg_color='#424242')
        self.button12.grid(column=2,row=3,pady=10,padx=10)
        self.button13=ctk.CTkButton(self.image_frame,text='image13',height=150,width=244,fg_color='#424242')
        self.button13.grid(column=3,row=0,pady=10,padx=10)
        self.button14=ctk.CTkButton(self.image_frame,text='image14',height=150,width=244,fg_color='#424242')
        self.button14.grid(column=3,row=1,pady=10,padx=10)
        self.button15=ctk.CTkButton(self.image_frame,text='image15',height=150,width=244,fg_color='#424242')
        self.button15.grid(column=3,row=2,pady=10,padx=10)
        self.button16=ctk.CTkButton(self.image_frame,text='image16',height=150,width=244,fg_color='#424242')
        self.button16.grid(column=3,row=3,pady=10,padx=10)

        for i in range(4):
            self.image_frame.grid_columnconfigure(i, weight=1, minsize=200)

        self.previous_button = ctk.CTkButton(self.navigation_frame,text="previous",height=40,width=50,fg_color='#424242')
        self.previous_button.grid(row=0,column=0, padx=30, pady=10)

        self.page_label = ctk.CTkLabel(self.navigation_frame,text="1")
        self.page_label.grid(row=0,column=1, padx=10, pady=10)

        self.next_button = ctk.CTkButton(self.navigation_frame,text="next",height=40,width=50,fg_color='#424242')
        self.next_button.grid(row=0,column=2, padx=30, pady=10)