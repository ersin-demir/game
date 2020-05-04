import pygame
import sys
import random

pygame.init()
clock = pygame.time.Clock()


class game_vars:

    top_hız_x = 7 * random.choice((1, -1))
    top_hız_y = 7 * random.choice((1, -1))
    oyuncu_skor = 0
    rakip_skor = 0


def top_hareketleri():

    top.x += game_vars.top_hız_x
    top.y += game_vars.top_hız_y

    if top.top <= 0 or top.bottom >= screen_height:
        game_vars.top_hız_y *= -1

    if top.left <= 0:
        game_vars.oyuncu_skor += 1
        top_yeniden_başlat()

    if top.right >= screen_width:
        game_vars.rakip_skor += 1
        top_yeniden_başlat()

    # çarpışma durumu
    if top.colliderect(oyuncu) or top.colliderect(rakip):
        game_vars.top_hız_x *= -1


def oyuncu_hareketleri():
    oyuncu.y += oyuncu_hız
    if oyuncu.top <= 0:
        oyuncu.top = 0
    if oyuncu.bottom >= screen_height:
        oyuncu.bottom = screen_height


def rakip_hareketleri():
    if top.x < screen_width/2 and rakip.bottom < top.y:
        rakip.top += rakip_hız
    if top.x < screen_width/2 and rakip.top > top.y:
        rakip.top -= rakip_hız
    if rakip.top <= 0:
        rakip.top = 0
    if rakip.bottom >= screen_height:
        rakip.bottom = screen_height


def top_yeniden_başlat():  # top ekrandan çıkınca merkezden tekrar başlatıyor

    top.center = (int(screen_width/2), int(screen_height/2))
    game_vars.top_hız_x *= random.choice((1, -1))
    game_vars.top_hız_y *= random.choice((1, -1))


# oyun ekranının ölçüleri (siyah ekran)
screen_width = 1000
screen_height = 500
screen = pygame.display.set_mode((screen_width, screen_height))

# ekranın üstünde gösterilen isim
pygame.display.set_caption("pong game")

# oyundaki dikdörtgenler
top = pygame.Rect(int(screen_width/2 - 10), int(screen_height/2 - 10), 20, 20)
oyuncu = pygame.Rect(int(screen_width - 20), int(screen_height/2 - 50), 5, 100)
rakip = pygame.Rect(10, int(screen_height/2 - 50), 5, 100)

# renkler
bg_color = pygame.Color('grey12')
açık_gri = (200, 200, 200)

oyuncu_hız = 0
rakip_hız = 9

# Text variable'ları
oyun_font = pygame.font.Font("freesansbold.ttf", 20)

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:   # Pencereyi kapatınca oyunu bitiriyor
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:   # ESC'ye basıldığında oyunu bitiriyor
                sys.exit()
            if event.key == pygame.K_DOWN:
                oyuncu_hız += 7
            if event.key == pygame.K_UP:
                oyuncu_hız -= 7
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_DOWN:
                oyuncu_hız -= 7
            if event.key == pygame.K_UP:
                oyuncu_hız += 7

    top_hareketleri()
    oyuncu_hareketleri()
    rakip_hareketleri()

    # görseller
    screen.fill(bg_color)
    pygame.draw.rect(screen, açık_gri, oyuncu)
    pygame.draw.rect(screen, açık_gri, rakip)
    pygame.draw.ellipse(screen, açık_gri, top)
    pygame.draw.aaline(screen, açık_gri, (screen_width/2, 0), (screen_width/2, screen_height))

    oyuncu_text = oyun_font.render(f"{game_vars.oyuncu_skor}", False, açık_gri)
    screen.blit(oyuncu_text, (510, 10))

    rakip_text = oyun_font.render(f"{game_vars.rakip_skor}", False, açık_gri)
    screen.blit(rakip_text, (480, 10))


    pygame.display.flip()
    clock.tick(60)

