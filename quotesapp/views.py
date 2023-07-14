from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import AuthorForm, TagForm, QuoteForm
from .models import Author, Tag, Quote

@login_required
def add_author(request):
    if request.method == 'POST':
        form = AuthorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(to='quotesapp:main')
        else:
            return render(request, 'quotesapp/add_author.html', {'form': form})

    return render(request, 'quotesapp/add_author.html', {'form': AuthorForm()})

@login_required
def add_tag(request):
    if request.method == 'POST':
        form = TagForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(to='quotesapp:main')
        else:
            return render(request, 'quotesapp/add_tag.html', {'form': form})

    return render(request, 'quotesapp/add_tag.html', {'form': TagForm()})

@login_required
def add_quote(request):
    tags = Tag.objects.all()

    if request.method == 'POST':
        form = QuoteForm(request.POST)
        if form.is_valid():
            new_quote = form.save()

            choice_tags = Tag.objects.filter(name__in=request.POST.getlist('tags'))
            for tag in choice_tags.iterator():
                new_quote.tags.add(tag)

            return redirect(to='quotesapp:main')
        else:
            return render(request, 'quotesapp/add_quote.html', {"tags": tags, 'form': form})

    return render(request, 'quotesapp/add_quote.html', {"tags": tags, 'form': QuoteForm()})

def author(request, author_name):
    author = get_object_or_404(Author.objects, name=author_name.replace('-', ' '))
    return render(request, 'quotesapp/author.html', {"author": author})


def main(request):
    quotes = Quote.objects.all()
    return render(request, 'quotesapp/index.html', {'quotes':quotes})