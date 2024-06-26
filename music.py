import telegram
import spotipy 
from spotipy.oauth2 import SpotifyClientCredentials 

# Replace with your actual credentials
SPOTIFY_CLIENT_ID = 'bcfe26b0ebc3428882a0b5fb3e872473'
SPOTIFY_CLIENT_SECRET = '907c6a054c214005aeae1fd752273cc4'
TELEGRAM_BOT_TOKEN = '6459647682:AAGX4P4aozvOj9zBwzYNO3_-DDBeT_ejeIY'

# Authentication with Spotify
auth_manager = SpotifyClientCredentials(client_id=SPOTIFY_CLIENT_ID, client_secret=SPOTIFY_CLIENT_SECRET)
sp = spotipy.Spotify(auth_manager=auth_manager)

# Initialize Telegram bot
bot = telegram.Bot(token=TELEGRAM_BOT_TOKEN)

def handle_message(update, context):
    user_text = update.message.text

    if user_text.startswith('/search'):
        query = user_text[8:]  # Extract the search term
        results = sp.search(q=query, type='track')

        # Present search results to the user (you'll need to format this nicely)
        bot.send_message(chat_id=update.message.chat_id, text="Search Results:")
        for track in results['tracks']['items']:
            bot.send_message(chat_id=update.message.chat_id, text=f"{track['name']} - {track['artists'][0]['name']}")

    # .... (Add more message handlers for download functionality or alternatives) 

# Start the bot
if __name__ == '__main__':
    updater = telegram.Updater(token=TELEGRAM_BOT_TOKEN, use_context=True)
    dispatcher = updater.dispatcher

    message_handler = telegram.MessageHandler(telegram.Filters.text & (~telegram.Filters.command), handle_message)
    dispatcher.add_handler(message_handler)

    updater.start_polling()
    updater.idle()
      
