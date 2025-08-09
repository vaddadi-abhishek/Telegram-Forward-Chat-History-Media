from pyrogram import Client
from dotenv import load_dotenv
import os
import asyncio

load_dotenv()

# Configuration
api_id = int(os.getenv("API_ID"))
api_hash = os.getenv("API_HASH")
bot_usernames = [u.strip().lower() for u in os.getenv("BOT_USERNAMES").split(",")]
target_channel = os.getenv("TARGET_CHANNEL_ID")

app = Client("media_forwarder", api_id=api_id, api_hash=api_hash)

print("✅ Configuration loaded successfully!")
print(f"👀 Bots to fetch from: {bot_usernames}")
print(f"🎯 Target channel: {target_channel}")

async def get_total_count(bot_username):
    """Count total media files accurately"""
    total = 0
    async for message in app.get_chat_history(bot_username):
        if message.photo or message.video or message.document:
            total += 1
    return total

async def forward_oldest_first(bot_username):
    print(f"\n🔍 Counting ALL media in @{bot_username}...")
    total = await get_total_count(bot_username)
    print(f"📊 Found {total} media files (photos + videos + documents)")

    print("⏳ Fetching ALL messages (this may take a while)...")
    all_messages = []
    async for message in app.get_chat_history(bot_username):
        if message.photo or message.video or message.document:
            all_messages.append(message)
    
    print("🔄 Reversing to process oldest first...")
    all_messages.reverse()  # Now oldest first
    
    print(f"🚀 Starting to forward {len(all_messages)} media files...")
    for idx, message in enumerate(all_messages, 1):
        try:
            await message.copy(target_channel)
            print(f"✅ [{idx}/{total}] Forwarded (ID: {message.id}) {'📷' if message.photo else '🎥' if message.video else '📄'}")
            await asyncio.sleep(1.5)  # Safer delay
        except Exception as e:
            print(f"❌ Failed to forward (ID: {message.id}): {e}")
    
    print(f"🎉 Finished forwarding from @{bot_username}")

async def main():
    async with app:
        # Verify target channel access
        try:
            chat = await app.get_chat(target_channel)
            print(f"\n🔗 Connected to channel: {chat.title} (ID: {chat.id})")
        except Exception as e:
            print(f"\n🚫 FATAL: Can't access channel: {e}")
            return

        # Process each bot
        for bot in bot_usernames:
            try:
                print(f"\n🔄 Initializing @{bot}...")
                await app.send_message(bot, "/start")
                await forward_oldest_first(bot)
            except Exception as e:
                print(f"⚠️ Error with @{bot}: {e}")

if __name__ == "__main__":
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    try:
        loop.run_until_complete(main())
    except KeyboardInterrupt:
        print("\n🛑 Script stopped by user")
    except Exception as e:
        print(f"💥 CRASHED: {e}")
    finally:
        loop.close()