# -*- coding: utf-8 -*-
"""
Created on Fri Mar 18 13:10:28 2022

@author: A2433
"""

import pandas as pd
import os
import glob
from utils import adjust_score

BASE_DIR = os.path.join('..','visper-1')
TARGET_DIR = r'\\10.19.13.40'
set_path = r'D:\Project\avi_ai_z01\setting.txt'


def check_label(save_path,check_path,setting):
    print('STATUS: CHECKING DATA...')
    type_table = setting[setting['Parameters'].str.contains('VRS_')]
    type_table = adjust_score.percentage_range(type_table)
    check_path = os.path.join(check_path, 'ScanImages', 'visper-1')
    for k in os.listdir(check_path):
        if len(k) != 8:
            continue
        all_vrs = glob.glob((os.path.join(check_path,k,'*\*\*\VRS')))
        print('STATUS: {} - error {}'.format(k,len(all_vrs)))
        for i in all_vrs:
            print('STATUS: CORRECTING ERROR')
            change_target = i.replace(check_path,save_path).replace('\VRS','')
            df = pd.read_csv(os.path.join(change_target,'AI.csv'))
            for j in os.listdir(i):
                defect_type = adjust_score.roll(1, type_table)
                defect_type = 'TYPE' + defect_type[0][4:]
                a = df.loc[(df['AVI_Image_Path'].str.contain(j)) & (df['AI_Flag'] == 'OK'), 'Step_Pos_Y']
                df.loc[(df['AVI_Image_Path'].str.contain(j)) & (df['AI_Flag'] == 'OK'), 'Step_Pos_Y'] = df.loc[(df['AVI_Image_Path'].str.contain(j)) & (df['AI_Flag'] == 'OK'), 'Step_Pos_X']
                df.loc[(df['AVI_Image_Path'].str.contain(j)) & (df['AI_Flag'] == 'OK'), 'Step_Pos_X'] = a
                df.loc[(df['AVI_Image_Path'].str.contain(j)) & (df['AI_Flag'] == 'OK'), 'AI_Flag'] = defect_type
            df.to_csv(os.path.join(change_target,'AI.csv'))
            print('STATUS: DONE')
        
    
if __name__ == '__main__':
    check_label(BASE_DIR,TARGET_DIR,pd.read_csv(set_path))
    pass
    