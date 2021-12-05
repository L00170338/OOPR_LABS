
##################################################
## Q2 - Assessment Webscrapper Apache Server.
##################################################
## Author: Wagner Ribeiro (L00170338).
## Email: L00170338@student.lyit.ie
## Status: Development.
##################################################
import requests
import sys
from bs4 import BeautifulSoup
import re
from collections import Counter

# Function defined to execute a http and get the page content on the URL especified.
def get_webpage(ip):
    url = 'http://{}'.format(ip)
    req = requests.get(url)
    return req

# Function created to get the Website headings.
def get_tittle(data):
    print ("\n1. Getting the Website headinds of Apache page")
    soup = BeautifulSoup(data.text, 'html.parser')
    for title in soup.find_all('title'):
        title_reponse = title.get_text()
        print('Title of the website is : {}'.format(title_reponse))
# Function created to get the Website headings.

def count_word(data):
    print ("\n2. Searching words on the website and counting the number of ocurrences in the page.")
    data_content = data.text
    words = ['Apache2', 'apache2', 'ubuntu','bugs', 'Debian']
    for i in words:
        word = i
        total_words=data_content.count(i)
        print('{} appears on the website {} times'.format(word, total_words ))

# Function created to get header classes and print the content of the headers.
def get_page_code(data):
    print ("\n3. Getting especific class ID from the section header of the page and printing the content.")
    soup = BeautifulSoup(data.text,'html.parser' )
    divs=soup.find_all('div',{'class':'section_header'})
    for i in divs:
        div_header_content = i.contents[2].strip()
        print (div_header_content)

def main():
    if len(sys.argv) < 2:
	    print ("You must pass the IP you want to scrape.")
    else:
        target = sys.argv[1] 
        request_data = get_webpage(target)
        get_tittle(request_data)
        count_word(request_data)
        get_page_code(request_data)
if __name__ == '__main__':
	main()


