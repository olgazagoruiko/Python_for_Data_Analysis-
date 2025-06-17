import os.path
import requests
import pandas as pd



# 1. ЗАВАНТАЖЕННЯ ДАНИХ ТА ЗЧИТУВАННЯ У DataFrame

def download_document(file_name, document_url):
    if os.path.exists(file_name):
        pass
    else:
        response=requests.get(document_url)
        if response.status_code==200:
            with open(file_name,'wb') as file:
                file.write(response.content)
        else:
            print(f"Failed to download the document. Status code: {response.status_code}")


file_name='ipf_lifts.csv'
document_url='https://raw.githubusercontent.com/rfordatascience/tidytuesday/master/data/2019/2019-10-08/ipf_lifts.csv'

download_document(file_name,document_url)
##df_ipf_lifts=pd.read_table('ipf_lifts.csv')
df_ipf_lifts=pd.read_csv('ipf_lifts.csv')
pd.set_option('display.max_columns', None) # щоб було видно всі колонки
print(df_ipf_lifts.info())