import tkinter as tk

class App(tk.Tk):
    def __init__(self,application_name):
        super().__init__()

        self.root = tk.Tk()
        self.root.title(application_name)
        self.root.geometry('800x600')
        self.root.state('zoomed')

        self.search_frame = tk.Frame(self.root)
        self.search_frame.pack()
        self.image_container_frame = tk.Frame(self.root)
        self.image_container_frame.pack()

        self.search_bar = tk.Entry(self.search_frame)
        self.search_bar.pack()