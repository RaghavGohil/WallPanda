from . import file_manager
from bs4 import BeautifulSoup
import requests as re

class Scraper:

    def __init__(self):
        self.__headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'
        }

    def scrape_wallpaperaccess(self,application_name:str,search_string:str):
        site = 'https://wallpaperaccess.com/{search_string}'
        bs_response = self.__generate_bs_response(site,search_string)
        img_tags = bs_response.find_all('img',{'data-slug':search_string})
        for img_tag in img_tags:
            img_src = img_tag.attrs['data-src']
            img_url = 'https://wallpaperaccess.com' + img_src 
            img = re.get(img_url)
            img_file_name = application_name + img_src.replace('/','-')
            file_manager.write_temp(img_file_name,img.content)                 

    def __generate_bs_response(self,site:str,search_string:str)->BeautifulSoup:
        site = site.format(search_string = search_string)
        response = re.get(site,headers=self.__headers)
        print(f'Response ok?: {response.ok}')
        bs_response = BeautifulSoup(response.text,'html.parser')
        return bs_response

