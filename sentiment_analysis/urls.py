from django.urls import path
from django.conf.urls import url ,include
from . import views


#urlpatterns = [
 #   url(r'^$', views.sentiment, name="choose_sentiment_or_emotion"),
#]

urlpatterns = [
    path('', views.sentiment, name="choose_sentiment"),
    path('sentiment/', include('sentiment.urls')),

  
]
