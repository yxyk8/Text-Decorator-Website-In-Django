# Created manually
from django.http import HttpResponse
from django.shortcuts import render
from django.core.mail import send_mail


def index(request):
    # var = "Alert!"
    # return HttpResponse("<title>Hi</title> <center><h1>Hi! This is a simple website for people who love simplicity</h1></center>")
    return render(request, 'index.html')


# def analyze(request):
#     return HttpResponse("<h1>Now this idiot came to the about page to show his faltu face</h1>")
def ex1(request):
    sites = ['''<h1>For Entertainment </h1><a href = "https://www.youtube.com" >youtube video</a>''',
             '''<h1>For Interaction </h1><a href = "https://www.facebook.com" >Facebook</a>''',
             '''<h1>For Insight   </h1><a href = "https://www.ted.com/talks" >Ted Talk</a>''',
             '''<h1>For Internship   </h1><a href="https://internshala.com" >Intenship</a>''',
             ]
    return HttpResponse((sites))


def analyze(request):
    djtext = request.POST.get('text', 'default')
    removepunc = request.POST.get('removepunc', 'of')
    allcaps = request.POST.get('allcaps', 'of')
    newlineremove = request.POST.get('lineremo', 'of')
    extraspaceremover = request.POST.get('exspre', 'of')
    print(djtext)
    # print(djtext)
    print(removepunc)
    if removepunc == "on":
        punctuations = '''!()-[]{};:'+\",<>./?@#$%^&*|=_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed+char
                params = {
                    'purpose': 'removepunc',
                    'analyzed_text': analyzed
                }
        djtext = analyzed
        # return render(request, 'analyze.html', params)

    if allcaps == "on":
        analyzed = ""
        for char in djtext:
            analyzed = analyzed+char.upper()

        params = {
            'purpose': 'changes lower case to upper case',
            'analyzed_text': analyzed
        }
        djtext = analyzed
        # return render(request, 'analyze.html', params)

    if newlineremove == "on":
        analyzed = ""
        for char in djtext:
            if char != "\n" and char != "\r":
                analyzed = analyzed + char

        params = {
            'purpose': 'removed new lines buddy',
            'analyzed_text': analyzed
        }
        djtext = analyzed
        # return render(request, 'analyze.html', params)

    if extraspaceremover == "on":
        analyzed = ""
        for index, char in enumerate(djtext):
            if djtext[index] == " " and djtext[index + 1] == " ":
                pass
            else:
                analyzed = analyzed+char

        params = {
            'purpose': 'removed extra white spaces buddy',
            'analyzed_text': analyzed
        }
        if removepunc == "of" and allcaps == "of" and extraspaceremover == "of" and newlineremove == "of":
            return HttpResponse("Error bhai! error alltime error")
            djtext = analyze
            # return render(request, 'analyze.html', params)
    # else:
    #     return HttpResponse("Please check the checkbox to get expected output")

    return render(request, 'analyze.html', params)

    send_mail(
        'This is the subject',
        'Hello mister human how are you',
        'sannidas38@gmail.com',
        ['shubhradasgupta8@gmail.com'],
        fail_silently=False,
    )
# return HttpResponse("remove punc")


# def capfirst(request):
#     return HttpResponse("capitalize first")


# def charcount(request):
#     return HttpResponse("character counted")


# def spaceremover(request):
#     return HttpResponse("space removed")


# def newlineremove(request):
#     return HttpResponse("new line removed")
