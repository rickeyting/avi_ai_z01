# -*- coding: utf-8 -*-
"""
Created on Wed Mar 16 14:31:13 2022

@author: A2433
"""

def create_data(ok_nums,ng_nums):
    def auto_add(main,high,low):
        types = []
        for a in range(1,15):
            if a == 1:
                types.append(random.uniform(high, 1))
            else:
                types.append(random.uniform(0, low))
        random_no = random.randrange(1,14)
        temp=types[0]
        types[0]=types[main-1]
        types[main-1]=tem       
        return types

    path = os.path.join(FINAL_CHART_DATA, '{}.csv'.format(refer))
    refer_df = pd.read_csv(path)
    #refer_df = refer_df.groupby(['VRS']).count().reset_index()
    refer_df['scale'] = refer_df['Image']/refer_df['Image'].sum()*total
    refer_df = refer_df[['VRS','scale']]
    df = pd.DataFrame(data = {'VRS': range(0,15)})
    refer_df = pd.merge(df,refer_df,how='left')
    refer_df = refer_df.fillna(1.5)
    random_range = 0.9
    quantity_list = []    
    for a in refer_df['scale'].tolist():
        quantity_list.append(int(random.uniform(a*0.9, a*1.1)))
    refer_df['scale'] = pd.Series(quantity_list)
    
    acc_rate_list = []    
    for a in refer_df['scale'].tolist():
        acc_high = random.uniform(acc_rate, acc_rate+5)/100
        acc_low = random.uniform(acc_rate-5, acc_rate)/100
        acc_rate_list.append(int(random.uniform(a*acc_low, a*acc_high)))
    refer_df['acc'] = pd.Series(acc_rate_list)
    
    
    overkill_list = []
    overkill_all = refer_df.loc[0]['scale'] - refer_df.loc[0]['acc']
    refer_df.loc[0,'overkill'] = 0
    refer_df.loc[1:15,'overkill'] = refer_df[1:15]['scale']
    refer_df['overkill'] = refer_df['overkill']/refer_df['overkill'].sum()*overkill
    for a in refer_df['overkill'].tolist():
        overkill_list.append(int(random.uniform(a*0.9, a*1.1)))
    refer_df['overkill'] = pd.Series(overkill_list)
    
    refer_df.loc[0,'scale'] = refer_df['overkill'].sum() + refer_df.loc[0]['acc']
    threshold = 0.6

    #print(refer_df)
    
    
    scroe = []
    
    for ac in range(int(refer_df.loc[0]['acc']*0.007)):
        OK = random.uniform(threshold*1.5, 1)
        main = [OK,1-OK]
        tail = [0,0]
        types = []
        for b in range(1,15):
            types.append(random.uniform(0, 1-OK))
        
        types = [i/sum(types) for i in types]
        types = [i*(1-OK) for i in types]
        scroe.append(main+types+tail)
    for ac in range(int(refer_df.loc[0]['acc']*0.99)):
        OK = 0.9999
        #OK = random.uniform(threshold*1.65, 1)
        main = [OK,1-OK]
        tail = [0,0]
        types = []
        for b in range(1,15):
            types.append(random.uniform(0, 1-OK))
        
        types = [i/sum(types) for i in types]
        types = [i*(1-OK) for i in types]
        scroe.append(main+types+tail)
    for ac in range(int(refer_df.loc[0]['acc']*0.003)):
        OK = random.uniform(threshold, 1)
        main = [OK,1-OK]
        tail = [0,0]
        types = []
        for b in range(1,15):
            types.append(random.uniform(0, 1-OK))
        
        types = [i/sum(types) for i in types]
        types = [i*(1-OK) for i in types]
        scroe.append(main+types+tail)
        
    for ac in range(1,15):
        
        for b in range(int(refer_df.loc[ac]['overkill']*0.01)):
            OK = random.uniform(0.3, threshold)
            main = [OK,1-OK]
            tail = [0,ac]
            types = auto_add(ac,0.5,0.5)
            types = [i/sum(types) for i in types]
            types = [i*(1-OK) for i in types]
            scroe.append(main+types+tail)
        for b in range(int(refer_df.loc[ac]['overkill']*0.19)):
            OK = random.uniform(0.4, threshold)
            main = [OK,1-OK]
            tail = [0,ac]
            types = auto_add(ac,0.5,0.5)
            types = [i/sum(types) for i in types]
            types = [i*(1-OK) for i in types]
            scroe.append(main+types+tail)
        
        for b in range(int(refer_df.loc[ac]['overkill']*0.8)):
            OK = random.uniform(0.5, threshold)
            main = [OK,1-OK]
            tail = [0,ac]
            types = auto_add(ac,0.5,0.5)
            types = [i/sum(types) for i in types]
            types = [i*(1-OK) for i in types]
            scroe.append(main+types+tail)
        
        for b in range(int(refer_df.loc[ac]['acc']*0.6)):
            OK = random.uniform(0, 0.001)
            main = [OK,1-OK]
            tail = [ac,ac]
            types = auto_add(ac,0.9,0.001)
            types = [i/sum(types) for i in types]
            types = [i*(1-OK) for i in types]
            scroe.append(main+types+tail)
        
        for b in range(int(refer_df.loc[ac]['acc']*0.3)):
            limitation = random.uniform(0,0.15)
            OK = random.uniform(0, limitation)
            main = [OK,1-OK]
            tail = [ac,ac]
            types = auto_add(ac,0.9,0.001)
            types = [i/sum(types) for i in types]
            types = [i*(1-OK) for i in types]
            scroe.append(main+types+tail)
        for b in range(int(refer_df.loc[ac]['acc']*0.1)):
            limitation = random.uniform(0,0.3)
            OK = random.uniform(0, limitation)
            main = [OK,1-OK]
            tail = [ac,ac]
            types = auto_add(ac,0.9,0.001)
            types = [i/sum(types) for i in types]
            types = [i*(1-OK) for i in types]
            scroe.append(main+types+tail)
            
        for b in range(int((refer_df.loc[ac]['scale']-refer_df.loc[ac]['acc']))):
            #limitation = random.uniform(0,0.5)
            cc = random.randrange(1,15)
            OK = random.uniform(0, 0.2)
            main = [OK,1-OK]
            tail = [ac,cc]
            types = auto_add(cc,0.9,0.1)
            types = [i/sum(types) for i in types]
            types = [i*(1-OK) for i in types]
            scroe.append(main+types+tail)
    
    df = pd.DataFrame(np.array(scroe),columns=['OK','NG',1,2,3,4,5,6,7,8,9,10,11,12,13,14,'VRS','AI'])
    df['result_ok'] = df['OK']
    all_list = [*range(1,15,1)]
    df['result_ng'] = df[all_list].max(axis=1)
    print(df)
    original_data_dir_csv = os.path.join(ORIGINAL_DATA_PATH,'{}.csv'.format(filename))
    original_data_dir_csv2 = os.path.join(ORIGINAL_DATA_PATH,'o{}.csv'.format(filename))
    df.to_csv(original_data_dir_csv,index=False)
    df.to_csv(original_data_dir_csv2,index=False)