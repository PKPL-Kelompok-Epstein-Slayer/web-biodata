from django.test import TestCase
from django.urls import reverse


class IndexViewTest(TestCase):

    def test_halaman_index_bisa_dibuka(self):
        # 1. Pura-puranya kita buka URL halaman utama ('index')
        url = reverse("index")
        response = self.client.get(url)

        # 2. Pastikan webnya merespons dengan sukses (Status 200 OK)
        self.assertEqual(response.status_code, 200)

        # 3. Pastikan template yang dipakai benar-benar 'biodata/index.html'
        self.assertTemplateUsed(response, "biodata/index.html")
