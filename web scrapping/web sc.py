import requests
from bs4 import BeautifulSoup
from csv import writer

import urllib.request
import os


response = requests.get('https://www.sultan-center.com/fresh-food.html/fruit-veg.html')

# print(response)
soup = BeautifulSoup(response.text , 'html.parser')

products = soup.findAll(class_='item product product-item')

with open('products.csv','w') as csv_file:
    csv_writer = writer(csv_file)
    headers = ['Title','image Link','image','measurement']


    for product in products:
        title = product.find(class_='product-item-link').get_text().replace('\n', '')
        # print(title)
        image_link = product.find(class_='product-image-wrapper').find('img')['src']
        print(image_link)
        if not os.path.exists('images'):
            os.makedirs('images')
        image = urllib.request.urlretrieve(image_link , "images/{}.jpg".format(title.strip()))
        print(image)
        measurement = product.find(class_='product_measurement').find('span').get_text().replace('\n','')
        csv_writer.writerow([title,image_link,image,measurement])

