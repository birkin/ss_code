"""
Checking out <https://www.digitalocean.com/community/tutorials/how-to-scrape-web-pages-with-beautiful-soup-and-python-3>

To set all this up (one time only!):
- create a directory named something like `screen_scraping_stuff`
- copy this `ss_code` directory into the `screen_scraping_stuff` directory
- cd into the `ss_code` directory
- create the virtual-environment: `/path/to/python3 -m venv ../env_ss`
- source the environment: `source ../env_ss/bin/activate`
- upgrade the package-installer: `pip install pip --upgrade`
- install the two required libraries: `pip install -r ./requirements.txt`

To run:
- cd into the `ss_code` directory
- source the environment: `source ../env_ss/bin/activate`
- run this file: `python3 ./grabber.py`
"""

import requests
from bs4 import BeautifulSoup


## Collect first page of artists’ list
url = 'https://web.archive.org/web/20121007172955/https://www.nga.gov/collection/anZ1.htm'
page = requests.get( url )


## Create a BeautifulSoup object
soup = BeautifulSoup( page.text, 'html.parser' )


## Pull all text from the BodyText div
artist_name_list = soup.find( class_='BodyText' )


## Pull text from all instances of <a> tag within BodyText div
artist_name_list_items = artist_name_list.find_all( 'a' )


## Create for loop to print out all artists' names
for artist_name in artist_name_list_items:
    # print( artist_name.prettify() )
    names = artist_name.contents[0]
    print( names )
