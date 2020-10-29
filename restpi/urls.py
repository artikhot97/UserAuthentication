from django.conf.urls import url
from . import views
from .views import PaginationView

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^registration/$', views.registration),
    url(r'^login_user/$', views.login_user),
    url(r'^get_list/$', views.get_list),
    url(r'^logout_user/$', views.logout_user),
    url(r'^search_data_by_condition/$',
        views.search_data_by_condition),
    url(r'^sort_user_deatils/$',
        views.sort_user_deatils),
    url(r'^pagination_list/$',PaginationView.as_view()),
]
