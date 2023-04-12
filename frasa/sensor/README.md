Indonesia Profanity

Terinspirasi dari [profanity](https://github.com/ben174/profanity) milik [Ben Friedland](https://github.com/ben174), namun pada prosesnya saya lebih menggunakan perbandingan antar string daripada menggunakan regex.

Pustaka ini juga mendukung kata alay (maaf) seperti k0ntol, m3MeK, aNJ!nk dan lain-lain.

### Instalasi

```
pip install frasa
```

### Cara Penggunaan
```
from frasa import sensor
if __name__ == "__main__":
    sensor.badword()

    text = "Dasar Anj!ng kau, baj1n94n."
    censored_text = sensor.beep(text)
    print(censored_text)
    # Dasar ****** kau, ********.
```

