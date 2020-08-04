# ###### Beautiful Soup Libary ######

# =================================
# What does scraping websites means?
#   Scraping websites means parsing the content from a website and pulling out exactly the information that we want
# ---------------------------------
# Problems with using our own Python code for web scraping
#   If we want to parse out information from website with something(some program) we built in python then we will run into alot of issues
# =================================
# ### Parsers ###

# There are some small differences between the parsers and they could return different results depending on the HTML that we are trying to parse 
# If we are trying to parse perfectly formed HTML then those differences aren't going to matter
# But if there are mistakes in HTML then the different parsers will try to fillin missing information differently 
# =================================
# BeautifulSoup Libary Documentation on Parsers

# ---------------------------------
# Differences between parsers
# Beautiful Soup presents the same interface to a number of different parsers, but each parser is different. 
# Different parsers will create different parse trees from the same document. 
# The biggest differences are between the HTML parsers and the XML parsers. 
# ---------------------------------
# Here’s a short document, parsed as HTML:

# BeautifulSoup("<a><b /></a>")
# # <html><head></head><body><a><b></b></a></body></html>
# Since an empty <b /> tag is not valid HTML, the parser turns it into a <b></b> tag pair.
# ---------------------------------
# Here’s the same document parsed as XML (running this requires that you have lxml installed). Note that the empty <b /> tag is left alone, and that the document is given an XML declaration instead of being put into an <html> tag.:

# BeautifulSoup("<a><b /></a>", "xml")
# # <?xml version="1.0" encoding="utf-8"?>
# # <a><b/></a>
# There are also differences between HTML parsers. 
# If you give Beautiful Soup a perfectly-formed HTML document, these differences won’t matter. 
# One parser will be faster than another, but they’ll all give you a data structure that looks exactly like the original HTML document.
# ---------------------------------
# But if the document is not perfectly-formed, different parsers will give different results. 
# ---------------------------------
# Here’s a short, invalid document parsed using lxml’s HTML parser. Note that the dangling </p> tag is simply ignored:

# BeautifulSoup("<a></p>", "lxml")
# # <html><body><a></a></body></html>
# ---------------------------------
# Here’s the same document parsed using html5lib:

# BeautifulSoup("<a></p>", "html5lib")
# # <html><head></head><body><a><p></p></a></body></html>
# Instead of ignoring the dangling </p> tag, html5lib pairs it with an opening <p> tag. This parser also adds an empty <head> tag to the document.
# ---------------------------------
# Here’s the same document parsed with Python’s built-in HTML parser:

# BeautifulSoup("<a></p>", "html.parser")
# # <a></a>
# Like html5lib, this parser ignores the closing </p> tag. 
# Unlike html5lib, this parser makes no attempt to create a well-formed HTML document by adding a <body> tag. 
# Unlike lxml, it doesn’t even bother to add an <html> tag.
# ---------------------------------
# Since the document “<a></p>” is invalid, none of these techniques is the “correct” way to handle it. The html5lib parser uses techniques that are part of the HTML5 standard, so it has the best claim on being the “correct” way, but all three techniques are legitimate.
# ---------------------------------
# Differences between parsers can affect your script. If you’re planning on distributing your script to other people, or running it on multiple machines, you should specify a parser in the BeautifulSoup constructor. That will reduce the chances that your users parse a document differently from the way you parse it.
# =================================
# Here lxml is used but html5lib is also popular parser
# =================================
# Importing important modules
from bs4 import BeautifulSoup
import lxml.html
import requests

# We are using the lxml parser

# We can pass HTML in BeautifulSoup method so that we can get BeautifulSoup object
# There are two ways to do that:
#   1. We can pass the HTML as string 
#   2. We can also pass the HTML File
# =================================
# ### BeautifulSoup() ###

with open('simple.html') as html_file:
  soup = BeautifulSoup(html_file, 'lxml')

print(soup)
# This html is not formatted
# =================================
# ### prettify() ###

# To format use prettify() method
print(soup.prettify())
# =================================
# Easiest way to get information from a tag is to access it like an attribute

# ---------------------------------
# To get the title

match = soup.title
print(match)
# ---------------------------------
# To just get text use the text attribute

match = soup.title.text
print(match)
# =================================
# ### find() ###

# ---------------------------------
# This way will give us only the first tag in the page of which attribute we have passed

match = soup.div
print(match)
# ---------------------------------
# We can use find method to do something similar but also can pass some argument

match = soup.find('div')
print(match)
# This will give the same result since extra argument is passed
# ---------------------------------
match = soup.find('div', class_='footer')
print(match)

# Most of the time we can pass the attribute as they are like id='' and others
# But reason we need _ after class is that class is a special keyword in Python

article = soup.find('div', class_='article')
print(article)
# ---------------------------------
# Now to get headline inside the article we don't need entire soup we can work with article variable itself

headline = article.h2.a.text
print(headline)

summary = article.p.text
print(summary)
# =================================
# ### find_all() ###

# Till now we have got headline and summary for first div tag with class article

# To get all headline and summary with div tag and class article
# So instead of using find method we will use find_all method

for article in soup.find_all('div', class_='article'):
  headline = article.h2.a.text
  print(headline)

  summary = article.p.text
  print(summary)
# =================================
# ### To get information from a real website ###

# ---------------------------------
source = requests.get('https://coreyms.com').text
# This requests.get() will return a response object and to get the source code from that response object we add on .text 
# ---------------------------------
soup = BeautifulSoup(source, 'lxml')
print(soup.prettify())
# =================================
# ### Performing different operations ###

# ---------------------------------
article = soup.find('article')
print(article.prettify())
# ---------------------------------
headline = article.h2.a.text
print(headline)
# ---------------------------------
summary = article.find('div', class_='entry-content').p.text
print(summary)
# ---------------------------------
vid_src = article.find('iframe', class_='youtube-player')
print(vid_src)
# =================================
# ### To get specific element we have to find it as we do in Python Dictonary ###

# ---------------------------------
vid_src = article.find('iframe', class_='youtube-player')['src']
print(vid_src)
# ---------------------------------
vid_id = vid_src.split('/')
print(vid_id)
# ---------------------------------
vid_id = vid_src.split('/')[4]
print(vid_id)
# ---------------------------------
vid_id = vid_id.split('?')[0]
# Here we get the youtube video id
print(vid_id)

# Some times getting what you want from webstie through scraping can get messy as in above case

yt_link = f'https://youtube.com/watch?v={vid_id}'
print(yt_link)
# =================================
# ### To loop thorgh all articles ###

for article in soup.find_all('article'):
  headline = article.h2.a.text
  print(headline)

  summary = article.find('div', class_='entry-content').p.text
  print(summary)

  vid_src = article.find('iframe', class_='youtube-player')['src']

  vid_id = vid_src.split('/')[4]
  vid_id = vid_id.split('?')[0]

  yt_link = f'https://youtube.com/watch?v={vid_id}'
  print(yt_link)
# =================================
# ### Some times we can run into situations where we are missing some data and if that happens it will break our scraper ###

# For this we have to use try-except statements

for article in soup.find_all('article'):
  headline = article.h2.a.text
  print(headline)

  summary = article.find('div', class_='entry-content').p.text
  print(summary)

  try:
    vid_src = article.find('iframe', class_='youtube-player')['src']

    vid_id = vid_src.split('/')[4]
    vid_id = vid_id.split('?')[0]

    yt_link = f'https://youtube.com/watch?v={vid_id}'
  except:
    yt_link = None
  
  print(yt_link)
# =================================
# ### Since we have scraped the website now we can save it any way ###

# Like saving data in csv file

# Importing csv module
import csv

# Opening the file
csv_file = open('scraped_data.csv', 'w')

# Writing to the file
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['headline', 'summary', 'video_link'])
# Inside list there is detail that we are saving

for article in soup.find_all('article'):
  headline = article.h2.a.text
  print(headline)

  summary = article.find('div', class_='entry-content').p.text
  print(summary)

  try:
    vid_src = article.find('iframe', class_='youtube-player')['src']

    vid_id = vid_src.split('/')[4]
    vid_id = vid_id.split('?')[0]

    yt_link = f'https://youtube.com/watch?v={vid_id}'
  except:
    yt_link = None
  
  print(yt_link)

  # Writing data to csv file with each iteration
  csv_writer.writerow([headline, summary, yt_link])

# Closing the file
csv_file.close() 
# =================================
# If we want data from large website such as twitter, facebook, youtube or something like that then it maybe benifical that to see that they have public api or not. Public api's allows their sites to serve up their data in more sufficient way and some times they don't appreciate if you try to scrape their data manually, they rather want us to use public api's

# We should be carefull while scraping websites. So computer programs allows us to send a lot of request very quickly so beaware that you might be bogging down someone's sever if we weren't careful
