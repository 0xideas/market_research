#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Written as part of https://www.scrapehero.com/how-to-scrape-amazon-product-reviews-using-python/		
from lxml import html  
import json
import requests
import json,re
from dateutil import parser as dateparser
from time import sleep

def ParseReviews_Raw(asin):
	# for i in range(5):
	# 	try:
	#This script has only been tested with Amazon.com
	amazon_url  = 'https://www.amazon.com/dp/'+asin
	# Add some recent user agent to prevent amazon from blocking the request 
	# Find some chrome user agent strings  here https://udger.com/resources/ua-list/browser-detail?browser=Chrome
	headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.90 Safari/537.36'}
	page = requests.get(amazon_url,headers = headers,verify=False)
	page_response = page.text


	parser = html.fromstring(page_response)

	#getting the all reviews page
	ALL_REVIEWS = './/a[@data-hook="see-all-reviews-link-foot"]/@href'
	all_reviews_link = parser.xpath(ALL_REVIEWS)[0]
	print(all_reviews_link)
	all_reviews_link = 'https://www.amazon.com' + all_reviews_link

	page = requests.get(all_reviews_link,headers = headers,verify=False)
	page_response = page.text
	parser = html.fromstring(page_response)

	return(page_response, parser)



for x in data[0]["reviews"]:
    if x["review_text"] not in new_review_texts:
        new_reviews.append(x)
        new_review_texts.append(x["review_text"])
