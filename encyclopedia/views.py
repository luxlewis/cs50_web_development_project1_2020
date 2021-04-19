from django.shortcuts import render
from . import util
import markdown2
from django import forms
from django.urls import reverse
from django.http import HttpResponseRedirect

class NewSearchForm(forms.Form):
    title = forms.CharField(label="Title")
    content = forms.CharField(label="Enter Markdown", widget=forms.Textarea())


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
            "not_found": title
        })


def search(request):
    query = request.GET.get("q")
    entries = util.list_entries()
    search_result = [s for s in entries if query.lower() in s.lower()]
    if util.get_entry(query):
        return render(request, "encyclopedia/search.html", {
            "title": markdown2.markdown(util.get_entry(query))
        })
    elif search_result:
        return render(request, "encyclopedia/search_results.html", {
            "results": search_result
        })
    else:
        return render(request, 'encyclopedia/error.html', {
            "not_found": query
        })

def new_page(request):
    if request.method == "POST":
        form = NewSearchForm(request.POST)
        if form.is_valid():
            content = form.cleaned_data["content"]
            title = form.cleaned_data["title"]
            if util.get_entry(title):
                return render(request, 'encyclopedia/error.html', {
                    "already_exists": title
                })
            else:
                util.save_entry(title, content)
                return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, 'encyclopedia/new_page.html', {
        "form": NewSearchForm()
    })


