#!/usr/bin/env python3
import pygame
import sys

# Konstanten definieren
BILDSCHIRM_BREITE = 800
BILDSCHIRM_HOEHE = 600
OBJEKT_GROESSE = 50
HINTERGRUND_FARBE = (0, 0, 0)
FPS = 30

# Pygame initialisieren
pygame.init()

# Bildschirmgröße festlegen
bildschirm = pygame.display.set_mode((BILDSCHIRM_BREITE, BILDSCHIRM_HOEHE))

# Flugzeug-Klasse definieren
class Flugzeug:
    def __init__(self):
        self.x = 100
        self.y = 100
        self.geschwindigkeit = 5
        self.farbe = (255, 0, 0)  # Rot

    def bewegen(self, richtung):
        if richtung == "hoch" and self.y > 0:
            self.y -= self.geschwindigkeit
        elif richtung == "runter" and self.y < BILDSCHIRM_HOEHE - OBJEKT_GROESSE:
            self.y += self.geschwindigkeit
        elif richtung == "links" and self.x > 0:
            self.x -= self.geschwindigkeit
        elif richtung == "rechts" and self.x < BILDSCHIRM_BREITE - OBJEKT_GROESSE:
            self.x += self.geschwindigkeit

    def zeichnen(self):
        pygame.draw.rect(bildschirm, self.farbe, (self.x, self.y, OBJEKT_GROESSE, OBJEKT_GROESSE))

# Hindernis-Klasse definieren
class Hindernis:
    def __init__(self):
        self.x = 700
        self.y = 300
        self.geschwindigkeit = -5
        self.farbe = (0, 0, 255)  # Blau

    def bewegen(self):
        self.x += self.geschwindigkeit
        # Hindernis zurücksetzen, wenn es den Bildschirm verlässt
        if self.x < -OBJEKT_GROESSE:
            self.x = BILDSCHIRM_BREITE
            self.y = pygame.randint(0, BILDSCHIRM_HOEHE - OBJEKT_GROESSE)

    def zeichnen(self):
        pygame.draw.rect(bildschirm, self.farbe, (self.x, self.y, OBJEKT_GROESSE, OBJEKT_GROESSE))

# Spieler-Eingaben verarbeiten
def handle_input(flugzeug):
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        flugzeug.bewegen("hoch")
    if keys[pygame.K_DOWN]:
        flugzeug.bewegen("runter")
    if keys[pygame.K_LEFT]:
        flugzeug.bewegen("links")
    if keys[pygame.K_RIGHT]:
        flugzeug.bewegen("rechts")

# Kollision überprüfen
def prüfe_kollision(flugzeug, hindernis):
    if (flugzeug.x + OBJEKT_GROESSE > hindernis.x and
        flugzeug.x < hindernis.x + OBJEKT_GROESSE and
        flugzeug.y + OBJEKT_GROESSE > hindernis.y and
        flugzeug.y < hindernis.y + OBJEKT_GROESSE):
        print("Kollision!")
        pygame.quit()
        sys.exit()

# Hauptspiel-Funktion
def main():
    # Flugzeug und Hindernis erstellen
    flugzeug = Flugzeug()
    hindernis = Hindernis()

    # Spiel-Loop
    clock = pygame.time.Clock()
    while True:
        for ereignis in pygame.event.get():
            if ereignis.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Spieler-Eingaben verarbeiten
        handle_input(flugzeug)

        # Bildschirm löschen
        bildschirm.fill(HINTERGRUND_FARBE)

        # Objekte zeichnen
        flugzeug.zeichnen()
        hindernis.zeichnen()

        # Objekte bewegen
        hindernis.bewegen()

        # Kollision überprüfen
        prüfe_kollision(flugzeug, hindernis)

        # Bildschirm aktualisieren
        pygame.display.flip()
        clock.tick(FPS)

# Spiel starten
if __name__ == "__main__":
    main()