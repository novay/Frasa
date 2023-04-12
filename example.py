from frasa.sensor import sensor

sensor.badword()

text = "Dasar anj!ng kamu b4j1nGan."
censored_text = sensor.beep(text)
print(censored_text)