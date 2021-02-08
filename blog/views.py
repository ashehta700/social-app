from django.shortcuts import render , get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin  ,UserPassesTestMixin   # uses for  make validation of any page you want
from django.http import HttpResponse 
from .models import Post
from django.views.generic import ListView , DetailView ,CreateView ,UpdateView , DeleteView
# uses for paggination
from django.core.paginator import Paginator






def home(request):
    context={
        "posts": Post.objects.all()
    }
    return render(request,'blog/home.html',context)

# make this with django to list our model automatic 
class PostListView(ListView):
    model = Post
    template_name='blog/home.html'
    context_object_name='posts'
    ordering = ['-data_posted'] #using for order 
    paginate_by = 5             #paggination 
    
    
    
# make this with django to list our users of that making a post automatic 
class userPostListView(ListView):
    model = Post
    template_name='blog/user_posts.html'
    context_object_name='posts' 
    paginate_by = 5            #paggination 
    
    #this function is used to control of each user ..
    def get_queryset(self):
        user = get_object_or_404(User , username = self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-data_posted')
    
    
     
    
    
    
# make this with django to show the details of each post with PK autmatic     
class PostDetailView(DetailView):
    model = Post
    
    
# make this with django to create anew form     
class PostCreateView(LoginRequiredMixin , CreateView):
    model = Post
    fields =['title' , 'content', 'photo' , 'video']
    # You must tell the form that who is user is logged in 
    def form_valid(self , form):
        form.instance.author = self.request.user
        return super().form_valid(form) 


# make this with django to update  our post form     
class PostUpdateView(LoginRequiredMixin ,UserPassesTestMixin,  UpdateView):
    model = Post
    fields =['title' , 'content', 'author', 'photo', 'video']
    # You must tell the form that who is user is logged in 
    def form_valid(self , form):
        form.instance.author = self.request.user
        return super().form_valid(form) 
    
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


# make this with django to delete Your post      
class PostDeleteView(LoginRequiredMixin ,UserPassesTestMixin,  DeleteView):
    model = Post
    success_url='/'
    
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False
    


    
    

def about(request):
    return render(request,'blog/about.html',{ 'title':'about' })

