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




