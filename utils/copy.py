# -*- coding: utf-8 -*-
"""
Created on Mon Mar 14 16:25:34 2022

@author: A2433
"""
import os
import pandas as pd
import numpy as np
from datetime import datetime, timedelta

BASE_DIR = os.path.join('..','visper-1')

if os.path.exists(r'\\10.19.13.40\DataFiles(Edit)'):
    ip_address = '10.19.13.40'
if os.path.exists(r'\\192.168.0.111\DataFiles(Edit)'):
    ip_address = '192.168.0.111'
    

def copy_ai_result(save_path):
    if not os.path.exists(save_path):
        os.mkdir(save_path)
        

if __name__ == '__main__':
    copy_ai_result(BASE_DIR)