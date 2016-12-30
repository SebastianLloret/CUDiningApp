import os
import json
import textract
import re

def rawImport(dictionary, subdict):
    for file in os.listdir('./PDFs'):
        if file.endswith('.pdf') and 'C4C' and 'Breakfast' in file:
            with open('./PDFs/' + file):
                rawText = textract.process('./PDFs/' + file)
                rawText = rawText.replace('\xc3\xa2\xe2\x82\xac\xe2\x84\xa2', '\'')
                rawText = rawText.replace('* denotes vegan', '')
                rawText = rawText.replace(': ', ':\n')
                rawText = rawText.replace('\n\n', '\n')
                rawText = rawText.rstrip()
                rawText = re.sub('(,[^\r\n]*?)[\r\n](?=[^\r\n]+?,)', r'\1 ', rawText, re.MULTILINE)
                dictionary[subdict][file] = rawText
                dictionary[subdict][file] = dictionary[subdict][file].split('\n')

def processc4cBreakfast():
    for pdf in rawDictionary['c4cBreakfast']:
        lst = rawDictionary['c4cBreakfast'][pdf]
        for i in xrange(0, len(c4cstations)):
            name = c4cstations[i].replace(' ', '')
            name = name.lower()
            if i < len(c4cstations) - 1:
                c4cBreakfastDictionary[name][pdf] = lst[lst.index(c4cstations[i]) + 1:lst.index(c4cstations[i+1])]
            else:
                c4cBreakfastDictionary[name][pdf] = lst[lst.index(c4cstations[i]) + 1:]
        print c4cBreakfastDictionary

if __name__ == '__main__':
    rawDictionary = {
        'c4c':{},
        'c4cBreakfast':{},
        'sewall':{},
        've':{},
    }

    c4cBreakfastDictionary = {
        'blackcoats':{},
        'italy':{},
        'wholesomefields':{},
        'asia':{},
        'latin':{},
        'dessert':{},
    }

    c4cstations = ['BLACK COATS', 'ITALY', 'WHOLESOME FIELDS', 'ASIA', 'LATIN', 'DESSERT']
    days = ['Daily:', 'Monday:', 'Tuesday:', 'Wednesday:', 'Thursday:', 'Friday:', 'Saturday:', 'Sunday:', 'Saturday & Sunday:']
    meals = ['BREAKFAST']

    rawImport(rawDictionary, 'c4cBreakfast')
    processc4cBreakfast()
