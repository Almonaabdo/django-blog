from django.shortcuts import render, get_object_or_404
from .models import Posts
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin    # allows login required for ListView classes
from django.contrib.auth.mixins import UserPassesTestMixin   # allows only owner of sometihng to edit it
from django.contrib.auth.models import User



# Create your views here.
def home(request):
     #creates doctionary
     context = dict()
     context = {
          'posts': Posts.objects.all()
     }

    
     return render(request, 'blog/Home.html', context)



class PostListView(ListView):
     model = Posts
     template_name = 'blog/home.html'
     
     
     ordering = ['-date_posted']              # order the list from newest to oldest (remove the - to do from oldest to newest)
     context_object_name = 'posts'            # this will change the generic list object passed to home page so it can be parsed as posts
     paginate_by = 3                          # allow only number of posts per page.
     
     
class UserPostListVIew(ListView):
     model = Posts
     template_name = 'blog/user_posts.html'
     
     context_object_name = 'posts'            # this will change the generic list object passed to home page so it can be parsed as posts
     paginate_by = 5                          # allow only number of posts per page.
     
     
     def get_queryset(self):
          user = get_object_or_404(User, username=self.kwargs.get('username'))
          return Posts.objects.filter(author=user).order_by('-date_posted')
     
     

class PostDetailed(DetailView):
     model = Posts
     template_name = 'blog/post_detail.html'
     
class PostCreateView(LoginRequiredMixin, CreateView):
     model = Posts
     fields = ['title', 'content']
     template_name = 'blog/post_form.html'
     
     
     # override the form valid to only allow posting when author is valid
     def form_valid(self, form):
          form.instance.author = self.request.user
          return super().form_valid(form)
     
     
     
     
class PostUpdateView(LoginRequiredMixin,UserPassesTestMixin , UpdateView):
     model = Posts
     fields = ['title', 'content']
     template_name = 'blog/post_form.html'
     
     
     # override the form valid to only allow posting when author is valid
     def form_valid(self, form):
          form.instance.author = self.request.user
          return super().form_valid(form)
     
     # this function prevents users from editing other authors posts
     def test_func(self):
          post = self.get_object()
          if self.request.user == post.author:
               return True
          return False
     
          
class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
     model = Posts
     success_url = '/'                        # user will be redirected to homepage on confirmation
     template_name = 'blog/post_confirm_delete.html'
     # this function prevents users from editing other authors posts
     def test_func(self):
          post = self.get_object()
          if self.request.user == post.author:
               return True
          return False


def about(request):
     return render(request, 'blog/About.html', {'title': 'about'})

