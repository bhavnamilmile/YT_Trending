
from selenium import webdriver
import selenium.webdriver.support.ui as ui

import pandas as pd

#/Applications/Google\ Chrome.app/Contents/MacOS/Google\ Chrome  --user-data-dir="~/ChromeProfile1" --remote-debugging-port=9222
import os
import time

#========================================================

input_path = "results_curated"
output_root = "results_txt"


id = "Michael Brown"
source = "WSJ"

# keyword = "Michael Brown"
# keyword = "Darren Wilson;Michael Brown;Ferguson"
keyword = "BLM;Black Lives Matter"
#========================================================










# csv_path = os.path.join(input_path, os.path.join( os.path.join(id, source), keyword+".csv"))
# df = pd.read_csv(csv_path)


# out_dir = os.path.join(output_root, os.path.join(os.path.join(id, source), keyword))
# os.makedirs(out_dir, exist_ok=True)





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





full_dir_path = os.path.join(input_path,  os.path.join(id, source))
out_dir = os.path.join(output_root,  os.path.join(id, source))

if not os.path.exists(out_dir):
    os.makedirs(out_dir, exist_ok=True)

files_list = os.listdir(full_dir_path)

# files_list = ["Darren Wilson;Michael Brown;Ferguson.csv"]
count_needed=2

headlines=[]
for curr_file in files_list:
    if curr_file.endswith(".csv"):
        csv_path = os.path.join(full_dir_path, curr_file)
        print("Processing", csv_path)
        df = pd.read_csv(csv_path)
        for ind in df.index:
            id = df['id'][ind]
            headline = df['headline'][ind]
            url = df['link'][ind]
            date = df['date published'][ind]

            if headline in headlines:
                continue

            output_file  = os.path.join(out_dir,headline+".txt")

            if os.path.exists(output_file):
                print("File exists: ", output_file)
                continue
            
            print(output_file)
            print(url)
            driver.get(url)

            title = driver.title
            print("Processing :", title)
            full_path = os.path.join(output_file)
            with open(full_path, "w") as f :
                f.write(driver.page_source)
            
            headlines.append(headline)
            time.sleep(1)


driver.quit()