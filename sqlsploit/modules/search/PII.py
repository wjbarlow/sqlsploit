__author__ = 'will@threadtheweb.co.uk'
from sqlsploit.cli import *
from sqlsploit.dbconnector import *

# Search Implementation - PII (Personally Identifiable Information
# Import modules
import click
import PyMySQL

# National Insurance - UK

# Social Security Number US
# ^(\d{3}-?\d{2}-?\d{4}|XXX-XX-XXXX)$

# Passport Numbers - UK
# ^[0-9]{10}GBR[0-9]{7}[U,M,F]{1}[0-9]{9}$

# Driving Licence
# ^(?!BG)(?!GB)(?!NK)(?!KN)(?!TN)(?!NT)(?!ZZ)(?:[A-CEGHJ-PR-TW-Z][A-CEGHJ-NPR-TW-Z])(?:\s*\d\s*){6}([A-D]|\s)$
# ^([A-Z]{2}[9]{3}|[A-Z]{3}[9]{2}|[A-Z]{4}[9]{1}|[A-Z]{5})[0-9]{6}([A-Z]{1}[9]{1}|[A-Z]{2})[A-Z0,9]{3}$

# Postcode - UK

# Date of Birth

# Email

# Telephone

# IP Address



#