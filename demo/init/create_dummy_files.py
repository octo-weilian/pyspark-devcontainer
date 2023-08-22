#create dummy files

import numpy as np
import pandas as pd
import time
from datetime import datetime
from pathlib import Path

np.random.seed(42)

stages = ['./data/00-landing','./data/01-bronze','./data/02-silver','./data/03-gold']
for stage in stages:
    Path(stage).mkdir(parents=True, exist_ok=True)

df = pd.read_csv('./init/00-dummy.csv')
for i in range(3):
    lower_id,upper_id = df['ProductID'].min(),df['ProductID'].max()
    df['ProductID'] = np.random.randint(lower_id,upper_id,len(df))
    df.sort_values('ProductID',inplace=True)

    df['Timestamp'] = np.random.randint(1588320743,int(time.time()),len(df))
    df['Timestamp'] = df['Timestamp'] \
                    .apply(lambda x:datetime.fromtimestamp(x).strftime('%Y-%m-%d %H:%M:%S'))
    
    fname = f'./data/00-landing/0{i+1}-products.csv'
    df.to_csv(fname,index=False)
    print(fname)
