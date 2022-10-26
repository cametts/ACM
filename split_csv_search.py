import pandas as pd 
from nltk.stem.snowball import SnowballStemmer
import json
import os
import sys

if getattr(sys, 'frozen', False) and hasattr(sys, '_MEIPASS'):
    os.chdir(sys._MEIPASS)

def search(word):
    folder = 'data'
    found = False
    file_list = pd.read_csv(f'{folder}/FileNames_all.csv', sep='TestDelim123456789', engine='python', encoding='utf-8', header=None)
    print(file_list)
    file_list = file_list[0].tolist()

    #Process word
    stemmer = SnowballStemmer('arabic')
    word = stemmer.stem(word)

    #Search for word
    index_list = []
    for file in file_list:
        print(file)
        if found is True:
            break

        if file.endswith('.csv'):
            try:
                index_list = pd.read_csv(file, usecols=[word], encoding='utf-8')
                index_list = index_list[word]
                found = True
            except:
                continue

        elif file.endswith('.gzip'):
            df = pd.read_parquet(file)
            try:
                index_list = df[word]
                found = True
            except:
                continue
    
    if len(index_list) == 0:
        return pd.DataFrame({'Files' : ''}, index=[0])
    index_list = index_list.dropna().astype(int).tolist()

    #Convert indices to filenames 
    json_path = 'data/index_to_names.json'
    with open(json_path, 'r', encoding='utf-8') as f:
        index_dict = json.load(f)

    file_series = pd.DataFrame({'Files' : [index_dict[str(index)] for index in index_list if index != 18397]})
    return file_series

if __name__ == '__main__':
    print(search("الحب"))



    

