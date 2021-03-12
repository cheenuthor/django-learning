from django.urls import path

from . import views

# created url config
urlpatterns = [
    # dyanmic path segments
    #  #<month> is should be same name as the function response name
    path("<month>", views.monthly_challenges)
]
