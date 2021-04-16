from django.shortcuts import render
from . import util
import markdown2

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
    query = request.GET.get("q")
    entries = util.list_entries()
    print(entries)
    search_result = [s for s in entries if query.lower() in s.lower()]
    if util.get_entry(query):
        return render(request, "encyclopedia/search.html", {
            "title": markdown2.markdown(util.get_entry(query))
        })
    elif search_result:
        print("yes")
        print(search_result)
        return render(request, "encyclopedia/search_results.html", {
            "results": search_result
        })
    else:
        return render(request, 'encyclopedia/error.html', {
            "error": query
        })




