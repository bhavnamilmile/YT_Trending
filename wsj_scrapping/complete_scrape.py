from bs4 import BeautifulSoup
import csv
# headline : #main > div:nth-child(5) > article:nth-child(1) > div > div.WSJTheme--search-text-combined--29JN8aap > div.WSJTheme--search-combined-headline-summary--1bmOvoTg > div.WSJTheme--headline--7VCzo7Ay

# headline text : WSJTheme--headlineText--He1ANr9C
# headline : WSJTheme--headline--7VCzo7Ay 

# Example selectors; adjust based on actual HTML structure
headline_selector = 'div.WSJTheme--headline--7VCzo7Ay'  # Adjust this to match the headline's HTML tag and attributes
author_selector = 'p.WSJTheme--byline--1oIUvtQ3'  # Adjust this to match the author's HTML tag and attributes
date_selector = 'p.WSJTheme--timestamp--22sfkNDv'  # Adjust this to match the date's HTML tag and attributes
url_selector = 'a'  # This often points to the article's URL

date_format = '%B %d, %Y %I:%M %p ET'

output_date_format = '%m-%d-%Y'

from datetime import datetime

import os 
def save_article_attrib_to_csv(data, csv_out):
    with open(csv_out, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        # Write the headers
        writer.writerow(['Headline', 'Author', 'Date', 'URL'])
        # Write article data
        for row in data:
            writer.writerow(row)

    print(f'Data written to {csv_out}')


def extract_info(file_name, csv_out):

    data = []
    urls = []
    with open(file_name) as f:
        html_content= f.read()
        # Assuming 'html_content' is a variable containing the HTML content
        soup = BeautifulSoup(html_content, 'html.parser')


        articles = soup.select('article.WSJTheme--story--XB4V2mLz')
        # print(rows)
        # articles = soup.select('.article')
        
        for article in articles:
            # print(article)
            headline = article.select_one(headline_selector).text.strip() if article.select_one(headline_selector) else 'HEADLINE_NOT_FOUND'
            author = article.select_one(author_selector).text.strip() if article.select_one(author_selector) else 'AUTHOR_NOT_FOUND'
            date = article.select_one(date_selector).text.strip() if article.select_one(date_selector) else 'DATE_NOT_FOUND'
            url = article.select_one(url_selector)['href'] if article.select_one(url_selector) else 'URL_NOT_FOUND'
            

            # Parse the original date string to datetime object
            date_obj = datetime.strptime(date, date_format)

            # Format the datetime object to the desired string format
            date = date_obj.strftime(output_date_format)


            # Append each article's data to the list
            data.append([headline, author, date, url])

            urls.append(url)

            save_article_attrib_to_csv(data, csv_out)


    return data, urls




if __name__ =="__main__":

    print(os.listdir("data"))
    data_all, urls_all = [], []
    
    for curr_file in os.listdir("data"):
        file_name = os.path.join("data", curr_file)
        out_fl_name = curr_file.split(".")[0] +".csv"
        
        csv_out = os.path.join("results",out_fl_name)

        print(file_name)
        print(csv_out)
        data, urls = extract_info(file_name, csv_out)
        data_all.extend(data)
        urls_all.extend(urls_all)

    

    save_article_attrib_to_csv(data_all, "results/complete.csv")