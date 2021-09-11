from django.shortcuts import get_object_or_404
from django.views.generic import ListView, DetailView

from blog.models import BlogPost, BlogCategory
from core.mixins import ContactFormViewMixin


class ListBlog(ContactFormViewMixin, ListView):
    model = BlogPost
    context_object_name = 'blogs'
    queryset = BlogPost.objects.order_by('-created')
    template_name = 'blog_home.html'


class ListBlogCategory(ContactFormViewMixin, ListView):
    model = BlogPost
    queryset = BlogPost.objects.order_by('category')
    template_name = 'blog_category.html'


class ListBlogByCategory(ContactFormViewMixin, ListView):
    model = BlogPost
    template_name = 'blog_home.html'

    def get_queryset(self):
        category = get_object_or_404(BlogCategory, slug=self.kwargs['slug'])
        return BlogPost.objects.filter(
            category=category
        ).order_by('-created')


class ListBlogByYear(ContactFormViewMixin, ListView):
    model = BlogPost
    template_name = 'blog_home.html'

    def get_queryset(self):
        return BlogPost.objects.filter(
            created__year=self.kwargs['year']
        ).order_by('-created')


class BlogDetailView(ContactFormViewMixin, DetailView):
    model = BlogPost
    context_object_name = 'blog'
    template_name = 'blog_detail.html'


class SearchBlog(ContactFormViewMixin, ListView):
    model = BlogPost
    paginate_by = 25
    template_name = 'search.html'

    def get_queryset(self):
        keyword = self.request.GET.get('keyword')
        if keyword and len(keyword) >= 1:
            return BlogPost.objects.filter(title__icontains=keyword, is_published=True).order_by('-created')
        else:
            return BlogPost.objects.none()
