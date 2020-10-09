from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [
# Hit URL to get Data of Member with Activity Periods
    path('data/', views.DataList.as_view()),
]