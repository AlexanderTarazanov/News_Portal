from django.urls import reverse_lazy
from django.views.generic import (ListView, DetailView, CreateView, UpdateView, DeleteView)
from .filters import PostFilter
from .forms import PostForm
from .models import Post
from django.shortcuts import redirect



class PostsList(ListView):
    model = Post
    ordering = '-created_time'
    template_name = 'flatpages/posts.html'
    context_object_name = 'posts'
    paginate_by = 10  # вот так мы можем указать количество записей на странице


class PostSearch(ListView):
    model = Post
    ordering = '-created_time'
    template_name = 'flatpages/post_search.html'
    context_object_name = 'posts'
    paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = PostFilter(self.request.GET, queryset)
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filterset'] = self.filterset
        return context


class PostDetail(DetailView):
    model = Post
    template_name = 'flatpages/post.html'
    context_object_name = 'post'


class NewsCreate(CreateView):
    form_class = PostForm
    model = Post
    template_name = 'flatpages/news_create.html'

    def form_valid(self, form):
        Post = form.save(commit=False)
        Post.post_type = 'Новость'
        return super().form_valid(form)


class NewsUpdate(UpdateView):
    model = Post
    fields = ['author', 'title', 'text']
    template_name = 'flatpages/news_edit.html'

    def dispatch(self, request, *args, **kwargs):
        Post = self.get_object()
        if Post.post_type != 'Новость':
            return redirect('articles_edit', Post.pk)
        return super(NewsUpdate, self).dispatch(request, *args, **kwargs)


class NewsDelete(DeleteView):
    model = Post
    template_name = 'flatpages/news_delete.html'
    success_url = reverse_lazy('post_list')

    def dispatch(self, request, *args, **kwargs):
        Post = self.get_object()
        if Post.post_type != 'Новость':
            return redirect('articles_delete', Post.pk)
        return super(NewsDelete, self).dispatch(request, *args, **kwargs)


class ArticlesCreate(CreateView):
    form_class = PostForm
    model = Post
    template_name = 'flatpages/articles_create.html'

    def form_valid(self, form):
        Post = form.save(commit=False)
        Post.post_type = 'Статья'
        return super().form_valid(form)


class ArticlesUpdate(UpdateView):
    model = Post
    fields = ['author', 'title', 'text']
    template_name = 'flatpages/articles_edit.html'

    def dispatch(self, request, *args, **kwargs):
        Post = self.get_object()
        if Post.post_type != 'Статья':
            return redirect('news_edit', Post.pk)
        return super(ArticlesUpdate, self).dispatch(request, *args, **kwargs)


class ArticlesDelete(DeleteView):
    model = Post
    template_name = 'flatpages/articles_delete.html'
    success_url = reverse_lazy('post_list')

    def dispatch(self, request, *args, **kwargs):
        Post = self.get_object()
        if Post.post_type != 'Статья':
            return redirect('news_delete', Post.pk)
        return super(ArticlesDelete, self).dispatch(request, *args, **kwargs)
