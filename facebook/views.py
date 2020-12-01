from django.shortcuts import render, redirect
from facebook.models import Article, Page, Comment

def help(request):
    return render(request, 'help.html')

def warn(request):
    return render(request, 'warn.html')

def fail(request):
    return render(request, 'fail.html')

def page_list(request) :
    pages = Page.objects.all().order_by('-created_ad')
    return render(request, 'page_list.html', {'pages': pages})

def newsfeed(request) :
    articles = Article.objects.all().order_by('-created_at')
    return render(request, 'newsfeed.html', {'articles': articles})

def detail_feed(request, pk) :
    article = Article.objects.get(pk=pk)

    if request.method == 'POST' :
        if request.POST['nickname'] != '' and request.POST['reply'] != '' and request.POST['password'] != '' :
            Comment.objects.create(
                article = article,
                author = request.POST.get('nickname', ''),
                text = request.POST.get('reply', ''),
                password = request.POST.get('password')
            )
            return redirect(f'/feed/{ article.pk }')

    return render(request, 'detail_feed.html', {'article': article})

def new_feed(request) :
    if request.method == 'POST' :
        if request.POST['author'] != '' and request.POST['title'] != '' and request.POST['cont'] != '' and request.POST['password'] != '' :
            cont = request.POST['cont']
            cont += ' - 고객님이 작성해주신 글'

            new_article = Article.objects.create(
                author = request.POST['author'],
                title = request.POST['title'],
                text = cont,
                password = request.POST['password']
            )

        print(f'새글 작성됨 : { new_article.created_at } / 제목 : { new_article.title }')
        return redirect(f'/feed/{ new_article.pk }/')

    return render(request, 'new_feed.html')

def edit_feed(request, pk) :
    article = Article.objects.get(pk=pk)

    if request.method == 'POST' :
        if request.POST['password'] == article.password :
            article.author = request.POST['author']
            article.title = request.POST['title']
            article.text = request.POST['cont']
            article.save()

            return redirect(f'/feed/{ article.pk }')
        else :
            return redirect('/fail')

    return render(request, 'edit_feed.html', {'article': article})

def remove_feed(request, pk) :
    article = Article.objects.get(pk=pk)

    if request.method == 'POST' :
        if request.POST['password'] == article.password :
            print(f'글 삭제됨 : {article.title}')
            article.delete()
            return redirect('/newsfeed')
        else :
            return redirect('/fail')

    return render(request, 'remove_feed.html', {'article': article})

def new_page(request) :
    if request.method == 'POST' :
        Page.objects.create(
            master = request.POST.get('master', ''),
            name = request.POST.get('name', ''),
            text = request.POST.get('cont', ''),
            category = request.POST.get('category', '')
        )
        return redirect('/page_list')

    return render(request, 'new_page.html', {})

def edit_page(request, pk) :
    page = Page.objects.get(pk=pk)
    if request.method == 'POST' :
        page.master = request.POST.get('master')
        page.name = request.POST.get('name')
        page.text = request.POST.get('cont')
        page.category = request.POST.get('category')
        page.save()

        return redirect('/page_list')

    return render(request, 'edit_page.html', {'page': page})

def remove_page(request, pk) :
    page = Page.objects.get(pk=pk)
    if request.method == 'POST' :
        print(f'페이지 삭제됨 : {page.name}')
        page.delete()
        return redirect('/page_list')

    return render(request, 'remove_page.html', {'page': page})

def remove_comment(request, pk) :
    comment = Comment.objects.get(pk=pk)
    if request.method == 'POST' :
        if request.POST.get('password') == comment.password :
            comment.delete()
            return redirect(f'/')

    return render(request, 'remove_comment.html', {'comment': comment})