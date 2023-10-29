from django.shortcuts import render

from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def get_entry_by_title(request, title):

    content = util.get_entry(title)
    if not content:
        return render(request, "encyclopedia/404.html",status=404)

    return render(request, "encyclopedia/entry_by_title.html", {

        "content": content
    })

