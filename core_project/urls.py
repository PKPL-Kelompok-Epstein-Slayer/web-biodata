from django.contrib import admin
from django.urls import path, include
from biodata import views  # <-- 1. Tambahkan import ini

urlpatterns = [
    path("admin/", admin.site.urls),
    # Rute untuk Allauth (Google Login) yang sudah kita buat sebelumnya
    path("accounts/", include("allauth.urls")),
    # <-- 2. Tambahkan rute kosong ini untuk halaman utama
    path("", views.index, name="index"),
]
