import pandas as pd

#/Applications/Google\ Chrome.app/Contents/MacOS/Google\ Chrome  --user-data-dir="~/ChromeProfile1" --remote-debugging-port=9222
import os

import csv

#========================================================

input_path = "results"

output_path="results_curated"

output_root = "results_txt"


id = "Michael Brown"
source = "WSJ"

# keyword = "Michael Brown"
# keyword = "Darren Wilson;Michael Brown;Ferguson"
keyword="Darren Wilson; Michael Brown; Ferguson"
# keyword = "BLM;Black Lives Matter"
#========================================================


keywords_to_search = [
    "Darren Wilson"," Michael Brown", "Ferguson",
"BLM","Black Lives Matter", 
"Protest", "Riot",
 "White Privilege", "Black Privilege",
 "Missouri"
,"Looting"
]

def check_if_keywords_found(curr_str):
    count=0
    for kw in keywords_to_search:
        if kw in curr_str:
            count+=1
    return count
def save_to_csv(data, csv_out, headers):
    with open(csv_out, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)

        #Name	Location	Sources	Keywords	Author Name	Article Date	Source Link

        writer.writerow(headers) #['Headline', 'Author', 'Date', 'URL'])
        for row in data:
            writer.writerow(row)
    print(f'Data written to {csv_out}')

def main():

    

    headers = ['id', 'date published', 'source', 'headline', 'author', 'description', 'directory', 'link']

    
    full_dir_path = os.path.join(input_path,  os.path.join(id, source))
    full_out_dir_path = os.path.join(output_path,  os.path.join(id, source))

    if not os.path.exists(full_out_dir_path):
        os.makedirs(full_out_dir_path, exist_ok=True)

    files_list = os.listdir(full_dir_path)

    # files_list = ["Darren Wilson;Michael Brown;Ferguson.csv"]
    count_needed=2
    for curr_file in files_list:
        if curr_file.endswith(".csv"):
            out_csv = os.path.join(full_out_dir_path, curr_file)

            print(curr_file)
            csv_path = os.path.join(full_dir_path, curr_file)
            df = pd.read_csv(csv_path)

            all_data=[]
            for i in df.index:

                if check_if_keywords_found(df["description"][i]) >=count_needed or check_if_keywords_found(df["headline"][i])>=count_needed:
                    # print("Desc:",check_if_keywords_found(df["description"][i]), df["description"][i])
                    # print("Headline",check_if_keywords_found(df["headline"][i]), df["headline"][i])
                    current_data= []
                    for head in headers:
                        current_data.append(df[head][i])
                    all_data.append(current_data)
            save_to_csv(all_data, out_csv, headers)

if __name__ == "__main__":
    main()

