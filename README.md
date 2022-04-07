# cse573-scrapers
Scrapers for CSE573, implemented using Python and Scrapy.  
So far, ebay, alibaba, and newegg have been implemented. It scrapes the results from the results page searching for "computers" or "graphics cards."

Prerequisites
- Python 3
- Scrapy
- WSL (if on windows and optional)

```
sudo apt install python3
pip install Scrapy
```

After installing Scrapy, create a new project.
```
scrapy startproject project_name
cd project_name
```

Add our spider files in the spiders folder and run the scraper.
```
scrapy crawl spider -O output.csv
```
The output file can be formatted in .csv or .json.
