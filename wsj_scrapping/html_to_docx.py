
from docx import Document
from htmldocx import HtmlToDocx

# import pypandoc

from bs4 import BeautifulSoup
import pandas as pd 
import os

from  datetime import datetime

if __name__ =="__main__":
    

    input_path = "results"
    input_html_path = "results_txt"
    output_root = "word_files"

    id = "Michael Brown"
    source = "WSJ"
    keyword = "Michael Brown" #"Darren Wilson;Michael Brown;Ferguson"


    csv_path = os.path.join(input_path, os.path.join( os.path.join(id, source), keyword+".csv"))
    df = pd.read_csv(csv_path)


    out_dir = os.path.join(output_root, os.path.join(os.path.join(id, source)))
    os.makedirs(out_dir, exist_ok=True)

    full_html_input_dir = os.path.join(input_html_path, os.path.join(os.path.join(id, source), keyword))

for ind in df.index:
    id = df['id'][ind]
    headline = df['headline'][ind]
    url = df['link'][ind]
    date_file = df['date published'][ind]
    date_obj = datetime.strptime(date_file, '%m-%d-%Y')
    date = date_obj.strftime('%B %Y')

    
    print(date)
    print(date_file)
    
   
    current_file  = os.path.join(full_html_input_dir,headline+".txt")

    new_output_dir = os.path.join(out_dir, date)

    if not os.path.exists(new_output_dir):
        os.makedirs(new_output_dir, exist_ok=True)                   
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
            # print(para.text)
