# -*- coding: utf-8 -*-
"""
Created on Sun Feb 19 23:05:09 2017

@author: Administrator
"""

import pandas as pd

unames = ['./user_id', 'gender', 'age', 'occupation', 'zip']
users = pd.read_table('users.dat', sep='::', header=None, names=unames)

rnames = ['./user_id', 'movie_id', 'rating', 'timestamp']
ratings = pd.read_table('ratings.dat', sep='::', header=None, names=rnames)

mnames = ['./movie_id', 'title', 'genres']
movies = pd.read_table('movies.dat', sep='::', header=None, names=mnames)
