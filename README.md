# Telegram Channel Script

This project allows you to forward media files from Bot to Channel using **Channel ID** and bot username.

---

## 🚀 Setup Instructions

### 1️⃣ Find Your Channel ID
1. Open Telegram and search for **@userinfobot**.
2. Start a chat with the bot.
3. Forward a message from your **channel** to the bot, or send `/start`.
4. The bot will respond with your **channel ID** (it usually starts with `-100`).

---

### 2️⃣ Fill in the `.env` Fields
Create a `.env` file in the project root with the following content:

```env
API_ID=your_telegram_api_id
API_HASH=your_telegram_api_hash
BOT_USERNAMES=bot_username_here
TARGET_CHANNEL_ID=-100xxxxxxxxxx
