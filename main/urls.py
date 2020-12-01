from django.urls import path
from django.contrib import admin

from facebook.views import fail, help, warn
from facebook.views import newsfeed, detail_feed, page_list, new_feed, edit_feed, remove_feed, new_page, edit_page, remove_page, remove_comment


urlpatterns = [
    path('admin/', admin.site.urls),

    path('fail/', fail),
    path('warn/', warn),
    path('help/', help),

    path('newsfeed/', newsfeed),
    path('/', newsfeed),
    path('', newsfeed),
    path('page_list/', page_list),
    path('new/', new_feed),
    path('feed/<pk>/', detail_feed),
    path('feed/<pk>/edit/', edit_feed),
    path('feed/<pk>/remove/', remove_feed),

    path('page/new/', new_page),
    path('page/<pk>/edit/', edit_page),
    path('page/<pk>/remove/', remove_page),
    path('comment/<pk>/remove', remove_comment)
]
