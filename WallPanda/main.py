import tkinter as tk
from bs4 import BeautifulSoup
import requests as re

APPLICATION_NAME = 'wallpanda'

#root = tk.Tk()
#root.title('WallPanda')
#root.state('zoomed')
#
#head_frame = tk.Frame()
#head_frame.pack()
#
#body_frame = tk.Frame()
#body_frame.pack()
#
#search_bar = tk.Entry(head_frame)
#search_bar.pack()

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'
}

def search(search_string:str):
    search_string = search_string.replace(' ','-')
    scrape_wallpaperaccess(search_string) 

def scrape_wallpaperaccess(search_string:str):
    site = 'https://wallpaperaccess.com/{search_string}'
    bs_response = generate_bs_response(site,search_string)
    img_tags = bs_response.find_all('img',{'data-slug':search_string})
    for img_tag in img_tags:
        img_src = img_tag.attrs['data-src']
        img_url = 'https://wallpaperaccess.com' + img_src 
        img = re.get(img_url)
        img_file_name = APPLICATION_NAME + img_src.replace('/','-')
        with open(img_file_name,'wb') as f:
            f.write(img.content)                 

def generate_bs_response(site:str,search_string:str):
    site = site.format(search_string = search_string)
    response = re.get(site,headers=headers)
    bs_response = BeautifulSoup(response.text,'html.parser')
    return bs_response

def download(search_string:str):
    pass

search('naruto and sasuke')

#root.mainloop()