# Run steps:
For every script frist run following command on a separate terminal to open browser

```/Applications/Google\ Chrome.app/Contents/MacOS/Google\ Chrome  --user-data-dir="~/ChromeProfile1" --remote-debugging-port=9221```

1. run auto_scrap_search_results.py : This extracts search results , so need to modify keywords and num_pages in search before running. output are html content for list of article links to be processed as .txt files per page
2. run blm_scrapper.py : This converts all the .txt per pages to single csv based on keywords
3. run auto_scrap_article_txt.py : extract all the urls in .csv to extract full article 
4. run html_to_docx.py:
5. output will be generated in word_files, final.csv
