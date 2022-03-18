# -*- coding: utf-8 -*-
"""
Created on Fri Mar 18 09:57:17 2022

@author: A2433
"""

import os
import pandas as pd
import numpy as np
import utils.copy as cp

setting_dir = os.path.join('.','setting.txt')
base_dir = os.path.join('.','visper-1')

def load_init():
    if not os.path.exists(setting_dir):
        default = [['SCORE RANGE : ',np.nan],
                   ['OK_99%',0.767],
                   ['OK_90%',0.110],
                   ['OK_80%',0.038],
                   ['OK_70%',0.030],
                   ['OK_60%',0.023],
                   ['OK_50%',0.018],
                   ['OK_40%',0.012],
                   ['OK_30%',0.002],
                   ['NG_99%',0.649],
                   ['NG_90%',0.258],
                   ['NG_80%',0.043],
                   ['NG_70%',0.021],
                   ['NG_60%',0.012],
                   ['NG_50%',0.009],
                   ['NG_40%',0.006],
                   ['NG_30%',0.001],
                   ['NG_20%',0.001],
                   ['DEFECT PERCEMTAGE : ',np.nan],
                   ['TYPE05',0.030],
                   ['TYPE06',0.557],
                   ['TYPE07',0.021],
                   ['TYPE08',0.043],
                   ['TYPE09',0.048],
                   ['TYPE10',0.029],
                   ['TYPE11',0.161],
                   ['TYPE12',0.027],
                   ['TYPE13',0.024],
                   ['TYPE14',0.060],
                   ['VRS DEFECT PERCEMTAGE : ',np.nan],
                   ['VRS_01',0.283],
                   ['VRS_02',0.140],
                   ['VRS_03',0.212],
                   ['VRS_04',0.011],
                   ['VRS_05',0.010],
                   ['VRS_06',0.197],
                   ['VRS_07',0.008],
                   ['VRS_08',0.015],
                   ['VRS_09',0.017],
                   ['VRS_10',0.010],
                   ['VRS_11',0.057],
                   ['VRS_12',0.009],
                   ['VRS_13',0.009],
                   ['VRS_14',0.022]]
        setting = pd.DataFrame(default,columns = ['Parameters', 'Values'])
        setting.to_csv(setting_dir, index = False)
    else:
        setting = pd.read_csv(setting_dir)
    return setting


if __name__ == '__main__':
    setting_df = load_init()
    print('STATUS: GET IP')
    ip_path = cp.get_ip_address()
    print('STATUS: START COPY')
    cp.copy_ai_result(base_dir,ip_path,setting_df)
    