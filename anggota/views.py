# yourappname/views.py
from django.shortcuts import render

def index(request):
    return render(request, 'base.html', {})



def absen_page(request):
    context = {
        'variable1': 'Value 1',
        'variable2': 'Value 2',
        # Add more key-value pairs as needed
    }
    return render(request, 'absen.html', context)
