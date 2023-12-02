import customtkinter as ctk
import config
import scraper 

class App(ctk.CTk):
    def search(self,search_string:str)->None:
        web_scraper = scraper.Scraper()
        web_scraper.scrape(search_string)

    def __init__(self):
        super().__init__()

        #other
        self.num_images = 5 
        
        #ctkinter
        self.wm_title(config.APPLICATION_NAME)
        self.wm_geometry(config.APPLICATION_GEOMETRY)
        self.after(200,lambda:self.wm_state('zoomed'))

        self._set_appearance_mode('system')

        self.search_frame = ctk.CTkFrame(self,fg_color='transparent')
        self.search_frame.pack(pady=20)
        self.image_container_frame = ctk.CTkFrame(self)
        self.image_container_frame.pack()

        self.search_bar = ctk.CTkEntry(self.search_frame,font=('',15),placeholder_text='Find your vibe.',width=400,height=40)
        self.search_bar.grid(row=0,column=0,padx=10)
        self.search_button = ctk.CTkButton(self.search_frame,text="search",height=40,width=50,command=lambda: self.search(self.search_bar.get()))
        self.search_button.grid(row=0,column=1)