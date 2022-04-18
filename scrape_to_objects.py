#Marie Valentonis 4.15.2022
#Web Scraper

from mimetypes import init
import colorize_plugin
import requests
from bs4 import BeautifulSoup

init #Initialize colorize_plugin

# herb = "chamomile"
# substring = "the"
URL = "https://www.nccih.nih.gov/health/chamomile"
page = requests.get(URL)
# datas = []

#.content attribute holds raw bytes, which can be decoded better
#html.parser calls the appropriate parser for data type html
soup = BeautifulSoup(page.content, "html.parser")

text = soup.find(class_="css-1z0obd3").get_text()

print(text)



    


    

#TO NOTATE
#print(f"This is a formatting string with the variable {herb}.")
#TO DO
#Import [Herbs] and pass value in for loop




