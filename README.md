# Singapore Pools 4D Scraper

Crawls up to past one year of Singapore 4D result.

## Scrapy

Require [Scrapy](https://scrapy.org/) to work

### Install Scrapy

`pip install scrapy`

## How to use

- Copy `fourd/settings.py.example` to `fourd/settings.py`
- Change your own settings

### Export to JSON

`scrapy crawl fourd -o result.json -t json`

### Dump to MySQL

You are required to run db_structure.sql and configure `fourd/settings.py` to fit your database credentials.

`scrapy crawl fourd`


## mysql -u root -pSim1lyplan -e "use four;select distinct(number) from numbers where number > 1000  and number < 2000 order by number" > /Users/i321395/1000-2000.txt