# Frasa NLP: Deteksi
#
# Copyright (C) 2023 Frasa Project
# Author: Novianto Rahmadi <novay@btekno.id>
# URL: <https://frasa.id/>
# For license information, see LICENSE.TXT

"""
Frasa Deteksi

Modul untuk melakukan deteksi pada beberapa hal seperti
- Prediksi Gender dari nama seseorang
- Prediksi Bahasa Daerah yang digunakan
- Prediksi Topik dalam suatu kalimat
- Prediksi Kesimpulan dari suatu dokumen
- Prediksi Tingkat Kesamaan dari beberapa dokumen
"""

from frasa.deteksi.gender import model_gender, probabilitas
import json

class gender:
    def __init__(self, nama):
        self.nama = nama
        self.gender = model_gender().classify(nama)
        self.prob = probabilitas(nama)
    
    def json(self):
        return json.dumps({'nama': self.nama, 'gender': self.gender, 'probabilitas': self.prob})
    
    def get_nama(self):
        return self.nama
    
    def get_gender(self):
        return self.gender
    
    def get_prob(self):
        return self.prob