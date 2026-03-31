from django.shortcuts import render
from django.views.decorators.http import require_GET


@require_GET
def index(request):
    # Fungsi ini bertugas memanggil file index.html yang kamu buat tadi
    return render(request, "biodata/index.html")
