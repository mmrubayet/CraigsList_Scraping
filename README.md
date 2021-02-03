# **craigsList_scraping**
 ### A web scraping project. Scraps data from Craigslist website.
#
For this project we need to install **Scrapy**, a web scraping framework written in python.

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
scrapy startproject craigslist
```

### Now Create a scrapy Spider

Navigate to craigslist folder using `cd craigsList`

Now we need to create a spider named 'jobs', using `genspider` command followed by a name and a URL.
```
scrapy genspider jobs https://newyork.craigslist.org/search/egr
```
