from django.contrib import admin
from django.urls import path, include, re_path
import DeepGuardian.settings.base as settings
from django.conf.urls.static import static, serve

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('predictor.urls'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 
