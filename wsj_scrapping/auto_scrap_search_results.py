
from selenium import webdriver
import selenium.webdriver.support.ui as ui

import pandas as pd

#/Applications/Google\ Chrome.app/Contents/MacOS/Google\ Chrome  --user-data-dir="~/ChromeProfile1" --remote-debugging-port=9221
import os

#===================
keyword = "BLM;Black Lives Matter"
last_url_base = "https://www.wsj.com/search?query=%22BLM%22%3B%20%22Black%20Lives%20Matter%22&isToggleOn=true&operator=AND&sort=relevance&duration=1y&startDate=2014%2F11%2F01&endDate=2015%2F06%2F30&source=wsjie%2Cwsjsitesrch%2Cwsjpro%2Capfeed&page="
page_count = 14


id = "Michael Brown"
source = "WSJ"

#===================




port = "9221"



options = webdriver.ChromeOptions()

# options.add_argument("start-maximized")
# options.add_argument('--remote-debugging-port=9220')
options.add_experimental_option("debuggerAddress", "127.0.0.1:"+port) 
options.debugger_address="127.0.0.1:"+port
options.add_argument("--incognito")

options.add_argument('"--headless=new"')

print("not done")
driver = webdriver.Chrome(options=options)



input_path = ""
save_path = os.path.join(input_path, os.path.join( os.path.join(id, source), keyword))

os.makedirs(save_path, exist_ok=True)

# save_path = "Michael Brown/WSJ/Darren Wilson;Michael Brown;Ferguson"

for i in range(1, page_count+1):


    current_id = str(i)
    print(current_id)

    full_path = os.path.join(save_path, "p"+current_id+".txt")
    print(full_path)

    url = last_url_base+current_id

    print(url)
    driver.get(url)
    title = driver.title
    print("Processing :", title)

    with open(full_path, "w") as f :
        f.write(driver.page_source)



driver.quit()