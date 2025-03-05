from django.contrib import admin
from django.urls import path, include  # ✅ 確保有 include()

urlpatterns = [
    path('admin/', admin.site.urls),
    path('myhello/', include('myhello.urls')),  # ✅ 確保 myhello 有正確的子路由
    path('', include('myhello.urls')),  # ✅ 讓根路徑 `/` 也指向 myhello
]
# ✅ 確保 myhello 有正確的子路由