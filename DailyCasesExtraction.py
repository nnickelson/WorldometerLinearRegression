# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import requests
from itertools import repeat

def new_cases(URL):
    
    page = requests.get(URL)
    txt = page.content
    soup = BeautifulSoup(txt, 'html.parser')
    script = soup.find_all("script")
    
    t_script = ""
    t_index = 0
    for scr in script:
        str_script = str(scr)
        int_index = str_script.find("'Daily Cases'")
        if int_index < 0:
            continue
        t_script = str_script
        t_index = int_index
        break
    index1 = t_script.find("[", t_index) + 1
    index2 = t_script.find("]", t_index)
    list_ints = (t_script[index1 : index2]).split(',')
    new_cases = []
    for i in list_ints:
        try:
            new_cases.append(int(i))
        except :
            continue
    return new_cases