Berikut adalah **panduan lengkap penggunaan semua jenis tombol (button) di bot Telegram** menggunakan `pyTelegramBotAPI` (`telebot`) — mulai dari:

1. **Inline Keyboard Button**
2. **Reply Keyboard (markup biasa)**
3. **Remove Keyboard**
4. **Force Reply**
5. **Callback Query (inline tombol interaktif)**

---

## ✅ 1. **Inline Keyboard Button** (dalam pesan)

```python
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

@bot.message_handler(commands=['inline'])
def inline_buttons(message):
    markup = InlineKeyboardMarkup()
    markup.row_width = 2
    markup.add(
        InlineKeyboardButton("Google", url="https://www.google.com"),
        InlineKeyboardButton("Klik Saya", callback_data="button_click")
    )
    bot.send_message(message.chat.id, "Pilih tombol:", reply_markup=markup)
```

---

## ✅ 2. **Reply Keyboard (Keyboard biasa)**

```python
from telebot.types import ReplyKeyboardMarkup, KeyboardButton

@bot.message_handler(commands=['keyboard'])
def reply_keyboard(message):
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.row(
        KeyboardButton("📷 Kirim Foto"),
        KeyboardButton("📄 Kirim Dokumen")
    )
    markup.row(
        KeyboardButton("🎵 Kirim Audio"),
        KeyboardButton("❌ Hapus Keyboard")
    )
    bot.send_message(message.chat.id, "Gunakan tombol berikut:", reply_markup=markup)
```

---

## ✅ 3. **Remove Keyboard** (menghilangkan keyboard)

```python
from telebot.types import ReplyKeyboardRemove

@bot.message_handler(func=lambda message: message.text == "❌ Hapus Keyboard")
def remove_keyboard(message):
    markup = ReplyKeyboardRemove()
    bot.send_message(message.chat.id, "Keyboard dihapus.", reply_markup=markup)
```

---

## ✅ 4. **Force Reply** (paksa user untuk balas pesan)

```python
from telebot.types import ForceReply

@bot.message_handler(commands=['reply'])
def force_reply(message):
    markup = ForceReply(selective=False)
    bot.send_message(message.chat.id, "Silakan balas pesan ini:", reply_markup=markup)

# Tangani balasan user
@bot.message_handler(func=lambda message: message.reply_to_message and message.reply_to_message.text == "Silakan balas pesan ini:")
def reply_received(message):
    bot.send_message(message.chat.id, f"Kamu membalas: {message.text}")
```

---

## ✅ 5. **Callback Query Handler** (respon tombol inline)

Lanjutan dari contoh `InlineKeyboardButton` dengan `callback_data`.

```python
@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    if call.data == "button_click":
        bot.answer_callback_query(call.id, "Tombol diklik!")
        bot.send_message(call.message.chat.id, "Kamu menekan tombol.")
```

---

## 🔁 Contoh `/start` untuk Tes Semua Tombol

```python
@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id,
        "Halo! Coba tombol:\n"
        "/inline - Tombol dalam pesan\n"
        "/keyboard - Keyboard bawah\n"
        "/reply - Balasan wajib\n"
        "/gif - Kirim gif\n"
        "/photo - Kirim foto\n"
        "/video - Kirim video"
    )
```

---

## ✅ Kesimpulan Tipe Tombol

| Tipe Button      | Untuk Apa?                        | Fitur Khusus                 |
| ---------------- | --------------------------------- | ---------------------------- |
| Inline Button    | Tampil di pesan (interaktif)      | Bisa callback, link URL, dll |
| Reply Keyboard   | Tampil di bawah kolom chat        | Untuk navigasi cepat         |
| Remove Keyboard  | Sembunyikan reply keyboard        | Membersihkan layar user      |
| Force Reply      | Minta user membalas pesan         | Untuk input spesifik         |
| Callback Handler | Menangani aksi dari inline button | Interaktif dan dinamis       |

---

Kalau kamu ingin contoh **tombol dinamis** dari database, atau **keyboard berdasarkan kondisi pengguna**, bisa saya bantu juga! Mau lanjut ke sana?
