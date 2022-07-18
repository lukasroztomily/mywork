#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb  9 18:09:12 2022

@author: erik
"""
import json
a = open("result.json", "r")

tweets = []
for line in open('result.json', 'r'):
    tweets.append(json.loads(line))
    print(tweets)