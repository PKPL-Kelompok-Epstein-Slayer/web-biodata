from django.shortcuts import render
from django.views.decorators.http import require_GET


@require_GET
def index(request):
    allowed_emails = [
        "muhammad.rafi41@ui.ac.id",
        "bismazharfan@gmail.com",
        "refkiseptian1@gmail.com",
        "muhathirmro@gmail.com",
    ]

    is_anggota = False

    if request.user.is_authenticated and request.user.email in allowed_emails:
        is_anggota = True

    context = {"is_anggota": is_anggota}

    return render(request, "biodata/index.html", context)
