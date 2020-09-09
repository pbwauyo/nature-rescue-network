
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('<int:number>/', views.vote, name='votes'),
    path('query/', views.query_db, name='query-db'),
    path('choices-list/', views.ChoiceListView.as_view(), name="choice-list"),
]