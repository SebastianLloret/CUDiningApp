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
                rawText = rawText.replace(': ', ': \n')
                rawText = rawText.rstrip()
                rawText = rawText.replace('\n\n', '\n')
                dictionary[subdict][file] = re.split(',|\n', rawText)
                print dictionary[subdict][file]

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
    days = ['Daily: ', 'Monday: ', 'Tuesday: ', 'Wednesday: ', 'Thursday: ', 'Friday: ', 'Saturday: ', 'Sunday: ', 'Saturday & Sunday: ']
    meals = ['BREAKFAST']

    rawImport(rawDictionary, 'c4cBreakfast')
