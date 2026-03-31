from django.shortcuts import render


def index(request):
    # Fungsi ini bertugas memanggil file index.html yang kamu buat tadi
    return render(request, "biodata/index.html")
