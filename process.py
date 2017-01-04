# -*- coding: utf-8 -*-
# Commit to test ssh
import os
import json
import textract
import re

def rawImport():
    for pdf in os.listdir('./PDFs'):
        if pdf.endswith('.pdf'):
            with open('./PDFs/' + pdf):
                rawText = textract.process('./PDFs/' + pdf)
                rawText = rawText.replace('\xc3\xa2\xe2\x82\xac\xe2\x84\xa2', '\'')
                rawText = rawText.replace('\xe2\x80\x99', '\'')
                rawText = rawText.replace('\x0c', '')
                rawText = rawText.replace('‘', '')
                rawText = rawText.replace('* denotes vegan', '')
                rawText = rawText.replace('LUNCH & DINNER MENU', '')
                rawText = rawText.replace(':\n', '\n')
                rawText = rawText.replace('\n\n', '\n')
                rawText = re.sub('(,[^\r\n]*?)[\r\n](?=[^\r\n]+?,)', r'\1 ', rawText, re.MULTILINE)
                rawText = rawText.rstrip()

                if 'C4C_Breakfast' in pdf:
                    rawDictionary['c4cBreakfast'][pdf] = rawText
                    rawDictionary['c4cBreakfast'][pdf] = rawDictionary['c4cBreakfast'][pdf].split('\n')

                if 'C4C' in pdf and 'Breakfast' not in pdf:
                    rawDictionary['c4c'][pdf] = rawText
                    rawDictionary['c4c'][pdf] = rawDictionary['c4c'][pdf].split('\n')

                if 'Sewall' in pdf:
                    rawDictionary['sewall'][pdf] = rawText
                    rawDictionary['sewall'][pdf] = rawDictionary['sewall'][pdf].split('\n')

                if 'VE' in pdf:
                    rawDictionary['ve'][pdf] = rawText
                    rawDictionary['ve'][pdf] = rawDictionary['ve'][pdf].split('\n')

def createDictionary():
    for pdf in rawDictionary['c4c']:
        c4cDict[pdf] = {}
        for station in c4cstations:
            c4cDict[pdf][station] = {}

def processC4C():
    for pdf in rawDictionary['c4c']:
        listQuery = rawDictionary['c4c'][pdf]
        listQuery = filter(None, listQuery)

        for i in xrange(0, len(c4cstations)):
            station = c4cstations[i]
            if i < len(c4cstations) - 1:
                c4cDict[pdf][station] = listQuery[listQuery.index(c4cstations[i]) + 1:listQuery.index(c4cstations[i+1])]
            else:
                c4cDict[pdf][station] = listQuery[listQuery.index(c4cstations[i]) + 1:]



if __name__ == '__main__':
    rawDictionary = {
        'c4c':{},
        'c4cBreakfast':{},
        'sewall':{},
        've':{},
    }

    c4cBreakfastDict = {}
    c4cDict = {}
    sewallDict = {}
    veDict = {}

    c4cbreakfaststations = ['BLACK COATS', 'ITALY', 'WHOLESOME FIELDS', 'ASIA', 'LATIN', 'DESSERT']
    c4cstations = ['ASIAN SHI PIN', 'ITALIAN CIBO', 'LATIN COMIDA', 'PERSIAN GHAZA', 'SMOKE N GRILL', 'SUSHI', 'WHOLESOME FIELDS', 'KOSHER', 'BLACK COATS', 'DESSERTS']
    days = ['DAILY', 'MONDAY', 'TUESDAY', 'WEDNESDAY', 'THURSDAY', 'FRIDAY', 'SATURDAY', 'SUNDAY', 'SATURDAY & SUNDAY', 'EVERY FRIDAY', 'DAILY FEATURES']

    rawImport()
    createDictionary()
    processC4C()
