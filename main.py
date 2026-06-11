import time
import strings
from player import Player
from text import slow_print, clear, clear_screen

options = {
    "Inventar": True,
    "Umgebung": True,
    "Shop": False,
    "Weiter reisen": True,
}

## Start ##
# Einleitung und Namenswahl

strings.intro()

strings.game_start()

print(" - ".join(key for key in options if options[key] is True))
