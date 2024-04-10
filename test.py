import random
pomaganie_srodowisku = ["pojdź do parku i pozbieraj smieci!", "segreguj śmieci!", "staraj się nie używać jednorazowych woreczków!"]

def losuj_pomysl():
    pomysly_lista = ["pojdź do parku i pozbieraj smieci!", "segreguj śmieci!"]
    wybrany_pomysl = random.choice(pomysly_lista)
    return wybrany_pomysl
