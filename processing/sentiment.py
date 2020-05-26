from textblob import TextBlob
import requests
from pandarallel import pandarallel
import traceback
from wordcloud import WordCloud, STOPWORDS 
import matplotlib.pyplot as plt 
import pandas as pd
from PIL import Image
import os

pandarallel.initialize(progress_bar=True)
server_url = "http://demo.autoai.org:8082/infer"

def generate_worldcloud(texts, target):
  stopwords = set(STOPWORDS)
  stopwords.add('twitter')
  stopwords.add('pic')
  stopwords.add('utm_source')
  stopwords.add('utm_medium')
  stopwords.add('medium')
  stopwords.add('https')
  stopwords.add('html')
  stopwords.add('bit.ly')
  stopwords.add('bit ly')
  stopwords.add('bit_ly')
  stopwords.add('instagram')
  stopwords.add('covid19')
  stopwords.add('covid')

  # iterate through the csv file 
    
  wordcloud = WordCloud(width = 1500, height = 1500, 
                  background_color ='white', 
                  stopwords = stopwords,
                  max_words=1024,
                  max_font_size=75).generate(texts)
  wordcloud.to_file(target)

def compress_analyse(df):
    cols_to_keep = ['id','emotion','polarity','subjectivity','time']
    new_df = df[cols_to_keep]
    return new_df

def tb_analyse(sentence):
    tb = TextBlob(str(sentence))
    return tb.sentiment.polarity, tb.sentiment.subjectivity

def emotion_analyse(sentence):
    try:
        r = requests.post(server_url, data={'text': sentence})
        return str(r.json()['output'][0])
    except Exception as e:
        traceback.print_exc()
        return ""

def process_row(row):
    column = "text"
    row['polarity'], row['subjectivity'] = tb_analyse(row[column])
    row['emotion'] = emotion_analyse(row[column])
    return row

def wordcloud(df, target):
    texts = " ".join(str(text) for text in df.text)
    print("Processing #" + target)
    generate_worldcloud(texts, target)

def wrapper(filename):
    date = filename[5:-4]
    print("Processing # "+date +"...")
    wc_target = "./result/"+date+".png"
    senti_target = "./result/"+date+".csv"
    df = pd.read_csv(filename)
    print("I am drawing wordcloud")
    wordcloud(df, target)
    print("I am performing sentiment analyse")
    df = df.parallel_apply(process_row, axis=1)
    df = compress_analyse(df)
    df.to_csv(senti_target)
    print("Finished today's work... waiting for uploading")
