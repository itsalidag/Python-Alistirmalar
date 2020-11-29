# -*- coding: utf-8 -*-
"""
Created on Fri Nov 27 00:06:30 2020

@author: alida
"""
from twitter_scraper import *
import pandas as pd

keywords = ['machinelearning', 'ML', 'deeplearning', 
            '#artificialintelligence', '#NLP', 'computervision', 'AI', 
            'tensorflow', 'pytorch', "sklearn", "pandas", "plotly", 
            "spacy", "fastai", 'datascience', 'dataanalysis']

tweets = get_tweets("#machinelearning", pages = 5)
tweets_df = pd.DataFrame(data = tweets)