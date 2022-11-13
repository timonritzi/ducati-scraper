from urllib.request import urlopen as uReq
from urllib.request import Request
import requests
from requests import status_codes
from selenium import webdriver
import pandas as pd
import os


def htmlParser(url):
    r = requests.get(url, headers={'User-Agent': 'facebookexternalhit/1.1'})

    if r.status_code == 200:

        return r.text

    else:
        print("failed", r.text)

def readData():

    return pd.read_csv('data.csv').fillna('').to_dict(orient="records")


def main():


    keywords = ["motorrad", "bike", "motorroller", "töff", "zweirad", "moto", "zweirad", "2-rad", "2 rad", "motorcycle", "scooter", "a1", "motorbike", "2 wheels", "2 roues", "moto-scooter"]

    records = readData()


    for i in records:

        print(i)

        if i["WEBSITE"] != '' and i["Motorrad"] == '':

            # print(i["Motorrad"])

            websiteUrl = i["WEBSITE"]

            if 'http' not in websiteUrl:

                websiteUrl = 'http://' + websiteUrl

            try:

                websiteContentRaw = htmlParser(websiteUrl)
                websiteContent = websiteContentRaw.lower()

                print(websiteContent)

                hasBikes = False

                for keyword in keywords:

                    if keyword in websiteContent:

                        hasBikes = True
                        break

                i['Motorrad'] = "ja" if hasBikes else "nein"

            except:

                print("not working", i)

                i['Motorrad'] = "nein"

    df = pd.DataFrame(records)

    df.to_csv('new_data05.csv', index=False)


main()



