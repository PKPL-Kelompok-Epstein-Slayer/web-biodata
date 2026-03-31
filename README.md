# 📝 Project Biodata - Tugas Kelompok PKPL

Proyek ini adalah aplikasi web berbasis Django yang dilengkapi dengan fitur Autentikasi menggunakan Google (Google OAuth2) via `django-allauth`.

## 🛠️ Persyaratan Sistem (Prerequisites)
Sebelum menjalankan proyek ini, pastikan komputer Anda sudah terinstal:
* Python (versi 3.8 atau lebih baru)
* Git

---

## 🚀 Cara Menjalankan Proyek di Komputer Lokal

Ikuti langkah-langkah di bawah ini secara berurutan:

### 1. Clone Repository
Buka terminal/Command Prompt, lalu jalankan perintah ini untuk mengunduh kode dari GitHub:
```bash
git clone <URL_REPOSITORY_KALIAN>
cd <NAMA_FOLDER_REPOSITORY>
```

### 2. Buat dan Aktifkan Virtual Environment
Sangat disarankan untuk menggunakan *virtual environment* agar *library* proyek ini tidak bentrok dengan proyek Python lainnya di komputer Anda.

**Untuk Windows:**
```bash
python -m venv env
.\env\Scripts\activate
```

**Untuk Mac/Linux:**
```bash
python3 -m venv env
source env/bin/activate
```

### 3. Install Dependencies
Jalankan perintah ini untuk menginstal Django, Allauth, dan paket lainnya yang ada di `requirements.txt`:
```bash
pip install -r requirements.txt
```

### 4. Atur Environment Variables (Kredensial Google) ⚠️
Proyek ini menggunakan variabel lingkungan rahasia untuk sistem Login Google. 
1. Buat sebuah file baru bernama **`.env`** di dalam folder utama (sejajar dengan file `manage.py`).
2. *Copy-paste* kode berikut ke dalam file **`.env`** dan isi nilainya:

```env
SECRET_KEY=isi_dengan_kunci_rahasia_django_kalian
GOOGLE_CLIENT_ID=isi_dengan_client_id_dari_google_console
GOOGLE_CLIENT_SECRET=isi_dengan_client_secret_dari_google_console
```
> **Catatan:** File `.env` ini **TIDAK BOLEH** di-commit atau di-push ke GitHub demi keamanan!

### 5. Jalankan Migrasi Database
Untuk membuat tabel-tabel bawaan Django dan Allauth di dalam *database* SQLite lokal, jalankan:
```bash
python manage.py migrate
```

### 6. Jalankan Server Lokal
Terakhir, nyalakan server Djangonya dengan perintah:
```bash
python manage.py runserver
```

Buka browser dan akses alamat: **`http://127.0.0.1:8000/`**

---

## 🔑 Catatan Khusus untuk Login Google
Jika Anda menggunakan kredensial Google Cloud Console milik sendiri untuk *testing*, pastikan Anda sudah menambahkan URL berikut ke dalam daftar **Authorized redirect URIs** di pengaturan Google Console Anda:
* `http://127.0.0.1:8000/accounts/google/login/callback/`

## 🧪 Menjalankan Unit Test
Untuk menjalankan *testing* otomatis (menggunakan `pytest`), jalankan perintah:
```bash
pytest
```
Untuk melihat *coverage* (cakupan) tes kode:
```bash
pytest --cov=.
```