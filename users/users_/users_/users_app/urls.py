from django.contrib import admin
from django.urls import path, include
from .users_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('user_app/', include('user_app.urls'))
]