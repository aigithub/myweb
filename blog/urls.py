from django.urls import path
from .import views

app_name='blog'
urlpatterns = [
    #path(r'',views.post_list, name='post_list'),
    path(r'',views.post_list, name='post_list'),
    path(r'^(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})/(?P<post>[-\w]+)/$',
         views.post_detail,name='post_detail'),
    path(r'<int:post_id>/share/',views.post_share,name='post_share'),
]