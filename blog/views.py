from django.core.urlresolvers import reverse_lazy
from django.views.generic import (
    ArchiveIndexView, CreateView, DeleteView, DetailView,
    MonthArchiveView, YearArchiveView)

from core.utils import UpdateView

from .forms import PostForm
from .models import Post
from .utils import DateObjectMixin

class PostArchiveMonth(MonthArchiveView):
    model = Post
    date_field = 'pub_date'
    month_format = '%m'

class PostArchiveYear(YearArchiveView):
    model = Post
    date_field = 'pub_date'
    make_object_list = True

class PostCreate(CreateView):
    form_class = PostForm
    model = Post
    # template_name = 'blog/post_form.html'
    #
    # def get(self, request):
    #     return render(
    #         request,
    #         self.template_name,
    #         {'form': self.form_class()})
    #
    # def post(self, request):
    #     bound_form = self.form_class(request.POST)
    #     if bound_form.is_valid():
    #         new_post = bound_form.save()
    #         return redirect(new_post)
    #     else:
    #         return render(
    #             request,
    #             self.template_name,
    #             {'form': bound_form})


class PostDelete(DateObjectMixin, DeleteView):
    allow_future = True
    date_field = 'pub_date'
    model = Post
    success_url = reverse_lazy('blog_post_list')

class PostDetail(DateObjectMixin, DetailView):
    allow_future = True
    date_field = 'pub_date'
    model = Post


class PostList(ArchiveIndexView):
    allow_empty = True
    allow_future = True
    context_object_name = 'post_list'
    date_field = 'pub_date'
    make_object_list = True
    model = Post
    paginate_by = 5
    template_name = 'blog/post_list.html'

# class PostList(ListView):
#     model = Post

    # def get(self, request):
    #     return render(
    #         request,
    #         'blog/post_list.html',
    #         {'post_list': Post.objects.all()})


class PostUpdate(DateObjectMixin, UpdateView):
    allow_future = True
    date_field = 'pub_date'
    form_class = PostForm
    model = Post
