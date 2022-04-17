from django.conf import settings
from django.conf.urls.static import static
from django import views
from django.contrib import admin
from django.urls import path
from App import views

app_name='App'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name="home"),
    path('order/<int:flavour_id>', views.order, name="order")
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
