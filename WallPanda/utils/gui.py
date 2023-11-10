import customtkinter as ctk

class App(ctk.CTk):
    def __init__(self,application_name:str,application_geometry:str):
        super().__init__()

        self.wm_title(application_name)
        self.wm_geometry(application_geometry)
        self.after(200,lambda:self.wm_state('zoomed'))

        self._set_appearance_mode('system')

        self.search_frame = ctk.CTkFrame(self)
        self.search_frame.pack(pady=20)
        self.image_container_frame = ctk.CTkFrame(self)
        self.image_container_frame.pack()

        self.search_bar = ctk.CTkEntry(self.search_frame,font=('',15),placeholder_text='search',width=400,height=40)
        self.search_bar.grid(row=0,column=0,padx=10)
        self.search_button = ctk.CTkButton(self.search_frame,height=40,width=50)
        self.search_button.grid(row=0,column=1)