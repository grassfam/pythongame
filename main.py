import pygame


def main():
    pygame.init()

    WINDOW_WIDTH = 500
    WINDOW_HEIGHT = 500

    display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption("여기에 엔트리포인트 코드가 작성됩니다.")

    clock = pygame.time.Clock()

    system_font = pygame.font.SysFont('arial', 30)

    game_font = system_font.render("Entrypoint", True, (255, 255, 255))
    game_font_rect = game_font.get_rect()
    game_font_rect.center = (WINDOW_WIDTH//2, 100)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        display_surface.fill((0,0,0))
        display_surface.blit(game_font, game_font_rect)
        pygame.display.update()
        clock.tick(60)

    pygame.quit()


if __name__ == "__main__":
    main()