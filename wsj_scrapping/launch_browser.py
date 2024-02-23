
from selenium import webdriver
import selenium.webdriver.support.ui as ui
#/Applications/Google\ Chrome.app/Contents/MacOS/Google\ Chrome  --user-data-dir="~/ChromeProfile1" --remote-debugging-port=9222
import os
port = "9222"



options = webdriver.ChromeOptions()

# options.add_argument("start-maximized")
# options.add_argument('--remote-debugging-port=9220')
options.add_experimental_option("debuggerAddress", "127.0.0.1:"+port) 
options.debugger_address="127.0.0.1:"+port
options.add_argument("--incognito")

print("not done")
driver = webdriver.Chrome(options=options)


# for handle in driver.window_handles:
#     driver.switch_to.window(handle)
#     print(driver.current_url)
# print("done")
# last_url = "https://www.wsj.com/search?query=%22Darren%20Wilson%22%3B%20%22Michael%20Brown%22%3B%20%22Ferguson%22&isToggleOn=true&operator=AND&sort=relevance&duration=1y&startDate=2014%2F11%2F01&endDate=2015%2F06%2F30&source=wsjie%2Cwsjsitesrch%2Cwsjpro%2Capfeed&page=1"

last_url = None

current_id = last_url.split('=')[-1]
print(current_id)
save_path = "Michael Brown/WSJ/Darren Wilson;Michael Brown;Ferguson"

full_path = os.path.join(save_path, "p"+current_id+".txt")
print(full_path)


while True:

    if driver.current_url != last_url:
        # print(driver.page_source)
        last_url = driver.current_url
        current_id = last_url.split('=')[-1]
        print("Processed = ", current_id)
        full_path = os.path.join(save_path, "p"+current_id+".txt")
        with open(full_path, "w") as f :
            f.write(driver.page_source)


    else:
        print(current_id, end="\r")


driver.quit()