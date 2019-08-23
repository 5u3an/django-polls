from django.urls import path

from . import views

urlpatterns = [
    # ex: /mysite/
    path('', views.index, name='index'),
    # ex: /mysite/5/
    path('<int:question_id>/', views.detail, name='detail'),
    # ex: /mysite/5/results/
    path('<int:question_id>/results/', views.results, name='results'),
    # ex: /mysite/5/vote/
    path('<int:question_id>/vote/', views.vote, name='vote'),
    path('specifics/<int:question_id>/', views.detail, name='detail'),
    path('<int:question_id>/vote/', views.vote, name='vote'),

]

app_name = 'polls'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:question_id>/', views.detail, name='detail'),
    path('<int:question_id>/results/', views.results, name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
]
