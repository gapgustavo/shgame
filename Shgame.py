import pygame
import sys
import random

# Inicializar o PyGame
pygame.init()

# Definir as dimensões da tela
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Simple Shooter Game")

# Cores
BLUE = (0, 0, 255)
RED = (255, 0, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)

# Definir o relógio
clock = pygame.time.Clock()

# Configurações do jogador
player_width = 50
player_height = 50
player_speed = 5
player_rect = pygame.Rect(SCREEN_WIDTH // 2 - player_width // 2, SCREEN_HEIGHT - player_height - 10, player_width, player_height)
player_life = 100

# Configurações dos inimigos
enemy_width = 50
enemy_height = 50
enemy_speed = 3
enemy_rect = pygame.Rect(SCREEN_WIDTH // 2 - enemy_width // 2, 10, enemy_width, enemy_height)
enemy_life = 100
enemy_bullets = []

# Configurações dos tiros
bullet_width = 5
bullet_height = 10
bullet_speed = 7
player_bullets = []

# Variáveis para controle das teclas pressionadas
keys = pygame.key.get_pressed()
shoot = False  # Controle do disparo

def draw_player():
    """Desenha o jogador e a barra de vida do jogador."""
    pygame.draw.rect(screen, BLUE, player_rect)
    draw_life(player_life, (10, 10), "Player")

def draw_enemy():
    """Desenha o inimigo e a barra de vida do inimigo."""
    pygame.draw.rect(screen, RED, enemy_rect)
    draw_life(enemy_life, (SCREEN_WIDTH - 210, 10), "Enemy")

def draw_bullets():
    """Desenha os tiros do jogador e do inimigo na tela."""
    for bullet in player_bullets:
        pygame.draw.rect(screen, BLACK, bullet)
    for bullet in enemy_bullets:
        pygame.draw.rect(screen, BLACK, bullet)

def update_bullets():
    """Atualiza a posição dos tiros e remove os que saíram da tela."""
    global player_bullets, enemy_bullets
    player_bullets = [bullet.move(0, -bullet_speed) for bullet in player_bullets if bullet.bottom > 0]
    enemy_bullets = [bullet.move(0, bullet_speed) for bullet in enemy_bullets if bullet.top < SCREEN_HEIGHT]

def check_collision():
    """Verifica colisões entre tiros e retângulos do jogador e inimigo."""
    global player_bullets, enemy_bullets, player_life, enemy_life
    for bullet in player_bullets:
        if bullet.colliderect(enemy_rect):
            enemy_life -= 5
            player_bullets.remove(bullet)
            if enemy_life <= 0:
                game_over("Player Wins!")

    for bullet in enemy_bullets:
        if bullet.colliderect(player_rect):
            player_life -= 10
            enemy_bullets.remove(bullet)
            if player_life <= 0:
                game_over("Enemy Wins!")

def draw_life(life, position, label):
    """Desenha a barra de vida e o texto correspondente no canto da tela."""
    font = pygame.font.Font(None, 36)
    life_text = font.render(f"{label} Life: {life}", True, BLACK)
    pygame.draw.rect(screen, GREEN, (position[0], position[1] + 20, life * 2, 20))
    pygame.draw.rect(screen, BLACK, (position[0], position[1] + 20, 200, 20), 2)  # Borda da barra de vida
    screen.blit(life_text, (position[0], position[1]))

def enemy_shoot():
    """Faz o inimigo atirar periodicamente."""
    global enemy_bullets
    if pygame.time.get_ticks() % 30 == 0:  # Ajuste a frequência do disparo
        bullet = pygame.Rect(enemy_rect.centerx - bullet_width // 2, enemy_rect.bottom, bullet_width, bullet_height)
        enemy_bullets.append(bullet)

def move_enemy():
    """Move o inimigo aleatoriamente dentro dos limites da tela."""
    if random.choice([True, False]):
        enemy_rect.x += random.choice([-enemy_speed, enemy_speed])
    if enemy_rect.left < 0:
        enemy_rect.left = 0
    if enemy_rect.right > SCREEN_WIDTH:
        enemy_rect.right = SCREEN_WIDTH

def game_over(message):
    """Exibe a mensagem de fim de jogo e encerra o programa após 2 segundos."""
    font = pygame.font.Font(None, 74)
    text = font.render(message, True, BLACK)
    screen.fill(WHITE)
    screen.blit(text, (SCREEN_WIDTH // 2 - text.get_width() // 2, SCREEN_HEIGHT // 2 - text.get_height() // 2))
    pygame.display.flip()
    pygame.time.wait(2000)  # Espera 2 segundos
    pygame.quit()
    sys.exit()

def draw_button(text, rect, font, screen, button_color, text_color, border_color):
    """Desenha um botão estilizado com borda e texto."""
    pygame.draw.rect(screen, border_color, rect)  # Desenha a borda
    pygame.draw.rect(screen, button_color, rect.inflate(-10, -10))  # Desenha o botão com efeito de borda
    label = font.render(text, True, text_color)
    screen.blit(label, (rect.centerx - label.get_width() // 2, rect.centery - label.get_height() // 2))

def main_menu():
    """Exibe o menu principal com um botão 'Start'."""
    # Definir as cores
    button_color = (100, 150, 255)  # Azul claro
    border_color = (50, 100, 200)   # Azul mais escuro para a borda
    text_color = BLACK  # Cor do texto

    # Fonte para o botão
    font = pygame.font.Font(None, 74)
    button_rect = pygame.Rect(SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT // 2 - 50, 200, 100)

    while True:
        screen.fill(WHITE)  # Cor de fundo branca

        # Desenhar o botão estilizado
        draw_button("Start", button_rect, font, screen, button_color, text_color, border_color)
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if button_rect.collidepoint(event.pos):
                    return

def game_loop():
    """Executa o loop principal do jogo, gerenciando eventos, atualizações e desenhos."""
    global player_life, enemy_life, player_rect, keys, shoot
    while True:
        screen.fill(WHITE)  # Cor de fundo branca
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            player_rect.x -= player_speed
        if keys[pygame.K_RIGHT]:
            player_rect.x += player_speed
        
        if keys[pygame.K_RETURN]:
            if not shoot:
                bullet = pygame.Rect(player_rect.centerx - bullet_width // 2, player_rect.top - bullet_height, bullet_width, bullet_height)
                player_bullets.append(bullet)
                shoot = True
        else:
            shoot = False

        # Atualizar a posição dos tiros
        update_bullets()

        # Mover o inimigo
        move_enemy()

        # Atirar inimigos
        enemy_shoot()

        # Verificar colisões
        check_collision()

        # Desenhar todos os elementos
        draw_player()
        draw_enemy()
        draw_bullets()

        pygame.display.flip()
        clock.tick(30)

if __name__ == "__main__":
    main_menu()
    game_loop()
