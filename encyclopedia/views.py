from django.shortcuts import render
from . import util
import markdown2



def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
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
