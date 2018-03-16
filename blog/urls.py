from django.urls import path
from .import views

app_name='blog'
urlpatterns = [
    #path(r'',views.post_list, name='post_list'),
    path(r'',views.post_list, name='post_list'),
    path(r'<int:year>/<int:month>/<int:day>/<post>/',
         views.post_detail,name='post_detail'),
    path(r'<int:post_id>/share/',views.post_share,name='post_share'),
]