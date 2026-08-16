import pandas as pd
fake=pd.read_csv('Fake.csv')
true=pd.read_csv('True.csv')
fake['label']=0
true['label']=1
data=pd.concat([fake,true],axis=0)
data=data[['title','text','label']]
data.to_csv('news.csv',index=False)
print("Data tayar zala! news.csv file banli")
print("Total rows:",len(data))