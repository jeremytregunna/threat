from datetime import datetime
from hurry.filesize import size
import json
import pandas as pd
import urllib.error
import urllib.request

hourly_filesize = 0

def fetch_current(url):
    filename = datetime.utcnow().strftime("%Y%m%d-%Hh.json")
    urllib.request.urlretrieve(url, filename=filename, reporthook=report_download)
    with open(filename, "r") as f:
        res = json.loads(f.read())
        print(f"\033[2KDownloaded {size(hourly_filesize)} in total for hourly attacks data")
        return res

def report_download(count, blockSize, totalSize):
    global hourly_filesize
    hourly_filesize += blockSize
    print(f"\033[2KDownloaded: {size(hourly_filesize)}\033[F")

if __name__ == "__main__":
    countries = pd.read_csv("countries.csv")
    attacks = fetch_current("https://www.gstatic.com/ddos-viz/attacks_v2.json")
