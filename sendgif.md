Great! Sekarang kita bahas **cara mengirim file `.gif` dan jenis file khusus lainnya** di bot Telegram menggunakan `pyTelegramBotAPI`.

---

## ✅ 1. Cara Kirim File `.gif`

Telegram mendukung `.gif` dalam dua cara:

| Jenis       | Metode             | Keterangan                                         |
| ----------- | ------------------ | -------------------------------------------------- |
| **Animasi** | `send_animation()` | Untuk file `.gif` yang ditampilkan sebagai animasi |
| **Dokumen** | `send_document()`  | Jika ingin mengirim `.gif` sebagai file biasa      |

### 🔸 Kirim `.gif` sebagai animasi

```python
@bot.message_handler(commands=['gif'])
def send_gif(message):
    with open("example.gif", "rb") as gif:
        bot.send_animation(message.chat.id, gif, caption="Ini animasi GIF")
```

### 🔸 Kirim `.gif` sebagai dokumen

```python
@bot.message_handler(commands=['gifdoc'])
def send_gif_document(message):
    with open("example.gif", "rb") as gif:
        bot.send_document(message.chat.id, gif, caption="Ini file GIF sebagai dokumen")
```

---

## ✅ 2. Format-Format Tambahan yang Didukung

| Format File      | Metode Pengiriman  | Catatan                               |
| ---------------- | ------------------ | ------------------------------------- |
| `.gif` (animasi) | `send_animation()` | Ideal untuk GIF bergerak              |
| `.gif` (file)    | `send_document()`  | Jika file tidak ingin diplay otomatis |
| `.zip`, `.rar`   | `send_document()`  | Bisa untuk kirim file arsip           |
| `.txt`, `.csv`   | `send_document()`  | Ideal untuk data, log, dan teks       |
| `.html`, `.xml`  | `send_document()`  | Didukung sebagai file dokumen biasa   |

---

## ✅ Tambahkan ke Bot

Berikut tambahan ke kode bot kamu:

```python
# /gif - Kirim animasi GIF
@bot.message_handler(commands=['gif'])
def send_gif(message):
    with open('example.gif', 'rb') as gif:
        bot.send_animation(message.chat.id, gif, caption="Ini animasi .gif")

# /gifdoc - Kirim GIF sebagai dokumen
@bot.message_handler(commands=['gifdoc'])
def send_gif_as_document(message):
    with open('example.gif', 'rb') as gif:
        bot.send_document(message.chat.id, gif, caption="Ini .gif sebagai dokumen")
```

---

## ✅ Tambahkan ke Menu /start

```python
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message,
        "Halo! Gunakan perintah:\n"
        "/photo - Kirim foto\n"
        "/video - Kirim video\n"
        "/document - Kirim dokumen\n"
        "/audio - Kirim audio\n"
        "/voice - Kirim voice\n"
        "/sticker - Kirim stiker\n"
        "/gif - Kirim animasi gif\n"
        "/gifdoc - Kirim gif sebagai dokumen"
    )
```

---

Kalau kamu juga ingin bot **menerima gif dari pengguna** dan menyimpannya ke folder lokal atau forward ke channel lain, saya bisa bantu tambahkan juga. Mau?
