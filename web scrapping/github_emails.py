import requests
import re
from bs4 import BeautifulSoup
from csv import writer


# we can put more than one link by using list of urls
#here we will get ionic developers' emails from github
url = 'https://github.com/search?q=ionic&type=Users&p='

with open('products4.csv','w') as csv_file:
    csv_writer = writer(csv_file)
    headers = ['E-mail']

    for page in range(10):
        r = requests.get(url + str(page))
        print(url + str(page))
        soup = BeautifulSoup(r.content, "html.parser")
        for link in soup.findAll('a', attrs={'href': re.compile("^mailto:")}):
            print(link.get('href'))
            csv_writer.writerow([link.get('href')])
