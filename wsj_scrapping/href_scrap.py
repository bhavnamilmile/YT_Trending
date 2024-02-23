import re
from bs4 import BeautifulSoup

# author : WSJTheme--byline--1oIUvtQ3 
# headline : WSJTheme--headlineText--He1ANr9C 
# timestamp : WSJTheme--timestamp--22sfkNDv 
# url

if __name__ =="__main__":
    file_name = "data/wsJ.txt"
    file_nameout = "data/out.txt"
    with open(file_name) as f:
        s= f.read()

        soup = BeautifulSoup(s)
        # print(soup.prettify())

        rows = soup.findAll('article')
        for article in rows:
            # print(article.prettify())
            headline = article.find_all("div")
            curr = article.find("div", {"class": "WSJTheme--search-result--2NFlrTX7"})
            curr = article.find("div", {"class": "WSJTheme--search-result--2NFlrTX7"})

                
            print(curr)
            break



        # # match = re.search(r'href=[\'"]?([^\'" >]+)', s)
        # urls = re.findall(r'href=[\'"]?([^\'" >]+)', s)
        # print('\n'.join(urls))


        # mydivs = soup.find_all("div", {"class": "stylelistrow"})


        
        # if match:
        #     print(match.group(1))