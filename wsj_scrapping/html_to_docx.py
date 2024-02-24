
from docx import Document
from htmldocx import HtmlToDocx

# import pypandoc

from bs4 import BeautifulSoup
import pandas as pd 
import os

from  datetime import datetime
import csv


def save_to_csv(data, csv_out, headers):
    with open(csv_out, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)

        #Name	Location	Sources	Keywords	Author Name	Article Date	Source Link

        writer.writerow(headers) #['Headline', 'Author', 'Date', 'URL'])
        for row in data:
            writer.writerow(row)
    print(f'Data written to {csv_out}')


if __name__ =="__main__":
    

    input_path = "results_curated" #"results"
    input_html_path = "results_txt"
    output_root = "word_files"

    id = "Michael Brown"
    source = "WSJ"
    keywords_list = ["Michael Brown" , "Darren Wilson;Michael Brown;Ferguson", "BLM;Black Lives Matter" ]
    # keyword = "Michael Brown" #
    # keyword = "Darren Wilson;Michael Brown;Ferguson"
    # keyword = "BLM;Black Lives Matter"

    out_dir = os.path.join(output_root, os.path.join(os.path.join(id, source)))
    os.makedirs(out_dir, exist_ok=True)
    
    new_csv_file = os.path.join("final.csv")

    headers = ['id', 'date published', 'source', 'headline', 'author', 'description', 'directory', 'link']

    all_data = []
    unique_articles = []
    for keyword in keywords_list:
        csv_path = os.path.join(input_path, os.path.join( os.path.join(id, source), keyword+".csv"))
        df = pd.read_csv(csv_path)




        full_html_input_dir = os.path.join(input_html_path, os.path.join(os.path.join(id, source), keyword))


        for ind in df.index:
            id = df['id'][ind]
            headline = df['headline'][ind]
            url = df['link'][ind]
            date_file = df['date published'][ind]
            print(date_file)
            date_obj = datetime.strptime(date_file, '%m/%d/%y')
            date = date_obj.strftime('%B %Y')

            date_file = date_obj.strftime('%m-%d-%Y')

            
            print(date)
            print(date_file)
            
        
            current_file  = os.path.join(full_html_input_dir,headline+".txt")

            new_output_dir = os.path.join(out_dir, date)

            if not os.path.exists(new_output_dir):
                os.makedirs(new_output_dir, exist_ok=True)    

            uniq_str = headline+" "+date_file

            if uniq_str in unique_articles:
                continue
            unique_articles.append(uniq_str)
                           
            output_file = os.path.join(new_output_dir, headline+" "+date_file+".txt" )


            print(output_file)
            print(current_file)

            with open(current_file) as f:

                html_content = f.read()

                soup = BeautifulSoup(html_content, 'html.parser')

                article_selector = "article"
                articles = soup.select(article_selector)


                paragraph_selector = "p.css-k3zb6l-Paragraph"

                paragraphs = soup.select(paragraph_selector)

                with open(output_file, "w") as out_f:
                    for para in paragraphs:
                        out_f.write(para.text)
                    out_f.write("\n")
            current_data= []
            for head in headers:
                current_data.append(df[head][ind])
            #fill directory
            current_data[-2] = new_output_dir

            all_data.append(current_data)

    save_to_csv(all_data, new_csv_file, headers)