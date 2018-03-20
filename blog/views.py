from django.shortcuts import render
from django.utils import timezone
from .models import Post
# Create your views here.

def post_list(request):
    # posts = Post.objects.all()
    # 아래쿼리는 데이터가 추출이 안된다 조건이 안맞는듯 그래서 모든 데이터 불러오는 걸로 변경
    # 혹은 다른 filter 로 조건을 변경
    #posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    posts = Post.objects.filter(id=5)
    return render(request, 'blog/post_list.html', {'posts':posts})
