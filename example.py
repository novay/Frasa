from frasa.sensor import sensor

text = "Dasar anj!ng kamu b4j1nGan."
censored_text = sensor.beep(text)
print(censored_text)





























# from frasa.deteksi.plagiat import plagiat

# """ Menggunakan URL """
# teks_1 = 'https://raw.githubusercontent.com/novay/amikom/main/datasets/text/kalimat-1.txt'
# teks_2 = 'https://raw.githubusercontent.com/novay/amikom/main/datasets/text/kalimat-2.txt'
# cek = plagiat.periksa(teks_1, teks_2, url=True).hitung()
# print('Persentase plagiarisme = {0}%'.format(cek))

# """ Menggunakan File """
# # cek = plagiat.periksa('/content/kalimat-1.txt', '/content/kalimat-2.txt', url=True).hitung()
# # print('Persentase plagiarisme = {0}%'.format(cek))

# """ Rabin Karp Method """
# rabin = plagiat.periksa("Aku sedang belajar kecerdasan buatan", "Mahasiswa yang cerdas selalu siap menerima tantangan", text=True).hitung()
# print('Rabin Karp Similarity = {0}%'.format(rabin))

# """ Jaccard Method """
# jaccard = plagiat.periksa("Aku sedang belajar kecerdasan buatan", "Mahasiswa yang cerdas selalu siap menerima tantangan", text=True, method='Jaccard').hitung()
# print('Jaccard Similarity = {0}%'.format(jaccard))

# """ Cosine Method """
# cosine = plagiat.periksa("Aku sedang belajar kecerdasan buatan", "Mahasiswa yang cerdas selalu siap menerima tantangan", text=True, method='Cosine').hitung()
# print('Cosine Similarity = {0}%'.format(cosine))