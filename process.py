import os
import json
import textract

def c4cBreakfast(dictionary):
    for file in os.listdir('./PDFs'):
        if file.endswith('.pdf') and 'C4C' and 'Breakfast' in file:
            with open('./PDFs/' + file):
                rawText = textract.process('./PDFs/' + file)
                rawText = rawText.replace('BREAKFAST', 'BREAKFAST\n')
                rawText = rawText.replace('* denotes vegan\n', '')
                dictionary[file] = rawText

def c4c(dictionary):
    for file in os.listdir('./PDFs'):
        if file.endswith('.pdf') and 'C4C' and not 'Breakfast' in file:
            with open('./PDFs/' + file):
                rawText = textract.process('./PDFs/' + file)
                rawText = rawText.replace('* denotes vegan\n', '')
                rawText = rawText.replace('LUNCH & DINNER MENU\n', '')
                rawText = rawText.replace('LUNCH MENU\n', '')
                rawText = rawText.replace('DAILY', '\nDAILY')
                rawText = rawText.replace('SUSHI', 'DAILY\n')
                rawText = rawText.replace('DAILY FEATURES', '\nDAILY FEATURES')
                rawText = rawText.replace('On occasion: Monday-Thursday check out the Chef\'s Showcase', '')
                rawText = rawText.replace('Closed all day on Fridays, Saturdays and on Jewish holidays', '')
                rawText = rawText.replace('Closed for Dinner', '')
                rawText = rawText.replace('Closed all Day on Saturday & Sunday', '')
                rawText = rawText.replace('Menu is subject to change', '')
                dictionary[file] = rawText

def sewall(dictionary):
    for file in os.listdir('./PDFs'):
        if file.endswith('.pdf') and 'Sewall' in file:
            with open('./PDFs/' + file):
                dictionary[file] = textract.process('./PDFs/' + file)

def ve(dictionary):
    for file in os.listdir('./PDFs'):
        if file.endswith('.pdf') and 'VE' in file:
            with open('./PDFs/' + file):
                dictionary[file] = textract.process('./PDFs/' + file)

def firstPass(rawDictionary, key):
    for text in rawDictionary[key]:
        rawDictionary[key][text] = rawDictionary[key][text].split('\n\n')
        print rawDictionary[key][text]


if __name__ == '__main__':
    rawDictionary = {
        'c4cRawTextList':{},
        'c4cRawBreakfastTextList':{},
        'sewallRawTextList':{},
        'veRawTextList':{},
    }

    c4cBreakfast(rawDictionary['c4cRawBreakfastTextList'])
    firstPass(rawDictionary, 'c4cRawBreakfastTextList')

    c4c(rawDictionary['c4cRawTextList'])
    firstPass(rawDictionary, 'c4cRawTextList')
