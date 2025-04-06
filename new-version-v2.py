#!/usr/bin/env python3
import pygame
import sys

#Pygame initialisieren
pygame.init()

#Bildschirmgröße festlegen
bildschirm = pygame.display.set_mode((800, 600))

# Flugzeug-Klasse definieren
class Flugzeug:
    def __init__(self):
        self.x = 100
        self.y = 100
        self.geschwindigkeit = 5
        self.richtung = "rechts"  # Start moving to the right

    def bewegen(self):
        # Move along a predefined path
        if self.richtung == "rechts":
            self.x += self.geschwindigkeit
            if self.x > 700:  # Change direction when reaching the screen edge
                self.richtung = "unten"
        elif self.richtung == "unten":
            self.y += self.geschwindigkeit
            if self.y > 500:
                self.richtung = "links"
        elif self.richtung == "links":
            self.x -= self.geschwindigkeit
            if self.x < 100:
                self.richtung = "oben"
        elif self.richtung == "oben":
            self.y -= self.geschwindigkeit
            if self.y < 100:
                self.richtung = "rechts"

    def zeichnen(self):
        pygame.draw.rect(bildschirm, (255, 0, 0), (self.x, self.y, 50, 50))

# Hindernis-Klasse definieren
class Hindernis:
    def __init__(self, flugzeug):
        self.flugzeug = flugzeug
        self.x = flugzeug.x - 200  # Start farther away to avoid immediate collision
        self.y = flugzeug.y
        self.geschwindigkeit = 2.5  # Slower speed to follow the Flugzeug

    def bewegen(self):
        # Move towards the Flugzeug's position
        if self.x < self.flugzeug.x:
            self.x += self.geschwindigkeit
        elif self.x > self.flugzeug.x:
            self.x -= self.geschwindigkeit

        if self.y < self.flugzeug.y:
            self.y += self.geschwindigkeit
        elif self.y > self.flugzeug.y:
            self.y -= self.geschwindigkeit

    def zeichnen(self):
        pygame.draw.rect(bildschirm, (0, 0, 255), (self.x, self.y, 50, 50))

# Spieler-Eingaben verarbeiten
def handle_input(flugzeug):
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        flugzeug.y -= flugzeug.geschwindigkeit
    if keys[pygame.K_DOWN]:
        flugzeug.y += flugzeug.geschwindigkeit
    if keys[pygame.K_LEFT]:
        flugzeug.x -= flugzeug.geschwindigkeit
    if keys[pygame.K_RIGHT]:
        flugzeug.x += flugzeug.geschwindigkeit

#Spiel-Loop
flugzeug = Flugzeug()
hindernis = Hindernis(flugzeug)

while True:
    for ereignis in pygame.event.get():
        if ereignis.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Spieler-Eingaben verarbeiten
    handle_input(flugzeug)

    # Bildschirm löschen
    bildschirm.fill((0, 0, 0))

    # Flugzeug und Hindernis zeichnen
    flugzeug.zeichnen()
    hindernis.zeichnen()

    # Flugzeug und Hindernis bewegen
    hindernis.bewegen()

    # Kollision überprüfen
    if (flugzeug.x + 50 > hindernis.x and
        flugzeug.x < hindernis.x + 50 and
        flugzeug.y + 50 > hindernis.y and
        flugzeug.y < hindernis.y + 50):
        print("Kollision! Spiel vorbei!")
        pygame.quit()
        sys.exit()

    # Bildschirm aktualisieren
    pygame.display.flip()
    pygame.time.Clock().tick(60)