# -*- coding: utf-8 -*-
"""
Created on Wed Mar 16 14:31:13 2022
@author: A2433
"""
import pandas as pd
import random
import numpy as np

path = r'\\10.19.13.40\DataFiles(Edit)\visper-1\20220318\V1-10VPJ5939IA-2X-R1\[135-Y6]_3\Panel0001\AI.csv'
set_path = r'D:\Project\avi_ai_z01\setting.txt'

def percentage_range(data):
    data = data.reset_index(drop=True)
    data.loc[0,'Values'] = 1 - data.loc[0,'Values']
    for i in range(1,len(data)):
        data.loc[i,'Values'] = data.loc[i-1,'Values'] - data.loc[i,'Values']
    return data


def roll(times, names_table):
    roll_nums = [random.uniform(0, 1) for i in range(times)]
    result = []
    for i in roll_nums:
        result.append(names_table.loc[names_table['Values'] <= i,'Parameters'].iloc[0])
    return result


def change_defects(df, setting):
    ##fillup the empty data
    if len(df.loc[df['AI_Flag'].isnull()]) > 0:
        change_nums = len(df.loc[df['AI_Flag'].isnull()])
        type_table = setting[setting['Parameters'].str.contains('VRS_')]
        type_table = percentage_range(type_table)
        result = roll(change_nums, type_table)
        result = ['TYPE' + i[4:] for i in result]
        df.loc[df['AI_Flag'].isnull(),'AI_Flag'] = result
    ##replace the defect type
    df.loc[df['AI_Flag'] == 'OSP1', 'AI_Flag'] = 'TYPE01'
    df.loc[df['AI_Flag'] == 'GOLD2', 'AI_Flag'] = 'TYPE02'
    df.loc[df['AI_Flag'] == 'SM3', 'AI_Flag'] = 'TYPE03'
    df.loc[df['AI_Flag'] == 'Copper_exposure4', 'AI_Flag'] = 'TYPE04'
    change_nums = len(df[(df['AI_Flag'] == 'Other5') | (df['AI_Flag'] == 'Tiny6')])
    type_table = setting[setting['Parameters'].str.contains('TYPE')]
    type_table = percentage_range(type_table)
    result = roll(change_nums, type_table)
    df.loc[(df['AI_Flag'] == 'Other5') | (df['AI_Flag'] == 'Tiny6'),'AI_Flag'] = result
    ##renew the type by proportion 
    proportion = setting.loc[setting['Parameters'] =='Filter rate','Values'][0]
    chosen_idx = df.loc[df['AI_Flag'].str.contains('TYPE')].index.tolist()
    replace_size = int(len(chosen_idx)*random.uniform(proportion-0.05, proportion+0.05))
    chosen_idx = np.random.choice(chosen_idx, replace = False, size = replace_size)
    df.loc[chosen_idx, 'AI_Flag'] = 'OK'
    return df


def roll_score(range_list):
    result = []
    for i in range_list:
        start = int(i[3:5])/100
        end = start + 0.1
        if end > 1:
            end = 1
        result.append(random.uniform(start, end))
    return result


def reverse_score(score_list):
    result = []
    for i in score_list:
        result.append(random.uniform(0, min(i,1-i)))
    return result
    
    
def change_score(df,setting):
    ok_nums = len(df[df['AI_Flag'] == 'OK'])
    type_table = setting[setting['Parameters'].str.contains('OK_')]
    type_table = percentage_range(type_table)
    ok_result = roll(ok_nums, type_table)
    ok_score = roll_score(ok_result)
    df.loc[df['AI_Flag'] == 'OK', 'Step_Pos_X'] = ok_score
    df.loc[df['AI_Flag'] == 'OK', 'Step_Pos_Y'] = reverse_score(ok_score)
    
    ng_nums = len(df[df['AI_Flag'].str.contains('TYPE')])
    type_table = setting[setting['Parameters'].str.contains('NG_')]
    type_table = percentage_range(type_table)
    ng_result = roll(ng_nums, type_table)
    ng_score = roll_score(ng_result)
    df.loc[df['AI_Flag'].str.contains('TYPE'), 'Step_Pos_Y'] = ng_score
    df.loc[df['AI_Flag'].str.contains('TYPE'), 'Step_Pos_X'] = reverse_score(ng_score)
    return df
    

if __name__ == '__main__':
    a = change_defects(pd.read_csv(path,header=9),pd.read_csv(set_path))
    #change_score(a,pd.read_csv(set_path))
