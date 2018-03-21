
from django.conf.urls import url
from django.contrib import admin
from django.conf.urls import include
# include 를 import 를 하지 않을 경우 에러 발생 장고 걸스 예제에는 이부분이 빠져 있다. 

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'', include('blog.urls')),
]
