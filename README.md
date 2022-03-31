# cse573-scrapers
Scrapers for CSE573, implemented using Python and Scrapy.  
So far, ebay has been implemented. It scrapes the results from searching for "graphics cards."

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

Add my ebay spider file in the spiders folder.
Run the scraper.
```
scrapy crawl ebay -O output.csv
```
The output file can be formatted in .csv or .json.
