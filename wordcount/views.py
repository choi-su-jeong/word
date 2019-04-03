from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def result(request):
    return render(request, 'result.html')

def result(request):
    text = request.GET['fulltext']
    words = text.split() 
    word_count = {}
    for word in words:
        if word in word_count:
            word_count[word]+=1
        else:
            word_count[word]=1
    return render(request, 'result.html', {'full' : text, 'total':len(words),'count': word_count.items})