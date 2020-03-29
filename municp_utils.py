#!/usr/bin/env python
  
"""
@package css
@file css/municp_utils.py
@author K Sree Harsha
@brief Utility module for retrieving congress.gov data.
"""


from mechanize import Browser
from bs4 import BeautifulSoup
import re
import urllib
import csv
import optparse

def download_municipality_by_page(first_page,last_page):
	for page_no in range(first_page,(last_page+1)):
		mech = Browser()
		url = "http://www.nscb.gov.ph/activestats/psgc/listmun.asp?whichpage=%i"%(page_no)
		print url
		page = mech.open(url)

		count=0
		NO_TRIES=10
		pattern1='municipality.asp'
		expr1 = re.compile(pattern1)
		MunicipalityList=[]
		while True:
			try:
				html = page.read()
				soup = BeautifulSoup(html)
				tags1 = soup.findAll(href=expr1)
				tableMunicipality=soup.findAll("table",{'width':'550'})
                            	tries = 0
                            	break
			except IOError as ex:
				print 'ERROR: ' + str(ex)
				tries += 1
				if tries > NO_TRIES:
					raise
				time.sleep(SLEEP_TIME)


if __name__=='__main__':

         # Parse command line arguments and options.
    usage = 'usage: %prog [options]'
    description = 'Download municipality records.'
    p = optparse.OptionParser(usage=usage, description=description)
    p.add_option('-f','--first_page', action='store', dest='first_page',
                 type='int',help='First Page to download')
    p.add_option('-l','--last_page', action='store', dest='last_page',
                 type='int', help='Last Page to download')
    p.set_defaults(first_page=1, last_page=1)

    (opts, args) = p.parse_args()
    first_page=opts.first_page
    last_page=opts.last_page

    print "Downloading pages from ",first_page," to ",last_page

    download_municipality_by_page(first_page,last_page)
