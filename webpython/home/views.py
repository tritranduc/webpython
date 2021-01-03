from django.shortcuts import render
from django.http import HttpResponse
from django.http import Http404
# Create your views here.
def index(request):
    response = HttpResponse()
    response.writelines('<h1>Xin chào</h1>')
    response.write('Đây là app home')
    return response
def index(request):
    return render(request, 'pages/home.html')
def post(request, id):
    try:
        post = Post.objects.get(id=id)
    except Post.DoesNotExist:
        raise Http404("Bài viết không tồn tại")

    return render(request, 'blog/post.html', {'post': post})

def error(request, exception):
    return render(request, 'pages/error.html', {'message': "not fourd"})
    # exception
