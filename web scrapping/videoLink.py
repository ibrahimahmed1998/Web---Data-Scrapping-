
from bs4 import BeautifulSoup
import re
import requests
from csv import writer


site = ["https://www.youtube.com/watch?v=zqsxNMRgKCQ&list=PL32HFpx_LBMvXp5HK9t4JWWMLyKhSILt8&index=7"]
allsite = []
linkes = []
with open('products3.csv','w') as csv_file:
    csv_writer = writer(csv_file)
    headers = ['E-mail','Tel']

    for l in site:
        r = requests.get(l)
        soup = BeautifulSoup(r.content, "html.parser")

        for link in soup.findAll('a', attrs={'href': re.compile("^https:")}):
            allsite.append(link.get('href'))
            csv_writer.writerow([link.get('href')])

    print(allsite)
    print('------------')
    for l in allsite:
        r = requests.get(l)
        soup = BeautifulSoup(r.content, "html.parser")
        for link in soup.findAll('iframe', attrs={}):
            linkes.append(link.get('src'))
            print(link.get('src'))
            csv_writer.writerow([link.get('src')])

print("Finsihed")