from datetime import date
from django.shortcuts import render


all_posts = [
    {
        "slug": "nature",
        "image": "woods.jpg",
        "author": "CHeeNU",
        "date": date(2020, 7, 21),
        "title": "Nature",
        "excerpt": """There's noting like the views while hiking in the Mountain
                    and I was'nt even prepared for what happend while I was enjoying
                     the view""",
        "content": """
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
        "title": "Hike in the mountains",
        "excerpt": """There's noting like the views while hiking in the Mountain
                    and I was'nt even prepared for what happend while I was enjoying
                     the view""",
        "content": """
                    Lorem ipsum dolor sit amet consectetur adipisicing elit.
                    Ab iste quia reiciendis nisi accusamus omnis debitis
                    similique assumenda ex aliquam suscipit, ratione commodi
                    sequi a cum rerum sint? Incidunt, natus!
                   """
    }, {
        "slug": "programming",
        "image": "coding.jpg",
        "author": "CHeeNU",
        "date": date(2020, 1, 21),
        "title": "Programming is Great",
        "excerpt": """There's noting like the views while hiking in the Mountain
                    and I was'nt even prepared for what happend while I was enjoying
                     the view""",
        "content": """
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
    return render(request, 'blog/all-posts.html', {
        "posts": all_posts
    })


def post_details(request, slug):
    identified_post = next(post for post in all_posts if post['slug'] == slug)
    return render(request, 'blog/post-detail.html', {
        "post": identified_post
    })
