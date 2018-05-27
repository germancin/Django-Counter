from django.http import HttpResponse
from django.shortcuts import render
import operator

def home(request):
    return render(request, 'home.html')

def count(request):
    fullText = request.GET['fulltext']
    wordlist = fullText.split()
    wordCount = len(wordlist)
    wordsDic = {}

    for w in wordlist:
        if w in wordsDic:
            # increment one
            wordsDic[w] += 1
        else:
            # add word to the diccionary
            wordsDic[w]  =  1

    sortedWords = sorted(wordsDic.items(), key=operator.itemgetter(1), reverse=True)

    return render(request, 'count.html',{
            'fulltext':fullText,
            'wordcount': wordCount,
            'sortedWords': sortedWords,
        })