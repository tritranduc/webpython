from django.shortcuts import render
from django.http import HttpResponse
from django.http import Http404
# Create your views here.
# Create your views here.
from .models import Post
# Create your views here.
def list(request):
    Data = {'Posts': Post.objects.all().order_by('-date')}
    return render(request, 'blog/blog.html', Data)
def post(request, id):
    try:
        post = Post.objects.get(id=id)
    except Post.DoesNotExist:
        raise Http404("Bài viết không tồn tại")

    return render(request, 'blog/post.html', {'post': post})
from .form import RegistrationForm
from django.http import HttpResponseRedirect

def register(request):
    form = RegistrationForm()
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    return render(request, 'pages/register.html', {'form': form})
