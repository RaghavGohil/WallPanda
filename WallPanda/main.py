import config
import utils.gui as gui
import utils.scraper as scraper

def search(search_string:str):
    search_string = search_string.replace(' ','-')
    web_scraper = scraper.Scraper()
    web_scraper.scrape_wallpaperaccess(config.APPLICATION_NAME,search_string) 

def main():
    application = gui.App(config.APPLICATION_NAME,config.APPLICATION_GEOMETRY)
    application.mainloop()
    x = input('search:')
    search(x)

main()