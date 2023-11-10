import config
from utils.gui import * 
from utils.scraper import * 

def search(search_string:str):
    search_string = search_string.replace(' ','-')
    scraper = Scraper()
    scraper.scrape_wallpaperaccess(config.APPLICATION_NAME,search_string) 

def main():
    application = App(config.APPLICATION_NAME,config.APPLICATION_GEOMETRY)
    application.mainloop()
    x = input('search:')
    search(x)

main()