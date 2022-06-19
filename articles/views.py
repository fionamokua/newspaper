from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.urls import reverse_lazy
from django.views.generic import ListView,DetailView
from django.views.generic.edit import DeleteView,UpdateView,CreateView
# Create your views here.
from . import models

class ArticleListView(LoginRequiredMixin,ListView):
    model=models.Article
    template_name='article_list.html'
    login_url='login'
class ArticleDetailView(LoginRequiredMixin,DetailView):
    model=models.Article
    template_name='article_detail.html'
    login_url='login'
class ArticleUpdateView(LoginRequiredMixin,UpdateView):
    model=models.Article
    fields=('title','body')
    template_name="article_update.html"
    login_url='login'
    def dispatch(self,request,*args,**kwargs):
        obj=self.get_object()
        if obj.author != self.request.user:
            raise PermissionDenied

class ArticleDeleteView(LoginRequiredMixin,DeleteView):
    model=models.Article
    template_name="article_delete.html"
    success_url=reverse_lazy('article_list.html')
    login_url='login'
    def dispatch(self,request,*args,**kwargs):
        obj=self.get_object()
        if obj.author != self.request.user:
            raise PermissionDenied
        return super().dispatch(request,*args,**kwargs)

class ArticleCreateView(LoginRequiredMixin,CreateView):
    model=models.Article
    template_name="article_create.html"
    fields=('title' ,  'body' )
    login_url='login'

    #setting default author to user
    def form_valid(self,form):
        form.instance.author=self.request.user
        return super().form_valid(form)