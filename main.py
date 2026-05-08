import pygame
import sys

from src.deck import Deck

pygame.init()

WIDTH = 1280
HEIGHT = 720

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("UNO No Mercy")

clock = pygame.time.Clock()

# Colores
BACKGROUND = (120, 0, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (40, 40, 40)

font = pygame.font.SysFont("arial", 30)

deck = Deck()

player_hand = []

for i in range(7):
    player_hand.append(deck.draw_card())

center_card = deck.draw_card()

running = True

while running:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

    # Fondo
    screen.fill(BACKGROUND)

    # Título
    title = font.render("UNO NO MERCY", True, WHITE)
    screen.blit(title, (20, 20))

    # Zona central
    pygame.draw.circle(screen, (180, 120, 0), (640, 360), 130, 12)

    # Carta central
    # Colores UNO
    color_map = {
        "Red": (220, 50, 50),
        "Blue": (50, 80, 220),
        "Green": (50, 180, 80),
        "Yellow": (240, 210, 50)
    }

    center_color = color_map[center_card.color]

    # Carta central
    pygame.draw.rect(
        screen,
        center_color,
        (590, 285, 100, 150),
        border_radius=10
    )

    pygame.draw.rect(
        screen,
        WHITE,
        (590, 285, 100, 150),
        3,
        border_radius=10
    )

    center_text = font.render(
        f"{center_card.value}",
        True,
        WHITE
    )

    screen.blit(center_text, (632, 340))

    # Mazo
    pygame.draw.rect(screen, BLACK, (280, 150, 100, 150), border_radius=10)

    deck_text = font.render("UNO", True, WHITE)
    screen.blit(deck_text, (300, 210))

    # Jugadores IA
    bot1 = font.render("BOT 1", True, WHITE)
    bot2 = font.render("BOT 2", True, WHITE)
    bot3 = font.render("BOT 3", True, WHITE)

    screen.blit(bot1, (80, 300))
    screen.blit(bot2, (580, 80))
    screen.blit(bot3, (1080, 300))

    # Cartas del jugador
    x = 300

    for card in player_hand:

        # Color según carta
        color_map = {
            "Red": (220, 50, 50),
            "Blue": (50, 80, 220),
            "Green": (50, 180, 80),
            "Yellow": (240, 210, 50)
        }

        card_color = color_map[card.color]

        pygame.draw.rect(
            screen,
            card_color,
            (x, 520, 90, 140),
            border_radius=12
        )

        pygame.draw.rect(
            screen,
            WHITE,
            (x, 520, 90, 140),
            3,
            border_radius=12
        )

        value_text = font.render(card.value, True, WHITE)

        screen.blit(value_text, (x + 40, 575))

        x += 95

    pygame.display.update()

    clock.tick(60)

pygame.quit()
sys.exit()