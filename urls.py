from django.urls import path
from . import views
#画像アップロードのために追加
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('upimg/', views.uploadimg, name="upimg"),
    path('imgview/', views.loginuser_imglist, name="imgview"),
    path('imgselect/<int:id>', views.imgselect, name="imgselect"),
]


#画像アップロードのために追加
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)