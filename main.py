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
bot1_hand = []
bot2_hand = []
bot3_hand = []

for i in range(7):
    
    player_hand.append(deck.draw_card())
    bot1_hand.append(deck.draw_card())
    bot2_hand.append(deck.draw_card())
    bot3_hand.append(deck.draw_card())

center_card = deck.draw_card()
current_turn = 0
bot_timer = 0
winner = None

running = True

while running:

    for event in pygame.event.get():
    
        if event.type == pygame.QUIT:
            running = False

        # Click del mouse
        if event.type == pygame.MOUSEBUTTONDOWN and current_turn == 0:

            mouse_pos = pygame.mouse.get_pos()
            
            # Click en el mazo
            if deck_rect.collidepoint(mouse_pos):

                if len(deck.cards) > 0:

                    player_hand.append(
                        deck.draw_card()
                    )
                    current_turn = 1

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

                        player_hand.remove(card)

                        # Verificar victoria
                        if len(player_hand) == 0:
                            winner = "PLAYER"

                        else:
                            # Pasar turno al BOT 1
                            current_turn = 1

                        break
    # Turnos de bots
    if current_turn != 0 and winner is None:

        bot_timer += 1

        # Esperar un poco antes de jugar
        if bot_timer >= 60:

            # Elegir mano según turno
            if current_turn == 1:
                current_hand = bot1_hand

            elif current_turn == 2:
                current_hand = bot2_hand

            else:
                current_hand = bot3_hand

            played = False

            # Buscar carta válida
            for card in current_hand:

                if (
                    card.color == center_card.color
                    or
                    card.value == center_card.value
                ):

                    center_card = card

                    current_hand.remove(card)

                    # Verificar victoria bot
                    if len(current_hand) == 0:

                        if current_turn == 1:
                            winner = "BOT 1"

                        elif current_turn == 2:
                            winner = "BOT 2"

                        else:
                            winner = "BOT 3"

                    played = True

                    break

            # Si no tiene carta válida, roba
            if not played:

                if len(deck.cards) > 0:

                    current_hand.append(
                        deck.draw_card()
                    )

            # Siguiente turno
            current_turn += 1

            if current_turn > 3:
                current_turn = 0

            # Reiniciar timer
            bot_timer = 0                
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

    # Colores según turno
    bot1_color = WHITE
    bot2_color = WHITE
    bot3_color = WHITE

    if current_turn == 1:
        bot1_color = (255, 220, 0)

    elif current_turn == 2:
        bot2_color = (255, 220, 0)

    elif current_turn == 3:
        bot3_color = (255, 220, 0)

    # Jugadores IA
    bot1 = font.render("BOT 1", True, bot1_color)
    bot2 = font.render("BOT 2", True, bot2_color)
    bot3 = font.render("BOT 3", True, bot3_color)

    screen.blit(bot1, (50, 300))
    screen.blit(bot2, (800, 80))
    screen.blit(bot3, (1160, 300))
    
    # Cartas BOT 2
    x_bot2 = 450

    for card in bot2_hand:

        pygame.draw.rect(
            screen,
            BLACK,
            (x_bot2, 40, 60, 90),
            border_radius=10
        )

        pygame.draw.rect(
            screen,
            WHITE,
            (x_bot2, 40, 60, 90),
            2,
            border_radius=10
        )

        x_bot2 += 35
    
    # Cartas BOT 1
    y_bot1 = 220

    for card in bot1_hand:

        pygame.draw.rect(
            screen,
            BLACK,
            (150, y_bot1, 60, 90),
            border_radius=10
        )

        pygame.draw.rect(
            screen,
            WHITE,
            (150, y_bot1, 60, 90),
            2,
            border_radius=10
        )

        y_bot1 += 25
        
    # Cartas BOT 3
    y_bot3 = 220

    for card in bot3_hand:

        pygame.draw.rect(
            screen,
            BLACK,
            (1050, y_bot3, 60, 90),
            border_radius=10
        )

        pygame.draw.rect(
            screen,
            WHITE,
            (1050, y_bot3, 60, 90),
            2,
            border_radius=10
        )

        y_bot3 += 25

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
    
    # Mostrar ganador
    if winner is not None:

        winner_text = font.render(
            f"{winner} WINS!",
            True,
            WHITE
        )

        screen.blit(winner_text, (560, 180))

    pygame.display.update()

    clock.tick(60)

pygame.quit()
sys.exit()