import time
import file_manager
from bs4 import BeautifulSoup
import threading
import requests as re
import config

class Scraper:

    def __init__(self):
        self.__headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS Xjj 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'
        }
        self.can_create = True 
        self.threads = []
        self.button_generator_sleep_time = 0.2
        self.stop_threads = False # stop threads when we have loaded a page 

    def __scrape_wallpaperaccess(self,search_string:str):

        search_string = search_string.replace(' ','-')

        site = 'https://wallpaperaccess.com/{search_string}'
        bs_response = self.__generate_bs_response(site,search_string)
        img_tags = bs_response.find_all('img',{'data-slug':search_string})
        for img_tag in img_tags:
            if self.stop_threads:
                while self.stop_threads:
                    print('stopped')
                    time.sleep(0.2)
            img_src = img_tag.attrs['data-src']
            img_url = 'https://wallpaperaccess.com' + img_src 
            img = re.get(img_url)
            img_file_name = config.APPLICATION_NAME + img_src.replace('/','-')
            file_manager.write_temp(img_file_name,img.content)

    def __generate_bs_response(self,site:str,search_string:str)->BeautifulSoup:
        site = site.format(search_string = search_string)
        response = re.get(site,headers=self.__headers)
        print(f'Response ok?: {response.ok}')
        bs_response = BeautifulSoup(response.text,'html.parser')
        return bs_response

    def scrape(self,search_string)->None:
        if search_string == '':
            return
        search_string = search_string.strip()
        self.threads = [
            threading.Thread(target=self.__scrape_wallpaperaccess,args=(search_string,)),
            threading.Thread(target=self.__scrape_wallpaperaccess,args=(search_string,))
        ]
        for thread in self.threads:
            thread.daemon = True # kill all threads when the main program ends
            thread.start()

    def create_buttons(self,gui_instance)->None:
        while True:
            if len(file_manager.image_stack) != 0 and self.can_create:
                path = file_manager.image_stack[-1].replace('\\\\','/')
                gui_instance.create_button(path)
            time.sleep(self.button_generator_sleep_time)
