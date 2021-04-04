This will go over the following with Python3.

0. [What is webscraping and how can we do it?](What is webscraping and how can we do it?)
    * [Some problems and solutions](Some problems and solutions)
1. [Downloading web pages](Downloading web pages)
    * [Modifying the User-Agent](Modifying the User-Agent)
2. [Parsing data with Beautiful Soup](Parsing data with Beautiful Soup)
3. [Parsing data with Scrapy](Parsing data with Scrapy)
4. Exercises:
    * Parse a simple title from any website
    * Parse a paragraph from a Wikipedia article
    * Parse a table from a website or a Wikipedia article
    * Parse forum posts from a forum
    * Head to https://webscraping.us/blog/ and try to see how far you can get using Scrapy


# What is webscraping and how can we do it?

Webscraping is the act of automatically downloading a single or more web pages and parsing data, instead of doing it manually, since some data may be hidden, or mass amount of data exist that need harvesting, such as tables and forum posts.

## Some problems and solutions

### Problems

1. Websites may limit browser-ability via blocking known bot User-Agents in the robots.txt file
2. Mass requests might result to a ban, so download the html file and practice on them
3. JavaScript might hide some data
4. Regex may be limiting if you are just using it by itself.

### Solutions

1. Use a simple regex solution to grab simple things, like titles and other easy-to-find things on the page
* Unless you are very good at regex, you can use it to do anything.
2. Use Beautiful Soup to parse HTML
3. Use Selenium to act as a browser and download data hidden with JavaScript
4. Use Scrapey to overall, do mass data extraction.
5. If a website offers API, USE IT! Makes it easier.


# Downloading web pages

We will be using requests in this workshop to download pages. A simple GET request will do the trick. Though, make sure you have it installed.
`pip install requests`
```python
import requests

URL = "https://www.linuxquestions.org/questions/slackware-14/what%27s-your-favorite-sql-editor-842171/"

data = requests.get(URL).text
```

This will download the page in memory and display it as text.

Make sure you save this as a file on your machine to avoid the delay in testing (over requesting.)

## Modifying the User-Agent

In order to mimic a real browser, you can modify the user agent in requests. This is the line that you need to have:
```python
import requests

URL = "https://www.linuxquestions.org/questions/slackware-14/what%27s-your-favorite-sql-editor-842171/"

headers = {
    "User-Agent": "Mozilla/5.0 (Android 4.4; Tablet; rv:41.0) Gecko/41.0 Firefox/41.0"
}

data = requests.get(URL, headers=headers).text
```

This will use the Firefox User Agent, but you can find some more when you look around the net, or use your own.


# Parsing data with Beautiful Soup

First, if you do not have it, install it `pip install BeautifulSoup4`

Please read the file in the data folder for the example. In addition, here is the link to the BeautifulSoup Documentation: https://www.crummy.com/software/BeautifulSoup/bs4/doc/

# Parsing data with Scrapy

Scrapy is not just a library, but a full-featured software on its own, that you can script out. You need to download it and then create a project in order to start with.

```bash
pip install scrapy
scrapy startproject matahacks
```

To keep things simple, navigate to the matahacks folder that was just created, and there will be another one inside of it. Then open the "spiders" folder: `matahacks/matahacks/spiders`

Create a python file to initiate your Spider, and fill it with the following:

```python
import scrapy

class MataSpider(scrapy.Spider):
    name = "mataspider"
    allowed_domains = ["wikipedia.org"]
    start_urls = [
        "https://en.wikipedia.org/wiki/Instant_messaging"
    ]

    def parse(self, response):
        data = {}
        data['title'] = response.css('title::text').extract()
        yield data
```

Get back to your console and run the following command:
```bash
scrapy crawl mataspider
```

You can also, get in the shell, this is to avoid coding a lot, and just debugging:

```bash
scrapy shell https://en.wikipedia.org/wiki/Instant_messaging
```

Some syntax you can use:
### To find divs with classes/IDs
```
response.xpath('//div[@id="place-id-here"]/p/text()').extract()
```
The above will extract all "text" from the paragraph tag inside of the div with the ID "place-id-here"

Alternatively, you can use the following:

```
response.css(r"p::text").extract()
```

Which will do the same, but the syntax is a bit different.


To grab URLs from a table row:
```python
response.css(r"tr[style='IDENTIFIER'] a[href*='IDENTIFIER']::attr(href)").extract()
```

The IDENTIFIERs are keywords that you can use to find specific rows (background color, font type, size etc.)
The href is what you want to look for, so, if a text has a link, it has an "href". The IDENTIFIER for this, is if a URL has some specific keywords, you can get specific types of URLs.
The ::attr(href) indicates that you want to get the links, similar to ::text


To look for words inside of a paragraph (and grab it) we can use :contains("WORD")
```
response.css(r"p:contains('INDICATOR')")
```

In addition, you can also make web requests with Scrapy:
```python
scrapy.Request(URL, callback=self.other_function)
```
This will request a URL (via a link found from the webpage, to keep digging in) and send it to a function called other_function.

```python
def other_function(self, response):
```
This way, you can parse several things, instead of just one. Though, you can yield your data at this stage, if you are planning on just going one level deep.


https://docs.scrapy.org/en/latest/intro/tutorial.html
https://docs.scrapy.org/en/latest/topics/practices.html
https://docs.scrapy.org/en/latest/topics/request-response.html

Using the links above, you can read the documentation to help you with the exercises.
