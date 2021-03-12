from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect

# Create your views here.
monthly_challenges = {
    "january": "Eat no meat for the entire month",
    "february": "Walk for atleast 20 min a day",
    "march": "Learn django & be a backend developer",
    "april": "celebrate the life of with people",
    "may": "Work hard and together",
    "june": "prepare for the 1 year learning",
    "july": "Go to the tour of world",
    "august": "holiday on 15th august",
    "september": "thanks all your teachers",
    "october": "learn flutter",
    "november": "happy diwalli🎆",
    "december": "Happy merry chiristmas"

}


def get_monthly_challenge(request, month):
    # month is url that appended
    try:
        challenge_text = monthly_challenges[month]
        return HttpResponse(challenge_text)
    except:
        return HttpResponseNotFound("This month is not supported")
    # return a 404 error


def get_monthly_challenge_by_number(request, month):
    # ? converting dict to list
    months = list(monthly_challenges.keys())
    redirected_month = months[month-1]
    if month > len(months):
        return HttpResponseNotFound("Invalid month")
    # redirect the url to the specified path
    return HttpResponseRedirect("/challenges/"+redirected_month)
