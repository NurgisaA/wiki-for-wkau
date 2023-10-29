from random import randint

from django.shortcuts import render

from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def get_entry_by_title(request, title):

    content = util.get_entry(title)

    if not content:
        return page_404(request)

    return render(request, "encyclopedia/entry_by_title.html", {
        "title": title,
        "content": content
    })


def get_random(request):
    entries = util.list_entries()
    count_entries = len(entries)
    if count_entries < 0:
        return page_404(request)

    i = randint(0, count_entries-1)

    return get_entry_by_title(request, entries[i])


def page_404(request):
    return render(request, "encyclopedia/404.html", status=404)
