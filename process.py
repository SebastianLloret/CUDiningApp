import os
import json
import textract

def c4c(finalDictionary):
    for file in os.listdir('./PDFs'):
        if file.endswith('.pdf') and 'C4C' in file:
            with open('./PDFs/' + file):
                finalDictionary['c4cRawTextList'][file] = textract.process('./PDFs/' + file)

def sewall(finalDictionary):
    for file in os.listdir('./PDFs'):
        if file.endswith('.pdf') and 'Sewall' in file:
            with open('./PDFs/' + file):
                finalDictionary['sewallRawTextList'][file] = textract.process('./PDFs/' + file)

def ve(finalDictionary):
    for file in os.listdir('./PDFs'):
        if file.endswith('.pdf') and 'VE' in file:
            with open('./PDFs/' + file):
                finalDictionary['veRawTextList'][file] = textract.process('./PDFs/' + file)


if __name__ == '__main__':
    finalDictionary = {
        'c4cRawTextList':{},
        'sewallRawTextList':{},
        'veRawTextList':{},
        'c4cBreakfastProcessed':{},
        'c4cLunchProcessed':{},
        'sewallBreakfastProcessed':{},
        'sewallLunchProcessed':{},
        'veBreakfastProcessed':{},
        'veLunchProcessed':{}
    }

    c4c(finalDictionary)
