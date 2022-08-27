import dotenv
import os
from bot import client

dotenv.load_dotenv()
client.run(os.getenv('DISCORD_KEY'))
