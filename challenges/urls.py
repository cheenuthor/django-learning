from django.urls import path

from . import views

# created url config
urlpatterns = [
    # ?dyanmic path segments
    # <month> is should be same name as the function url name
    # *PATH CONVERTER
    # *str:string
    # *int:int
    path("<int:month>", views.monthly_challenge_by_number),
    # !order matters(int,str)....!
    path("<str:month>", views.monthly_challenges),
]
