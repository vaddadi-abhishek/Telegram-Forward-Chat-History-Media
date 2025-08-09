# Telegram Channel Script

This project allows you to forward media files from Bot to Channel using **Channel ID** and bot username.

---

## 📌 Steps to Create a Telegram Developer App (MTProto API)

### 1️⃣ Sign in to Telegram's Developer Portal
1. Go to: my.telegram.org
2. Log in using your phone number
3. You’ll get a login code in your Telegram app — enter it.

### 2️⃣ Create a New Application
1. Once logged in, click "API Development Tools".
2. Fill in the form:
3. App title → Any name (e.g., MyChannelBot).
   Short name → A short identifier (e.g., channelbot).
   Platform → Choose Desktop or Other (doesn’t matter much here).
   Description → your app description.
4. Click Create application.

## 🚀 Telegram Setup

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
