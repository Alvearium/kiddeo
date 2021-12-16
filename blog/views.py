from django.shortcuts import get_list_or_404, get_object_or_404, render

from blog.models import Blog, Comments

# Create your views here.
def blogView(request):
    posts = Blog.objects.all()
    return render(request, 'blog.html', {'posts': posts})

def postView(request, post_slug):
    post = get_object_or_404(Blog, slug = post_slug)
    comments = get_list_or_404(Comments, title_post = post.id)
    similar_posts = get_list_or_404(Blog, rubric = post.rubric)
    return render(request, 'post.html', {
        'post': post,
        'comments': comments,
        'similar_posts': similar_posts,
        }
    )
