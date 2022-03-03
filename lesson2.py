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

        
        #Lesson2.
        ## Getting and Storing Multiple Real Time Stock Data.
        ### getting the vol.
        texts = web_content_div(web_content, 'Pend(12px)')
        if texts != []:
            for count, vol in enumerate(texts):
                if vol == 'Volume':
                    volume = texts[count + 1]
        else:
            Volume = []
        

        ### getting the yahoo pattern techincal analysis.
        pattern = web_content_div(web_content, 'Mb(4px)')
        try:
            latest_pattern = pattern[0] # show any latest info.
        except IndexError:
            latest_pattern = []
        

        ### getting another info(yearly target)
        texts = web_content_div(web_content, 'Pstart(12px)')
        if texts != []:
            for count, target in enumerate(texts):
                if target  == '1y Target Est':
                    one_year_target = texts[count+1]
        else:
            one_year_target = []
                    

            
    except ConnectionError:
        
        price, change, volume, latest_pattern, one_year_target = [], [], [], [], []
        
    return price, change, volume, latest_pattern, one_year_target

#assing stock = BRK-B
stock_code = ['BRK-B']

print(real_time_price('BRK-B'))
        