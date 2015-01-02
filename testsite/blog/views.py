
from django.shortcuts import render
from blog.models import Post


def post_list(request):
    posts = Post.objects.filter(published_date__isnull=False).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})
#def post_detail(request, pk):
 #   post = get_object_or_404(Post, pk=pk)
  #  return render(request, 'blog/post_detail.html', {'post': post})
