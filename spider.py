#!/usr/bin/env python3

import requests # allows to send requests over http
import re # regex
import urlparse

target_url = "https://google.com"
target_links = []	

def extract_links(url):
	response = requests.get(target_url)
	return re.findall('(?:href=")(.*?)"', response.content) # find all links in html source code using regex syntax

def crawl(url):
	href_links = extract_links(url)
	for link in href_links:
		link = urlparse.urljoin(url, link) # converts relative or isolated links to full links
		if '#' in link:
			link = link.split("#")[0] # separate link and hash link
		if target_url in link and link not in target_links: # only display unique links related to target url
			target_links.append(link)
			print(link)
			crawl(link) # recursively extract further links in a particular link
crawl(target_url)
