"""
URL configuration for mysite2 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from http.client import responses

from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
# 导入使用返回值

urlpatterns = [
    # 默认后台
    path('admin/', admin.site.urls),
    # 通过总路由找到应用路由，避免堆到一起  namespace命名空间，解除硬编码，命名空间加上路由名字
    path("",include("main.urls",namespace="main")),
    path("user/", include("user.urls")),
]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
    )
