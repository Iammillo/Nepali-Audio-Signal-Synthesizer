from django.shortcuts import render
from django.http import HttpResponse


from . import main

from django import forms

class NameForm(forms.Form):
    text = forms.CharField(label='text', max_length=1000)


def index(request,number=0):
    return(render(request,"index.html"))

def tempo(request):
    if request.method == 'POST':
        form = NameForm(request.POST)
        if form.is_valid():
            try:
                a = form.cleaned_data['text']
                X = main.engine()
                X.text_entry(a);
                X.play();
                return HttpResponse("Played")
            except:
                return HttpResponse("Problem Occured.")

        else:
            return HttpResponse("Invalid Input")
    else:
        return HttpResponse("Invalid Input")
