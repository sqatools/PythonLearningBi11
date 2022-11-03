"""
Selenium : browser interaction
BeautifulSoup : Data Parcing
Pandas

pip install selenium
pip install BeautifulSoup
"""

from selenium import webdriver
from bs4 import BeautifulSoup
import pandas
import time

products = []
prices = []
ratings = []

driver = webdriver.Chrome()
driver.get("https://www.flipkart.com/laptops/laptops~buyback-guarantee-on-laptops-/pr?sid=6bo%2Cb5g&page=19")

driver.maximize_window()
page_content = driver.page_source
#print(page_content)
soup_obj = BeautifulSoup(page_content)
for a in soup_obj.find_all('a', href=True, attrs={'class': '_1fQZEK'}):
    #print(a)
    prod_name = a.find('div', attrs={'class': '_4rR01T'})
    prod_price = a.find('div', attrs={'class': '_30jeq3 _1_WHN1'})
    prod_rating = a.find('div', attrs={'class': '_3LWZlK'})
    if prod_name is not None:
        products.append(prod_name.text)
    else:
        products.append(0)
    if prod_price is not None:
        prices.append(prod_price.text)
    ratings.append(prod_rating.text)


print(products)
print(prices)
print(ratings)

time.sleep(10)


driver.close()



