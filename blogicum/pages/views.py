from django.shortcuts import render


def about(request):
    return render(request, 'about/about.html')


def rules(request):
    return render(request, 'about/rules.html')
