# -*- coding: utf-8 -*-
"""
Created on Mon Mar 14 16:25:34 2022

@author: A2433
"""
import os
import pandas as pd
from datetime import datetime, timedelta, date
import glob
from utils import adjust_score
from tqdm import tqdm

BASE_DIR = os.path.join('..','visper-1')
RECORD_DIR = os.path.join('..','checked.csv')
SETTING_DIR = os.path.join('.','setting.txt')

def get_ip_address():
    
    if os.path.exists(r'\\10.19.13.40\ScanImages'):
        return r'\\10.19.13.40'
    elif os.path.exists(r'\\192.168.0.111\ScanImages'):
        return r'\\192.168.0.111'
    else:
        print('STATUS: unconnected, Please check the internet connection')
        print('STATUS: retry press ENTER...')
    

def check_ai_files(raw_d_path,save_path,setting_path):
    if not os.path.exists(save_path):
        os.makedirs(save_path)
    print('STATUS: GET AI FILES COMPARE')
    all_ai_nums = glob.glob((os.path.join(raw_d_path,'*\*\*\AI.csv')))
    cur_ai_nums = glob.glob((os.path.join(save_path,'*\*\*\AI.csv')))
    print('STATUS: COPY {}'.format(raw_d_path))
    if len(all_ai_nums) != len(cur_ai_nums):
        for i in tqdm(all_ai_nums):
            df = pd.read_csv(i,header=9)
            save_dir = i.replace(raw_d_path,save_path)
            folder_path = save_dir.replace('\AI.csv','')
            if not os.path.exists(folder_path):
                os.makedirs(folder_path)
            df = adjust_score.change_defects(df,setting_path)
            df = adjust_score.change_score(df,setting_path)
            df.to_csv(save_dir,index = False)

    
    
def copy_ai_result(save_path,check_path,setting_path,check_range = 1):
    check_path = os.path.join(check_path, 'DataFiles(Edit)', 'visper-1')
    if not os.path.exists(save_path):
        os.mkdir(save_path)
    original_date = os.listdir(save_path)
    current_date = os.listdir(check_path)
    current_date = [i for i in current_date if len(i)==8]
    un_update_date = list(set(current_date) - set(original_date))
    today = date.today().strftime('%Y%m%d')
    if not today in un_update_date:
        un_update_date.append(today)
    last_date = (datetime.strptime(min(un_update_date),'%Y%m%d') - timedelta(days = 1)).strftime('%Y%m%d')
    if last_date in current_date:
        un_update_date.append(last_date)
    for i in un_update_date:
        print('STATUS: COPY {}'.format(i))
        check_target = os.path.join(check_path,i)
        save_target = os.path.join(save_path,i)
        check_ai_files(check_target,save_target,setting_path)

if __name__ == '__main__':
    target_dir = get_ip_address()
    copy_ai_result(BASE_DIR,target_dir,pd.read_csv(SETTING_DIR))