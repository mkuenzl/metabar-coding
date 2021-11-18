#! /usr/bin/python
import re
import urllib.request

taxonID = input("Please enter a Taxon Id: ")
# print(taxonID)

# Open url and access html code
url = urllib.request.urlopen("http://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=" + taxonID).read()
url = str(url, 'utf-8')
# print(url)

# Search html for patterns of taxonomy
sciName = re.search(r"(?<=Taxonomy browser )\(\w+ \w+\)", url)
if sciName:
    print('Taxonomy browser: ', sciName.group())
else:
    print('Taxonomy browser: No match')

kingdom = re.search(r'(?<="kingdom">)\w+', url)
if kingdom:
    print('Kingdom: ', kingdom.group())
else:
    print('Kingdom: No match')

phylum = re.search(r'(?<="phylum">)\w+', url)
if phylum:
    print('Phylum: ', phylum.group())
else:
    print('Phylum: No match')

superclass = re.search(r'(?<="superclass">)\w+', url)
if superclass:
    print('Superclass: ', superclass.group())
else:
    print('Superclass: No match')

sciClass = re.search(r'(?<="class">)\w+', url)
if sciClass:
    print('Class: ', sciClass.group())
else:
    print('Class: No match')

subClass = re.search(r'(?<="subclass">)\w+', url)
if subClass:
    print('Subclass: ', subClass.group())
else:
    print('Subclass: No match')

order = re.search(r'(?<="order">)\w+', url)
if order:
    print('Order: ', order.group())
else:
    print('Order: No match')

superFamily = re.search(r'(?<="superfamily">)\w+', url)
if superFamily:
    print('SuperFamily: ', superFamily.group())
else:
    print('SuperFamily: No match')

family = re.search(r'(?<="family">)\w+', url)
if family:
    print('Family: ', family.group())
else:
    print('Family: No match')

genus = re.search(r'(?<="genus">)\w+', url)
if genus:
    print('Genus: ', genus.group())
else:
    print('Genus: No match')
