# -*- coding: utf-8 -*-
"""
Created on Fri Nov 27 00:19:40 2020

@author: alida
"""

from twitterscraper import query_tweets
import datetime as dt
import pandas as pd

begin_date = dt.date(2019,4,15)
end_date = dt.date(2019,4,18)

limit = 1000
lang = "english"

tweets = query_tweets("notre dame fire", begindate = begin_date, enddate = end_date, limit=limit, lang=lang)
