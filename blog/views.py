from django.views.generic import ListView, DetailView
from .models import Post

# Create your views here.


class BlogListView(ListView):
    model = Post
    template_name = 'home.html'


class BlogDetailedView(DetailView):
    model = Post
    template_name = 'post-detail.html'
