from django.shortcuts import render
from django.shortcuts import get_object_or_404, render

# Create your views here.
def index(request):
    return render(request,'index.html')

def post(request):
   return render(request,'post.html')


#  def post(request, post_id):
#      post = get_object_or_404(Post, pk = post_id)
#      return render(request, 'post.html', {'post': post})

