from dotenv import dotenv_values
from pushbullet import PushBullet

TOKEN = dotenv_values()['TOKEN']

pb = PushBullet(TOKEN)