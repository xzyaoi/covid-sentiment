import pandas as pd
from textblob import TextBlob
import requests
from pandarallel import pandarallel
import traceback

pandarallel.initialize(progress_bar=True)
server_url = "http://demo.autoai.org:8082/infer"

def perform_analyse(filename):
    df = pd.read_csv(filename)
    results = process_df(df)
    cols_to_keep = ['id','emotion','polarity','subjectivity','time']
    new_df = results[cols_to_keep]
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

def process_df(df):
    df = df.parallel_apply(process_row, axis=1)
    return df