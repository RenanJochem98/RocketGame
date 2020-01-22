import pygame
import random

def score_text(score):
    font = pygame.font.Font(None, 30)
    text = font.render('Score '+ str(score) + " - Velocidade: "+str(speed)+"x", 1, BLACK)
    return text

def update_position(match =False):
    global speed, rocket_pos, score
    rocket_pos[0] -= speed

    if (rocket_pos[0] + img_rocket.get_rect().size[0]) <= 0 or match:
        rocket_pos[0] = window_size[0]
        rocket_pos[1] = random.randint(img_rocket.get_rect().size[0],
                                        window_size[1] - img_rocket.get_rect().size[0])
        speed+=1
        if speed > 20:
            speed = 1
        if not match:
            if score > 0:
                score -= 1
#inicializa pygame
pygame.init()

# definw cores RGB
WHITE = (255, 255, 255)
BLACK = (0,0,0)

# tamanho janela
window_size = [800,600]

#inicializa janela
window = pygame.display.set_mode(window_size)

#setar titulo
pygame.display.set_caption("Rocket Game")

#carrega uma imagem
img_rocket = pygame.image.load('rocket.png')

#posicao da imagem
rocket_pos = [window_size[0], random.randint(0, window_size[1])]
speed = 5
score = 0

done = True
rocket = None

while done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if rocket.collidepoint(event.pos):
                score += 1
                update_position(True)
            else:
                if score > 0:
                    score -= 1
    window.fill(WHITE)
    rocket = window.blit(img_rocket, rocket_pos)
    window.blit(score_text(score), (0,0))

    pygame.display.update()
    pygame.time.delay(100)
    update_position()
#endwhile
pygame.quit()
