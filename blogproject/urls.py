from django.contrib import admin
from django.urls import path, include
import blogapp.views
import portfolio.views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', blogapp.views.home, name="home"),
    #path('blog/', include('blogapp.urls')),
    path('<int:blog_id>', blogapp.views.detail, name="detail"), 
    path('new/',blogapp.views.new, name="new"),
    path('create/', blogapp.views.create, name="create"),
    path('mypage/', blogapp.views.mypage, name="mypage"),
    path('portfolio/',portfolio.views.portfolio, name="portfolio"),
] + static(settings.MEDIA_URL, document_roots=settings.MEDIA_ROOT)

