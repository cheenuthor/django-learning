from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound

# Create your views here.


def monthly_challenges(request, month):
    # month is url that appended
    challenge_text = None
    if month == 'january':
        challenge_text = 'Eat no meat for the entire month'
    elif month == 'february':
        challenge_text = 'Walk for atleast 20 min a day'
    elif month == 'march':
        challenge_text = 'Learn Django and be a backend developer'
    else:
        return HttpResponseNotFound("This month is not supported")
        # return a 404 error
    return HttpResponse(challenge_text)
