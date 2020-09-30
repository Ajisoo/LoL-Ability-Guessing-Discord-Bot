from datetime import datetime
import os



BOT_PREFIX = "$"

BOT_KEY_FILE = "bot.key"

BIRTHDAYS = {225822313550053376: [3, 14],
			 167090536602140682: [7, 21],
			 191597928090042369: [8, 3],
			 193550776340185088: [11, 20],
			 363197965306953730: [9, 2],
			 182707904367820800: [11, 2],
			 190253188262133761: [4, 17],
			 285290000395010048: [7, 30],
			 377691228977889283: [2, 17]}


PATCH_MESSAGE_HEADER = "🎉 New patch today 🎉\n"

PATCH_MESSAGE = "Added $bm for when you die first in Among Us"

PATCH_DAY = datetime(2020, 9, 17)

HELP_DEFAULT_MESSAGE = "😠 no help for you! 😠"

# Folder names are relative to the location of bot.py, so if anything gets moved around make sure to update these

CONTENT_FOLDER = "content" + os.path.sep

GA_BASE_WEBSITE = "https://www.mobafire.com"
GA_WEBSITE = GA_BASE_WEBSITE + "/league-of-legends/abilities"

GA_FOLDER = CONTENT_FOLDER + "lol_ability_guesser" + os.path.sep
GA_LEADERBOARD_FILE = GA_FOLDER + "leaderboard.txt"

GS_FOLDER = CONTENT_FOLDER + "lol_splash_guesser" + os.path.sep
GS_LEADERBOARD_FILE = GS_FOLDER + "leaderboard.txt"