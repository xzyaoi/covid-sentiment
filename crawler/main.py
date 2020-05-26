import datetime
import twint
import time
import pandas as pd
import os
from dateutil import tz

def crawl(date, start_time, end_time):
    start_time_str = start_time.strftime('%Y-%m-%d %H:%M:%S')
    end_time_str = end_time.strftime('%Y-%m-%d %H:%M:%S')
    print("I am going to crawl from "+start_time_str + " to "+end_time_str)
    c = twint.Config()
    c.Search = "#covid-19"
    c.Lang="en"
    c.Pandas = True
    c.Store_csv = True
    c.Retries_count = 10
    c.Custom["tweet"] = ["id", "date", "time", "tweet", "retweets_count", "likes_count"]
    c.Output = "./data/"+date+".csv"
    c.Since = start_time_str
    c.Until= end_time_str
    try:
        twint.run.Search(c)
    except Exception as e:
        print(e)
    print("Finished crawling for 1 hour, it's time to relax...")
    time.sleep(10)
    return True

def wrap_crawl(start):
    start_date = start.strftime('%Y-%m-%d')
    for i in range(24):
        start_time = start + datetime.timedelta(hours=i)
        end_time = start_time + datetime.timedelta(hours=1)
        crawl(start_date, start_time, end_time)
    print("I've finished all crawling")

def main():
    today = datetime.datetime.utcnow().date() - datetime.timedelta(days=1)
    start = datetime.datetime(today.year, today.month, today.day, tzinfo=tz.tzutc())
    wrap_crawl(start)
    

if __name__=="__main__":
    main()