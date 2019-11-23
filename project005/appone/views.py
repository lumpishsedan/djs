# pages/views.py
from django.views.generic import TemplateView, DetailView, ListView # new
from django.views.generic.edit import CreateView # new

from .models import Post

class HomePageView(TemplateView):
    template_name = 'home.html'
class SelectView(TemplateView):
    template_name = 'select.html'

class PostView(CreateView): # new
    model = Post
    template_name = 'post_new.html'
    fields = '__all__'

class PostDetailView(DetailView): # new
    model = Post
    template_name = 'post_detail.html'

class HomePageView(ListView):
    model = Post
    template_name = 'home.html'
    context_object_name = 'all_posts_list' # new
