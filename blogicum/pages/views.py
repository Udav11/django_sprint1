from django.shortcuts import render


def about(request):
    return render(request, template_name='pages/about.html')


def rules(request):
    return render(request, template_name='pages/rules.html')
