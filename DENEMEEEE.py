import pygame
import math

# Ekran boyutları
WIDTH, HEIGHT = 800, 600

# Renkler
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
ORANGE = (255, 165, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Gezegen sınıfı
class Planet:
    def __init__(self, distance, angle, radius, speed, color):
        self.distance = distance
        self.angle = angle
        self.radius = radius
        self.speed = speed
        self.color = color
        self.trail = []  # Gezegenin izini tutmak için liste

    def update(self):
        self.angle += self.speed
        self.x = WIDTH // 2 + self.distance * math.cos(math.radians(self.angle))
        self.y = HEIGHT // 2 + self.distance * math.sin(math.radians(self.angle))

        # İzi güncelle
        self.trail.append((self.x, self.y))

    def draw_trail(self, screen):
        for i, point in enumerate(self.trail):
            trail_color = self.color + (int(100 * (i / len(self.trail))),)  # İzin rengini ve opaklığını ayarla
            pygame.draw.circle(screen, trail_color, (int(point[0]), int(point[1])), self.radius // 2, 1)

# Pygame başlat
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Galaksi Simülasyonu")

# Gezegenler oluştur
planets = [
    Planet(200, 0, 19, 1, BLUE),
    Planet(250, 45, 5, 0.7, GREEN),
    Planet(300, 90, 4, 0.5, RED),
    Planet(350, 135, 3, 0.9, ORANGE)
]

# Karadelik oluştur
black_hole_radius = 160
black_hole_x = WIDTH // 2
black_hole_y = HEIGHT // 2

# Ana döngü
clock = pygame.time.Clock()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Ekranı temizle
    screen.fill(BLACK)

    # Karadelik çiz
    pygame.draw.circle(screen, ORANGE, (black_hole_x, black_hole_y), black_hole_radius)

    # Gezegenleri güncelle ve çiz
    for planet in planets:
        planet.update()
        planet.draw_trail(screen)  # İzi çiz
        pygame.draw.circle(screen, planet.color, (int(planet.x), int(planet.y)), planet.radius)

    # Ekranı güncelle
    pygame.display.flip()

    # FPS ayarı
    clock.tick(60)

pygame.quit()
