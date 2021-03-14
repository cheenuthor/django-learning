from datetime import date
from django.shortcuts import render


all_posts = [
    {
        "slug": "hike-in-the-mountains",
        "image": "woods.jpg",
        "author": "CHeeNU",
        "date": date(2020, 7, 21),
        "title": "Mountain Hiking",
        "excerpt": """There's noting like the views while hiking in the Mountain
                    and I was'nt even prepared for what happend while I was enjoying
                     the view""",
        "centent": """
                    Lorem ipsum dolor sit amet consectetur adipisicing elit.
                    Ab iste quia reiciendis nisi accusamus omnis debitis
                    similique assumenda ex aliquam suscipit, ratione commodi
                    sequi a cum rerum sint? Incidunt, natus!
                   """
    }, {
        "slug": "hike-in-the-mountains",
        "image": "mountains.jpg",
        "author": "CHeeNU",
        "date": date(2020, 6, 21),
        "title": "Mountain Diving",
        "excerpt": """There's noting like the views while hiking in the Mountain
                    and I was'nt even prepared for what happend while I was enjoying
                     the view""",
        "centent": """
                    Lorem ipsum dolor sit amet consectetur adipisicing elit.
                    Ab iste quia reiciendis nisi accusamus omnis debitis
                    similique assumenda ex aliquam suscipit, ratione commodi
                    sequi a cum rerum sint? Incidunt, natus!
                   """
    }, {
        "slug": "hike-in-the-mountains",
        "image": "coding.jpg",
        "author": "CHeeNU",
        "date": date(2020, 1, 21),
        "title": "Mountain Walking",
        "excerpt": """There's noting like the views while hiking in the Mountain
                    and I was'nt even prepared for what happend while I was enjoying
                     the view""",
        "centent": """
                    Lorem ipsum dolor sit amet consectetur adipisicing elit.
                    Ab iste quia reiciendis nisi accusamus omnis debitis
                    similique assumenda ex aliquam suscipit, ratione commodi
                    sequi a cum rerum sint? Incidunt, natus!
                   """
    }
]
# Create your views here.


def get_date(post):
    return post['date']


def starting_page(request,):
    sorted_post = sorted(all_posts, key=get_date)
    latest_post = sorted_post[-3:]
    return render(request, 'blog/index.html', {
        "posts": latest_post
    })


def posts(request):
    return render(request, 'blog/all-posts.html')


def post_details(request, slug):
    return render(request, 'blog/post-detail.html', {

    })
