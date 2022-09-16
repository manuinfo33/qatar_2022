from django.shortcuts import render,redirect
from news.models import Articles
from news.forms import Form_news
from django.contrib.auth.decorators import login_required

@login_required
def create_article(request):
    if request.user.is_superuser:
        if request.method == 'POST':
            form=Form_news(request.POST)

            if form.is_valid():
                Articles.objects.create(
                    title=form.cleaned_data['title'],
                    description=form.cleaned_data['description'],
                    author=form.cleaned_data['author'],
                )
                return redirect(list_articles)
        
        elif request.method == 'GET':
            form= Form_news()
            context={'form':form}
            return render(request, 'news/new_article.html', context=context)
    else: return redirect ('login-super')
    
def list_articles(request):
    all_articles=Articles.objects.all()
    context={
        "all_articles":all_articles
    }
    return render(request,"news/all_articles.html",context=context)

def delete_article(request,pk):
    if request.method == 'GET':
        article= Articles.objects.get(pk=pk)
        context={'article':article}
        return render (request, 'news/delete_articles.html',context=context)
    elif request.method == 'POST':
        article= Articles.objects.get(pk=pk)
        article.delete()
        return redirect (list_articles)

def update_articles(request,pk):
    if request.method == 'POST':
        form=Form_news(request.POST)

        if form.is_valid():
            article=Articles.objects.get(id=pk)
            article.title=form.cleaned_data['title']
            article.description=form.cleaned_data['description']
            article.author=form.cleaned_data['author']
            article.save()

            return redirect (list_articles)
    
    elif request.method == 'GET':
        article=Articles.objects.get(id=pk)
        form=Form_news(initial={'title':article.title,
                                    'description':article.description,
                                    'author':article.author,
                                    })
        context={'form':form, 'article':article}
        return render (request, 'news/update_articles.html',context=context)