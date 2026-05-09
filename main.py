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

        # Click del mouse
        if event.type == pygame.MOUSEBUTTONDOWN:

            mouse_pos = pygame.mouse.get_pos()
            
            # Click en el mazo
            if deck_rect.collidepoint(mouse_pos):

                if len(deck.cards) > 0:

                    player_hand.append(
                        deck.draw_card()
                    )

            # Revisar cartas del jugador
            for card in player_hand:

                # Detectar click sobre carta
                if card.rect.collidepoint(mouse_pos):

                    # Validar jugada
                    if (
                        card.color == center_card.color
                        or
                        card.value == center_card.value
                    ):

                        # Cambiar carta central
                        center_card = card

                        # Eliminar carta jugada
                        player_hand.remove(card)

                        break

    # Fondo
    screen.fill(BACKGROUND)

    # Título
    title = font.render("UNO NO MERCY", True, WHITE)
    screen.blit(title, (20, 20))

    # Zona central
    pygame.draw.circle(screen, (180, 120, 0), (640, 360), 130, 12)

    # Carta central
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
    deck_rect = pygame.Rect(280, 150, 100, 150)

    pygame.draw.rect(
        screen,
        BLACK,
        deck_rect,
        border_radius=10
    )

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
        card.x = x
        card.y = 520

        card.update_rect()

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
    
    # Botón UNO
    pygame.draw.circle(
        screen,
        (220, 40, 40),
        (1180, 620),
        45
    )

    pygame.draw.circle(
        screen,
        WHITE,
        (1180, 620),
        45,
        4
    )

    uno_text = font.render("UNO", True, WHITE)

    screen.blit(uno_text, (1153, 603))

    pygame.display.update()

    clock.tick(60)

pygame.quit()
sys.exit()