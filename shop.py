import random

random_antworten = [
    " seitdem meine Frau laktoseintolerant ist.",
    " seitdem ich hungig bin.",
    " seit Mitte August.",
    " seitdem ich weiß, dass es keine Drachen gibt...",
    " seitdem... seit... Guten Tag junger Abenteurer!\n Wie kann ich behilflich sein?",
    " seitdem Herbert meine Jackpot Bingo Karte gegessen hat.",
    " seitdem Döner mehr als 5 Gold kostet.",
    " seit es gestern regnete.",
    " seit die Antwortsteuer erhöht wurde.",
    ". Aber ich mag Pudding.",
]


def shop(self):
    if self.location != "city":
        print(f"{self.name} ist keine Stadt. Hier gibt es keinen Shop.")
        return
    else:
        print("Guten Tag junger Abenteurer!\n", "Wie kann ich behilflich sein?")
        inp = "Hi"

        while inp != "Verlassen":
            inp = input("Kaufen - Verkaufen - Befragen - Verlassen").lower()

            match inp:

                case "kaufen":
                    print("Was hätten Sie gerne?")
                    pass
                case "verkaufen":
                    print("Was bieten Sie an?")
                    pass
                case "befragen":
                    print(
                        f"Ich beantworte keine Fragen mehr{random.choice(random_antworten)}"
                    )
                case "verlassen":
                    print("Beehren Sie uns bald wieder!")
                case _:
                    print("Ich konnte Sie leider nicht verstehen.")
    pass
