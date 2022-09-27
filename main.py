import datetime
# import xlsxwriter
import numpy as np
import pandas as pd

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


page_urls = ["https://ipon.ro/shop/grup/componente-pc/placa-video/463?156=11752", "https://ipon.ro/shop/grup/componente-pc/placa-video/463?156=11749"]
page_urls_evomag = ["https://www.evomag.ro/componente-pc-gaming-placi-video/filtru/model+chipset:radeon+rx+6900+xt", "https://www.evomag.ro/componente-pc-gaming-placi-video/filtru/model+chipset:radeon+rx+6800+xt"]
element_list = []
element_list_evomag = []
now = datetime.datetime.now()
current_time = now.strftime("%Y-%m-%d-%H-%M")

browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

#   Getting prices for RX 6900XT

# Getting prices on Ipon.ro

browser.get("https://ipon.ro/shop/grup/componente-pc/placa-video/463?156=11752")
titles = browser.find_elements(By.CLASS_NAME, "shop-card__title")
prices = browser.find_elements(By.CLASS_NAME, "shop-card__price")
for i in range(len(titles)):
    element_list.append([titles[i].text, prices[i].text])
df = pd.DataFrame(element_list)

# Getting prices from evomag.ro
browser.get("https://www.evomag.ro/componente-pc-gaming-placi-video/filtru/model+chipset:radeon+rx+6900+xt")
titles = browser.find_elements(By.CLASS_NAME, "npi_name")
prices = browser.find_elements(By.CLASS_NAME, "real_price")
for i in range(len(titles)):
    element_list.append([titles[i].text, prices[i].text])
df2 = pd.DataFrame(element_list)
df = df.append(df2, ignore_index=True)

# Getting prices from Cel.ro
browser.get("https://www.cel.ro/placi-video/model-i1938/radeon-rx-6900-xt/4a-1")
titles = browser.find_elements(By.CLASS_NAME, "productTitle")
prices = browser.find_elements(By.CLASS_NAME, "price")
for i in range(len(titles)):
    element_list.append([titles[i].text, prices[i].text])
df3 = pd.DataFrame(element_list)
df = df.append(df3, ignore_index=True)

# Getting prices from emag.ro
browser.get("https://www.emag.ro/placi_video/filter/procesor-video-f9897,amd-radeon-rx-6900-xt-v-9572834/c?ref=lst_leftbar_9897_-9572834")
titles = browser.find_elements(By.CLASS_NAME, "card-v2-title semibold mrg-btm-xxs js-product-url")
prices = browser.find_elements(By.CLASS_NAME, "product-new-price")
for i in range(len(titles)):
    element_list.append([titles[i].text, prices[i].text])
df4 = pd.DataFrame(element_list)
df = df.append(df4, ignore_index=True)

# Getting prices from pcgarage.ro
browser.get("https://www.pcgarage.ro/placi-video/filtre/model-model-radeon-rx-6900-xt/")
titles = browser.find_elements(By.CLASS_NAME, "product_box_name")
prices = browser.find_elements(By.CLASS_NAME, "price")
for i in range(len(titles)):
    element_list.append([titles[i].text, prices[i].text])
df5 = pd.DataFrame(element_list)
df = df.append(df5, ignore_index=True)
df = df.drop_duplicates(keep=False)


# Getting prices from pcgarage.ro
# browser.get("https://www.forit.ro/placi-video/filtre/model-model-radeon-rx-6900-xt/")
# element_list.append("De pe ForIT")
# titles = browser.find_elements(By.CLASS_NAME, "name")
# prices = browser.find_elements(By.CLASS_NAME, "price-value text-bold")
# for i in range(len(titles)):
#     element_list.append([titles[i].text, prices[i].text])
#
# df6 = pd.DataFrame(element_list)


#frames = [df, df2, df3, df4, df5]
#result = pd.concat(frames, sort=False)
#result.drop_duplicates(keep=False)

#result.to_excel(fr'Preturi-{current_time}.xlsx')

df.to_csv(fr'Preturi-{current_time}.csv')
browser.close()