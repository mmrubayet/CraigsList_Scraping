# Quote Scrapper
 ### A web scraping project. To scrap quote from http://quotes.toscrape.com/.
#
For this project we need to install **Scrapy**, a web scraping framework written in python.

##### Note: *To go through this project, you need to know the basics of python as well as command line/terminal, and have installed python in your system.*

*To install Scrapy:*
```
pip install scrapy
```
#### Typically any Scrapy command looks like this:
```
scrapy <command> [options] [args]
```
#
### Creating a Brand New Scrapy Project

Now, we need to create a Scrapy project.
The command is:  `scrapy startproject 'projectName'`

*Let's do ours:*
```
scrapy startproject niceQuotes
```

### Now Create a scrapy Spider

Navigate to craigslist folder using `cd niceQuotes`

Now we need to create a spider named 'jobs', using `genspider` command followed by a name and a URL.
```
scrapy genspider getQuote http://quotes.toscrape.com/
```
**Warning:** Remember to delete extra (if exits) `http://` in `start_urls` in `getQuote` within `spiders` folder. Otherwise the spider will not work.

Now we have a basic spider.
Run this using:
```
scrapy crawl niceQuotes
```

Or, save result in a csv file:
```
scrapy crawl niceQuotes -o quotes-one-page.csv
```
