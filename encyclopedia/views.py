from random import randint

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from markdown2 import Markdown

from . import util
from .forms import EntryForm


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def get_entry_by_title(request, title):

    content = util.get_entry(title)
    if not content:
        return page_404(request)
    mder = Markdown()
    content = mder.convert(content)

    return render(request, "encyclopedia/entry_by_title.html", {
        "title": title,
        "content": content
    })

def get_create_form(request):

    if request.method == "POST":
        entry_form = EntryForm(request.POST)
        if entry_form.is_valid():
            title = request.POST.get("title")
            content = request.POST.get("content")
            util.save_entry(title, content)
            return HttpResponseRedirect(reverse('get_entry_by_title', kwargs={'title': title}))
    else:
        entry_form = EntryForm()

    return render(request, "encyclopedia/form.html", {
            "title": "Create New Entity",
            "form": entry_form
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


def edit_entry_by_title(request, title):
    if request.method == "POST":
        entry_form = EntryForm(request.POST)
        if entry_form.is_valid():
            util.save_entry(request.POST.get("title"), request.POST.get("content"))

            return HttpResponseRedirect(reverse('get_entry_by_title', kwargs={'title': title}))
    else:
        content = util.get_entry(title)

        if not content:
            return page_404(request)

        entry_form = EntryForm(initial={"title": title, "content": content})

    return render(request, "encyclopedia/form.html", {
            "title": "Edit Entity " + title,
            "form": entry_form
        })

