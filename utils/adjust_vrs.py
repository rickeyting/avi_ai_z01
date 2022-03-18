# -*- coding: utf-8 -*-
"""
Created on Fri Mar 18 13:10:28 2022

@author: A2433
"""

import pandas as pd
import numpy as np
import os
import glob

def load_history(record_path):
    if not os.path.exists(record_path):
        compare_table = pd.DataFrame(columns = ['path','nums'])
    else:
        compare_table = pd.read_csv(record_path)
    return compare_table


def check_label(path,check_df,ai_path):
    renew_list = glob.glob((os.path.join(path,'*\*\*\VRS')))
    #if len(renew_list) == check_df.loc[check_df['path'] == path]['nums']:
        #return 'un-changed'
    base_path = r'\\10.19.13.40\ScanImages\visper-1'
    for i in renew_list:
        target = i.replace(base_path,'')
        target = target.replace('\VRS','')
        target = ai_path+target
        print(ai_path)
        print(target)
    #check_df.loc[check_df['path'] == path,'nums'] = len(renew_list)
    
if __name__ == '__main__':
    pass