from django.shortcuts import render
from . import util
import markdown2
from django.urls import reverse
from django.http import HttpResponseRedirect
from django import forms


class SearchForm(forms.Form):
    title = forms.CharField(widget=forms.TextInput(attrs={
        "class": "search"
    }))


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries(),
    })


def title(request, title):
    if util.get_entry(title):
        return render(request, "encyclopedia/title.html", {
            "title": markdown2.markdown(util.get_entry(title))
        })
    else:
        return render(request, 'encyclopedia/error.html', {
            "error": title
        })

def search(request):
    entries = util.list_entries()
    query = request.GET.get("q")
    if util.get_entry(query):
        return render(request, "encyclopedia/search.html", {
            "title": markdown2.markdown(util.get_entry(query))
        })
    else:
        return render(request, 'encyclopedia/error.html', {
            "error": query
        })



