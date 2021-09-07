from django.shortcuts import get_object_or_404
from django.views.generic import ListView, DetailView

from blog.models import BlogPost, BlogCategory
from core.forms import ContactForm


class ListBlog(ListView):
    model = BlogPost
    queryset = BlogPost.objects.order_by('-created')
    template_name = 'view_blogs_by_date.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context_data = super(ListBlog, self).get_context_data()
        context_data['form'] = ContactForm
        return context_data


class ListBlogCategory(ListView):
    model = BlogPost
    queryset = BlogPost.objects.order_by('category')
    template_name = 'view_blog_category.html'


class ListBlogByCategory(ListView):
    model = BlogPost
    template_name = 'view_blogs_by_date.html'

    def get_queryset(self):
        category = get_object_or_404(BlogCategory, slug=self.kwargs['slug'])
        return BlogPost.objects.filter(
            category=category
        ).order_by('-created')


class ListBlogByYear(ListView):
    model = BlogPost
    template_name = 'view_blogs_by_date.html'

    def get_queryset(self):
        return BlogPost.objects.filter(
            created__year=self.kwargs['year']
        ).order_by('-created')


class BlogDetailView(DetailView):
    model = BlogPost
    context_object_name = 'blog_details'
    template_name = 'view_blog.html'


class SearchBlog(ListView):
    model = BlogPost
    paginate_by = 25
    template_name = 'search_result.html'

    def get_queryset(self):
        keyword = self.request.GET.get('keyword')
        if keyword and len(keyword) >= 1:
            return BlogPost.objects.filter(title__icontains=keyword, is_published=True).order_by('-created')
        else:
            return BlogPost.objects.none()
