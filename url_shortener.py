import pyshorteners

import csv 
import os 


def savetocsv(full_url, short_url):
    file_exists = os.path.isfile('urls.csv')
    with open('urls.csv', 'a', newline='') as csvfile:
        fieldnames = ['full_url', 'short_url']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        if not file_exists:
            writer.writeheader()
        writer.writerow({'full_url': full_url, 'short_url': short_url})

def shorten_url(full_url):
    s = pyshorteners.Shortener()
    try:
        short_url = s.tinyurl.short(full_url)
        savetocsv(full_url, short_url)
        return short_url
    except Exception as e:
        return f"Error: {str(e)}"


def expand_url(short_url):
    s = pyshorteners.Shortener()
    try:
        full_url = s.tinyurl.expand(short_url)
        return full_url
    except Exception as e:
        return f"Error: {str(e)}"
    

def count_shortened_urls():
    if not os.path.isfile('urls.csv'):
        return 0
    with open('urls.csv', 'r') as csvfile:
        reader = csv.reader(csvfile)
        return sum(1 for row in reader) - 1 