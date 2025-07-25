Berikut adalah **contoh lengkap program bot Telegram** menggunakan `pyTelegramBotAPI` (alias `telebot`) untuk **mengirim berbagai jenis file** ke pengguna, termasuk:

1. Gambar (send\_photo)
2. Video (send\_video)
3. Dokumen (send\_document)
4. Audio (send\_audio)
5. Voice (send\_voice)
6. Sticker (send\_sticker)

---

## ✅ PERSIAPAN

### 1. Install Library

```bash
pip install pyTelegramBotAPI
```

### 2. Struktur Folder

Letakkan file media di folder yang sama:

```
bot.py
photo.jpg
video.mp4
document.pdf
audio.mp3
voice.ogg
sticker.webp
```

---

## ✅ CONTOH PROGRAM LENGKAP

```python
import telebot
from telebot import apihelper

# Ganti dengan token bot milikmu
API_TOKEN = 'YOUR_BOT_TOKEN'
bot = telebot.TeleBot(API_TOKEN)

# Optional: atur timeout untuk file besar
apihelper.READ_TIMEOUT = 60
apihelper.CONNECT_TIMEOUT = 20

# /photo - Kirim foto
@bot.message_handler(commands=['photo'])
def send_photo(message):
    with open('photo.jpg', 'rb') as photo:
        bot.send_photo(message.chat.id, photo, caption="Ini foto")

# /video - Kirim video
@bot.message_handler(commands=['video'])
def send_video(message):
    with open('video.mp4', 'rb') as video:
        bot.send_video(message.chat.id, video, caption="Ini video")

# /document - Kirim dokumen
@bot.message_handler(commands=['document'])
def send_document(message):
    with open('document.pdf', 'rb') as doc:
        bot.send_document(message.chat.id, doc, caption="Ini dokumen PDF")

# /audio - Kirim file audio
@bot.message_handler(commands=['audio'])
def send_audio(message):
    with open('audio.mp3', 'rb') as audio:
        bot.send_audio(message.chat.id, audio, caption="Ini audio MP3")

# /voice - Kirim voice message
@bot.message_handler(commands=['voice'])
def send_voice(message):
    with open('voice.ogg', 'rb') as voice:
        bot.send_voice(message.chat.id, voice, caption="Ini voice")

# /sticker - Kirim sticker
@bot.message_handler(commands=['sticker'])
def send_sticker(message):
    with open('sticker.webp', 'rb') as sticker:
        bot.send_sticker(message.chat.id, sticker)

# /start - Perintah awal
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Halo! Gunakan perintah:\n"
                          "/photo - Kirim foto\n"
                          "/video - Kirim video\n"
                          "/document - Kirim dokumen\n"
                          "/audio - Kirim audio\n"
                          "/voice - Kirim voice\n"
                          "/sticker - Kirim stiker")

# Jalankan polling
bot.polling()
```

---

## 🔧 CATATAN FORMAT FILE

| Tipe    | Format yang Didukung         |
| ------- | ---------------------------- |
| Foto    | `.jpg`, `.png`               |
| Video   | `.mp4`                       |
| Dokumen | `.pdf`, `.txt`, `.docx`, dll |
| Audio   | `.mp3`, `.m4a`, `.flac`      |
| Voice   | `.ogg` (opus codec)          |
| Sticker | `.webp`                      |

---

## 📌 Tips Tambahan

* Gunakan file kecil untuk pengujian (<5MB).
* Jika kamu mengalami error `Timeout`, bisa gunakan `send_document()` untuk semua jenis file sebagai alternatif.
* Untuk mengirim file dari URL (tanpa unduh manual), kamu bisa langsung kirim link ke `send_photo`, `send_video`, dll.

---

Kalau kamu ingin ditambahkan fitur upload dari pengguna, atau menyimpan file yang dikirim pengguna, saya juga bisa bantu. Mau lanjut ke arah itu?
