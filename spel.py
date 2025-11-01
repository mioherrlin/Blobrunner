import pgzrun
import random

WIDTH = 700
HEIGHT = 400

marknivå = HEIGHT - 100

spelare = Actor("spelare", (100,100))
fiende = Actor("fiende", (WIDTH, marknivå))

gravitation = 0.8
hastighet = 0
svårighetsgrad = 8

poäng = 0

game_over = False
spelare_duckar = False

def draw():
    screen.fill((50,0,80))
    spelare.draw()
    fiende.draw()
    screen.draw.text(str(poäng), center=(WIDTH/2, 100), fontsize=40)

def update():
    global game_over
    if not game_over:
        update_spelare()
        update_fiende()
        udate_svårighetsgrad()
    else:
        spelare.image = "spelare_dog"

    # om spelare koliderar med fiende spel slut
    if spelare.colliderect(fiende):
        game_over = True

def udate_svårighetsgrad():
    global svårighetsgrad

    if poäng < 100:
        svårighetsgrad = 8
    elif poäng < 200:   
        svårighetsgrad = 12
    elif poäng < 300:
        svårighetsgrad = 14
    else:
        svårighetsgrad = 16




def update_fiende():
    global poäng
    fiende.x -= svårighetsgrad
    fiende.angle += 1
    if fiende.x < 0:
        fiende.x = WIDTH
        poäng += 10
        fiende.y = random.choice([marknivå, marknivå -40])


def update_spelare():
    global hastighet

    if hastighet > 0:
        spelare.image = "spelare_faller"
    elif hastighet < 0:
        spelare.image = "spelare_hoppar"
    elif spelare_duckar:
        spelare.image = "spelare_duckar"
    else:
        spelare.image = "spelare"

    spelare.y += hastighet
    hastighet += gravitation

    if spelare.y > marknivå:
        hastighet = 0

# tangenten är nedtyckt.
def on_key_down(key):
    global hastighet, spelare_duckar
    if key == keys.SPACE and hastighet == 0 and not spelare_duckar:
        hastighet = -12
    # spelare dukar (och är inte i luften)
    if key == keys.DOWN and hastighet == 0:
        spelare_duckar =True
        spelare.y += 20

def on_key_up(key):
    global spelare_duckar
    if key == keys.DOWN and spelare_duckar:
        spelare_duckar = False
        spelare.y -= 20


pgzrun.go()