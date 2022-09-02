from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.contrib import messages
# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView
from blog.models import BlogPost
from blog.forms import BlogPostForm


# def handle_not_found(request, exception):
#     return render(request, "404.html")

# crudl (create retrieve update delete list)
# these views work fine with out the need of Model form
#########################################################################
# class BlogPostCreate(CreateView):
#     model = BlogPost
#     fields = ["author", "title", "content"]
#     success_url = reverse_lazy("blog:blogpost-detail-list")
#     template_name = "blog/blogpost/create.html"
#
#
# class BlogPostUpdate(UpdateView):
#     model = BlogPost
#     fields = ["title", "content"]
#     success_url = reverse_lazy("blog:blogpost-detail-list")
#     template_name = "blog/blogpost/update.html"


#
#
class BlogPostDetail(DetailView):
    model = BlogPost
    template_name = "blog/blogpost/detail.html"


#
#
class BlogPostDelete(DeleteView):
    model = BlogPost
    success_url = reverse_lazy("blog:blogpost-detail-list")
    template_name = "blog/blogpost/delete.html"


class BlogPostList(ListView):
    model = BlogPost
    template_name = "blog/blogpost/detailList.html"


############################################################################

# Now with the Model form we can make the crudl classes
# without the need for neither fields nor model
# now we can have an annotation saying that this class require login in order to function

class BlogPostCreate(LoginRequiredMixin, CreateView):
    # il prof ha detto che non possiamo togliere il campo model
    # per far funzionare la create ma stranamente mi funziona anche senza
    # ora ha detto che non serve più il model,(**Roba da pazzi**)
    # model = BlogPost
    form_class = BlogPostForm
    success_url = reverse_lazy("blog:blogpost-detail-list")
    template_name = "blog/blogpost/create.html"


class BlogPostUpdate(UpdateView):
    model = BlogPost
    form_class = BlogPostForm
    success_url = reverse_lazy("blog:blogpost-detail-list")
    template_name = "blog/blogpost/update.html"


# class BlogPostListViewA