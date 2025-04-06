#!/usr/bin/env python3
import pygame
import sys

#Pygame initialisieren
pygame.init()

#Bildschirmgröße festlegen
bildschirm = pygame.display.set_mode((800, 600))

#Flugzeug-Klasse definieren
class Flugzeug:
    def __init__(self):
        self.x = 100
        self.y = 100
        self.geschwindigkeit = 5

    def bewegen(self):
        self.x += self.geschwindigkeit

    def zeichnen(self):
        pygame.draw.rect(bildschirm, (255, 0, 0), (self.x, self.y, 50, 50))

#Hindernis-Klasse definieren
class Hindernis:
    def __init__(self):
        self.x = 700
        self.y = 300
        self.geschwindigkeit = -5

    def bewegen(self):
        self.x += self.geschwindigkeit

    def zeichnen(self):
        pygame.draw.rect(bildschirm, (0, 0, 255), (self.x, self.y, 50, 50))

#Spiel-Loop
while True:
    for ereignis in pygame.event.get():
        if ereignis.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Bildschirm löschen
    bildschirm.fill((0, 0, 0))

    # Flugzeug und Hindernis zeichnen
    flugzeug = Flugzeug()
    hindernis = Hindernis()
    flugzeug.zeichnen()
    hindernis.zeichnen()

    # Flugzeug und Hindernis bewegen
    flugzeug.bewegen()
    hindernis.bewegen()

    # Kollision überprüfen
    if (flugzeug.x + 50 > hindernis.x and
        flugzeug.x < hindernis.x + 50 and
        flugzeug.y + 50 > hindernis.y and
        flugzeug.y < hindernis.y + 50):
        print("Kollision!")

    # Bildschirm aktualisieren
    pygame.display.flip()
    pygame.time.Clock().tick(60)