from django.shortcuts import render

def header_view(request):
    return render(request, 'components/header.html')
