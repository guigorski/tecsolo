from django.conf.urls import include, url
from . import views

urlpatterns = [

    url(r'^$', views.login, name='login'),
    url(r'^add/', views.index, name='add'),
    url(r'^pagos/', views.pagos, name='pagos'),
    url(r'^gastos/', views.gastos, name='gastos'),
    url(r'^new_gastos/', views.new_gastos, name='new_gastos'),
    url(r'^post_list/', views.post_list, name='pendentes'),
    url(r'^reducao/', views.reducao, name='reducao'),
    url(r'^amostra/(?P<pk>[0-9]+)/$', views.amostra_detail),
    url(r'^search/', views.search, name='search'),
    url(r'^search_results/', views.search_results, name='search_results'),
    url(r'^amostra/(?P<pk>[0-9]+)/edit/$', views.amostra_edit, name='amostra_edit'),
    url(r'^gasto_detail/(?P<pk>[0-9]+)/$', views.gasto_detail),
    url(r'^gasto_detail/(?P<pk>[0-9]+)/edit/$', views.gasto_edit, name='gasto_edit'),


]
