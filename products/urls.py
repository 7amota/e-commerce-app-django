from django.urls import path , include
from . import views
urlpatterns = [
    path('',views.IndexViews.as_view(), name='index')
]
