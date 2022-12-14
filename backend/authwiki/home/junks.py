from django.db import models

class Comment(models.Model):
    # Each comment is associated with a specific article
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    # The comment text
    text = models.TextField()
    # The date and time the comment was created
    created_at = models.DateTimeField(auto_now_add=True)
    # The name of the user who wrote the comment
    author = models.CharField(max_length=50)

# In your views.py file:

def article_detail(request, pk):
    # Get the article with the specified primary key
    article = get_object_or_404(Article, pk=pk)
    # Get all the comments for the article
    comments = article.comments.all()
    # Render the template with the article and comments
    return render(request, 'article_detail.html', {
        'article': article,
        'comments': comments,
    })

# In your templates:

{# Display the article title and body #}
<h1>{{ article.title }}</h1>
<p>{{ article.body }}</p>

{# Loop through all the comments and display each one #}
{% for comment in comments %}
    <div class="comment">
        <p>{{ comment.text }}</p>
        <p>by {{ comment.author }} on {{ comment.created_at }}</p>
    </div>
{% endfor %}

for voting
# models.py

from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    votes = models.IntegerField(default=0)

class Vote(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    value = models.IntegerField(default=1)
# views.py

from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        if request.user.is_authenticated:
            # Check if the user has already voted on this post
            try:
                vote = Vote.objects.get(post=post, user=request.user)
                # If the user has already voted on this post, delete their previous vote
                vote.delete()
            except Vote.DoesNotExist:
                # If the user has not voted on this post, create a new vote
                vote = Vote(post=post, user=request.user, value=1)
                vote.save()
    # Calculate the total number of votes for this post
    votes = Vote.objects.filter(post=post).count()
    context = {'post': post, 'votes': votes}
    return render(request, 'post_detail.html', context)

from .models import Post

def create_post(request):
    # create a new post object
    post = Post()

    # set the post title and content
    post.title = request.POST.get('title')
    post.content = request.POST.get('content')

    # save the post object to the database
    post.save()

    # return a success message
    return HttpResponse("Post created successfully!")
