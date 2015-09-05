#!/usr/local/bin/python3.4
# coding: utf-8

# In[1]:

import os
"""
NADAV - CHANGE THIS TO THE LOCATION OF THE OTHER FILE I ATTACHED
"""
known_posts_file = "/Users/yotamvaknin/scripts/known_posts.txt"
try :
    with open(known_posts_file,"r") as f:
        known_hosts = f.read()
except :
    with open(known_posts_file,"w") as f:
        known_hosts = ""
def add_post_to_known_posts(post):
    with open(known_posts_file,"a") as f:
        f.write(post.id +'\n')


# In[2]:

from urllib import request
from urllib.parse import urlencode
from json import loads
from collections import namedtuple
import contextlib


# In[3]:

limit = 300
"""
NADAV - ADD HERE YOUR FACEBOOK ACCESS TOKEN
YOU CAN GET IT FROM HERE:
https://developers.facebook.com/tools/explorer/
"""
access_token ='' 
url = "https://graph.facebook.com/v2.0/172544843294/feed/?access_token={}&limit={}"
res = loads(request.urlopen(url.format(access_token,limit)).read().decode('utf8'))
data = res['data']


# In[4]:

# In[5]:

def hebrew_to_english(text):
    translate = {chr(ord('א')+heb):eng for heb,eng in zip(range(27),"abgdhwzhtycclmmnnseppzzkrrst")} 
    translate[' '] = '-'
    translate[','] = ','
    return "".join(translate[i] for i in text if i in translate)

yotam_phone_number = '972546888972'

"""
NADAV - UPDATE THE URL WITH THE API_KEY AND API_SECRET 
YOU CAN GET IT FROM nexmo.com
"""

def send_text(text,number):
    nexmo_url = "https://rest.nexmo.com/sms/json?api_key=&api_secret=&from=NEXMO&to={number}&text={text}"
    request.urlopen(nexmo_url.format(number = number,text = request.quote(text.encode('utf8'))))
def text_post(post):
    text = "{link} at {neighborhood} for {prices}".format(link = post.get_link(),
                                                         neighborhood = hebrew_to_english(str(post.neighborhood)),
                                                          prices = str(post.prices))
    send_text(text,yotam_phone_number)


# In[6]:

import re
fields = 'id,message,link,updated_time,prices,neighborhood'.split(',')#,comments,likes'
Neighborhoods = "רחביה,בית הכרם,רסקו,נחלאות,גבעת רם".split(',')

class Post:
    def __init__(self,dictionary):
        for field in fields:
            setattr(self,field,dictionary.get(field,''))
        self.prices = [float(num) for num in re.findall(r'(\d{3,4})',self.message)]
        self.neighborhood = [neighborhood for neighborhood in Neighborhoods if neighborhood in self.message]
    def get_link(self):
        return 'https://www.facebook.com/groups/{}/?view=permalink&id={}'.format(*self.id.split('_'))
    def __iter__(self):
        return (getattr(self,field) for field in fields)
posts = [Post(d) for d in data]


# In[7]:

import re
def filter_posts(posts):
    for post in posts:
        if post.neighborhood:
            if any(price < 1800 or 3000 < price < 5300  for price in post.prices):
                yield post


# In[8]:

import pandas as pd
from dateutil import parser
relevant_posts =list(filter_posts(posts))


# In[9]:

for post in relevant_posts:
    if post.id not in known_hosts:
        text_post(post)
        print("New Post {}".format(post.id))
        add_post_to_known_posts(post)


# In[ ]:




# In[ ]:


print("Test")
