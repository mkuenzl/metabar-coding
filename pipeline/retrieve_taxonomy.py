#! /usr/bin/python
import re
import urllib.request

query_file = 'otu/query.txt'

# taxonID = input("Please enter a Taxon Id: ")
# print(taxonID)
with open(query_file, 'r') as query:
    print('Otu\tTaxId\tTaxonomy\tKingdom\tPhylum\tSuperclass\tClass\tSubclass\tOrder\tSuperFamily\tFamily\tGenus')

    for line in query:
        splitter = line.split('\t')
        taxonID = splitter[0]
        otu = splitter[1]
        print(otu, end='\t')
        print(taxonID, end='\t')

        # Open url and access html code
        url = urllib.request.urlopen("http://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=" + taxonID).read()
        url = str(url, 'utf-8')
        # print(url)
        # Search html for patterns of taxonomy
        sciName = re.search(r"(?<=Taxonomy browser )\(\w+ \w+\)", url)
        if sciName:
            print(sciName.group(), end='\t')
            # print('Taxonomy browser: ', sciName.group(), end='\t')
        else:
            print('-', end='\t')
            # print('Taxonomy browser: No match')

        kingdom = re.search(r'(?<="kingdom">)\w+', url)
        if kingdom:
            print(kingdom.group(), end='\t')
            # print('Kingdom: ', kingdom.group())
        else:
            print('-', end='\t')
            # print('Kingdom: No match')

        phylum = re.search(r'(?<="phylum">)\w+', url)
        if phylum:
            print(phylum.group(), end='\t')
            # print('Phylum: ', phylum.group())
        else:
            print('-', end='\t')
            # print('Phylum: No match')

        superclass = re.search(r'(?<="superclass">)\w+', url)
        if superclass:
            print(superclass.group(), end='\t')
            # print('Superclass: ', superclass.group())
        else:
            print('-', end='\t')
            # print('Superclass: No match')

        sciClass = re.search(r'(?<="class">)\w+', url)
        if sciClass:
            print(sciClass.group(), end='\t')
            # print('Class: ', sciClass.group())
        else:
            print('-', end='\t')
            # print('Class: No match')

        subClass = re.search(r'(?<="subclass">)\w+', url)
        if subClass:
            print(subClass.group(), end='\t')
            # print('Subclass: ', subClass.group())
        else:
            print('-', end='\t')
            # print('Subclass: No match')

        order = re.search(r'(?<="order">)\w+', url)
        if order:
            print(order.group(), end='\t')
            # print('Order: ', order.group())
        else:
            print('-', end='\t')
            # print('Order: No match')

        superFamily = re.search(r'(?<="superfamily">)\w+', url)
        if superFamily:
            print(superFamily.group(), end='\t')
            # print('SuperFamily: ', superFamily.group())
        else:
            print('-', end='\t')
            # print('SuperFamily: No match')

        family = re.search(r'(?<="family">)\w+', url)
        if family:
            print(family.group(), end='\t')
            # print('Family: ', family.group())
        else:
            print('-', end='\t')
            # print('Family: No match')

        genus = re.search(r'(?<="genus">)\w+', url)
        if genus:
            print(genus.group(), end='\t')
            # print('Genus: ', genus.group())
        else:
            print('-', end='\t')
            # print('Genus: No match')
        print()
