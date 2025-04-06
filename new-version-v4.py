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

# ...existing code...

import math  # Import math for angle calculations

# Hindernis-Klasse definieren
class Hindernis:
    def __init__(self, flugzeug):
        self.flugzeug = flugzeug
        self.x = flugzeug.x - 100  # Start farther away to avoid immediate collision
        self.y = flugzeug.y
        self.geschwindigkeit = 2  # Base speed for following
        self.inertia = 0.1  # Inertia factor (0 < inertia <= 1)
        self.angle = 0  # Angle of the triangle (in degrees)

    def bewegen(self):
        # Gradually move towards the Flugzeug's position with inertia and speed limit
        dx = self.flugzeug.x - self.x
        dy = self.flugzeug.y - self.y

        # Calculate the distance to the Flugzeug
        distance = (dx**2 + dy**2)**0.5

        # Normalize the direction vector and scale by geschwindigkeit
        if distance > 0:
            move_x = (dx / distance) * min(self.geschwindigkeit, distance)
            move_y = (dy / distance) * min(self.geschwindigkeit, distance)

            # Apply inertia to smooth the movement
            self.x += move_x * self.inertia
            self.y += move_y * self.inertia

            # Calculate the angle of movement (in radians) and convert to degrees
            self.angle = math.degrees(math.atan2(dy, dx))

    def zeichnen(self):
        # Calculate the points of the triangle based on the angle
        size = 30  # Size of the triangle
        half_base = size / 2

        # Calculate the triangle's points
        point1 = (self.x + math.cos(math.radians(self.angle)) * size,
                  self.y + math.sin(math.radians(self.angle)) * size)
        point2 = (self.x + math.cos(math.radians(self.angle + 120)) * half_base,
                  self.y + math.sin(math.radians(self.angle + 120)) * half_base)
        point3 = (self.x + math.cos(math.radians(self.angle - 120)) * half_base,
                  self.y + math.sin(math.radians(self.angle - 120)) * half_base)

        # Draw the triangle
        pygame.draw.polygon(bildschirm, (0, 0, 255), [point1, point2, point3])

# ...existing code...

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