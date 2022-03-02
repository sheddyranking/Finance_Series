#Introduction and Getting Real Time Stock Data.(Webscrapping)

import pandas as pd 
import datetime 
import requests
from requests.exceptions import ContentDecodingError
from bs4 import BeautifulSoup



##the fucntion to help find the information from the url below.
def web_content_div(web_content, class_path):
    web_content_div  = web_content.find_all('div', {'class': class_path})
    try:
        
        spans = web_content_div[0].find_all('span')
        texts = [span.get_text() for span in spans]
        
    except IndexError:
        
        texts = []
    
    return texts
# the Function to get the information from the URL
def real_time_price(stock_code):
    url = 'https://finance.yahoo.com/quote/' + stock_code + '?p=' + stock_code + '&.tsrc=fin-srch'
    try:
        r = requests.get(url)
        web_content = BeautifulSoup(r.text, 'lxml')
        texts = web_content_div(web_content, 'My(6px)')
        
        if texts != []:
            price, change = texts[0], texts[1]
        
        else:
              price, change = [], []
            
    except ConnectionError:
        
        price, change = [], []
        
    return price, change

#assing stock = BRK-B
stock_code = ['BRK-B']

print(real_time_price('BRK-B'))
        