Untuk membuat bot Telegram yang **interaktif, fleksibel**, dan bisa membaca & merespons pesan masuk (baik dari **chat pribadi, grup**, maupun **channel**), serta **mencetak isi pesan di terminal (console)**, kamu bisa mengikuti panduan lengkap berikut.

---

## ✅ FITUR-FITUR YANG AKAN DIBUAT:

1. 📥 **Membaca semua pesan masuk**
2. 📦 **Mencetak isi pesan ke terminal (console)**
3. 👥 **Membedakan jenis chat (grup, channel, atau private)**
4. 💬 **Merespons otomatis sesuai jenis pesan**
5. 🛡️ **Membatasi siapa yang bisa gunakan bot (opsional)**

---

## ✅ 1. **Setup Dasar Bot**

```bash
pip install pyTelegramBotAPI
```

---

## ✅ 2. **Script Lengkap Interaktif Bot**

```python
import telebot

TOKEN = 'YOUR_BOT_TOKEN'  # Ganti dengan token bot kamu
bot = telebot.TeleBot(TOKEN)

# Fungsi utama menangani SEMUA pesan masuk
@bot.message_handler(func=lambda message: True)
def handle_all_messages(message):
    chat_type = message.chat.type  # private, group, supergroup, channel
    sender_name = message.from_user.first_name
    message_text = message.text

    # Cetak ke terminal
    print("==== PESAN MASUK ====")
    print(f"Dari: {sender_name}")
    print(f"Chat Type: {chat_type}")
    print(f"Isi Pesan: {message_text}")
    print("=====================\n")

    # Respon berdasarkan tipe chat
    if chat_type == "private":
        bot.reply_to(message, f"Hai {sender_name}! Ini chat pribadi.")
    elif chat_type in ["group", "supergroup"]:
        bot.send_message(message.chat.id, f"Hai semua! {sender_name} kirim: {message_text}")
    elif chat_type == "channel":
        bot.send_message(message.chat.id, f"Pesan diterima dari channel.")

# Jalankan bot
print("Bot sedang berjalan...")
bot.infinity_polling()
```

---

## ✅ 3. **Respon Khusus Berdasarkan Kata Kunci**

Contoh: tanggapi pesan tertentu

```python
@bot.message_handler(func=lambda m: m.text and "halo" in m.text.lower())
def greeting_reply(message):
    bot.reply_to(message, "Halo juga! Ada yang bisa dibantu?")
```

---

## ✅ 4. **Membatasi Akses Bot (Opsional)**

Jika hanya ingin bot merespons ID tertentu:

```python
ALLOWED_USERS = [123456789]  # Ganti dengan user ID Telegram kamu

@bot.message_handler(func=lambda message: message.from_user.id in ALLOWED_USERS)
def restricted_access(message):
    bot.reply_to(message, "Halo admin, perintahmu diterima.")
```

---

## ✅ 5. **Tambahan Info Pesan yang Bisa Dibaca**

```python
print(f"Username: @{message.from_user.username}")
print(f"User ID: {message.from_user.id}")
print(f"Message ID: {message.message_id}")
print(f"Date (Unix): {message.date}")
print(f"Has Media: {'Yes' if message.content_type != 'text' else 'No'}")
```

---

## ✅ 6. **Mendeteksi Media, Lokasi, Stiker, dll**

```python
@bot.message_handler(content_types=['photo', 'video', 'sticker', 'location', 'document'])
def handle_media(message):
    print(f"[{message.content_type.upper()}] diterima dari {message.from_user.first_name}")
    bot.reply_to(message, f"Saya menerima {message.content_type} kamu!")
```

---

## ✅ 7. **Menangani Pesan di Grup**

Telegram tidak akan mengirim semua pesan ke bot dalam grup **kecuali**:

* Bot dijadikan **admin**
* **Privasi bot dimatikan**:
  Pergi ke [@BotFather](https://t.me/BotFather) → /mybots → pilih bot kamu → **Group Privacy** → **Turn OFF**

---

## 🔁 Bot Bisa Berjalan Selamanya

Gunakan:

```python
bot.infinity_polling()  # Auto-reconnect jika terputus
```

---

## ✅ BONUS: Mengetahui ID Chat

Untuk tahu `chat.id` atau `user.id`, gunakan ini:

```python
@bot.message_handler(commands=['id'])
def get_chat_id(message):
    bot.reply_to(message, f"ID chat ini: `{message.chat.id}`", parse_mode='Markdown')
```

---

## 🔚 KESIMPULAN

Dengan script ini kamu bisa:

✅ Melihat pesan apapun di terminal
✅ Merespons otomatis berdasarkan isi & jenis chat
✅ Mengatur hak akses pengguna
✅ Menangani grup, channel, atau chat pribadi
✅ Menangani berbagai jenis media

---

Kalau kamu ingin bot ini **mencatat pesan ke file log, database, atau forward otomatis ke channel lain**, tinggal bilang — saya bantu modifikasinya. Mau lanjut ke arah itu?
