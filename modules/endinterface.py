import sys
import pygame

def showEndInterface(screen, cfg, score, highest_score):
    font_big = pygame.font.Font(cfg.FONT_PATH, 60)
    font_small = pygame.font.Font(cfg.FONT_PATH, 40)
    text_tile = font_big.render(f"Time is up!", True, (255, 0, 0))
    text_tile_rect = text_tile.get_rect()
    text_tile_rect.centerx = screen.get_rect().centerx
    text_tile_rect.centery = screen.get_rect().centery -100
    text_score = font_small.render(f"Score: {score}, Highest Score: {highest_score}", True, (255, 0, 0))

    text_score_rect = text_score.get_rect()
    text_score_rect.centerx = screen.get_rect().centerx
    text_tile_rect.centery = screen.get_rect().centery -10
    text_tip = font_small.render(f"Enter Q to quit game of R to restart it", True, (255, 0, 0))

    text_tip_rect = text_tip.get_rect()
    text_score_rect.centerx = screen.get_rect().centerx
    text_score_rect.centery = screen.get_rect().centery +60
    text_tip_count = 0
    text_tip_freq = 10
    text_tip_show_flag = True

    clock = pygame.time.Clock()

    while True:
        screen.fill(0)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    return False
                elif event.key == pygame.K_r:
                    return True
        
        screen.blit(text_tile, text_tile_rect)
        screen.blit(text_score, text_score_rect)
        if text_tip_show_flag:
            screen.blit(text_tip, text_tip_rect)

        text_tip_count += 1
        if text_tip_count % text_tip_freq == 0:
            text_tip_count = 0
            text_tip_show_flag = not text_tip_show_flag
        pygame.display.flip()
        clock.tick(cfg.FPS)