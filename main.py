import pygame
import random
import sys

pygame.init()

white = (255, 255, 255)
pink = (255, 0, 132)
black = (0, 0, 0)

width, height = 600, 400
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Pedra, Papel e Tesoura")

background_image = pygame.image.load("tigrinho.png")
background_image = pygame.transform.scale(background_image, (width, height))

font = pygame.font.SysFont(None, 50)

class Game:
    def __init__(self):
        self.player_choice = None
        self.computer_choice = None
        self.result = None

    def play(self, player_choice):
        choices = ["rock", "paper", "scissors"]
        self.player_choice = player_choice
        self.computer_choice = random.choice(choices)
        self.result = self.determine_winner()

    def determine_winner(self):
        if self.player_choice == self.computer_choice:
            return "draw"
        elif (
            (self.player_choice == "rock" and self.computer_choice == "scissors")
            or (self.player_choice == "paper" and self.computer_choice == "rock")
            or (self.player_choice == "scissors" and self.computer_choice == "paper")
        ):
            return "player"
        else:
            return "computer"

def display_text(text, size, y, color=pink):
    font_size = pygame.font.Font(None, size)
    rendered_text = font_size.render(text, True, color)
    screen.blit(rendered_text, (width // 2 - rendered_text.get_width() // 2, y))

def main():
    game = Game()

    clock = pygame.time.Clock()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()

                if event.key == pygame.K_r:
                    game.play("rock")
                elif event.key == pygame.K_p:
                    game.play("paper")
                elif event.key == pygame.K_s:
                    game.play("scissors")

        screen.blit(background_image, (0, 0))  # Desenha a imagem de fundo
        display_text("Pressione R para Pedra, P para Papel, S para Tesoura", 20, height - 65)

        if game.player_choice:
            display_text(f"Você escolheu: {game.player_choice}", 50, 100)
            display_text(f"Computador escolheu: {game.computer_choice}", 50, 150)

            if game.result == "player":
                display_text("Você venceu!", 50, 200, color=(0, 255, 0))
            elif game.result == "computer":
                display_text("Computador venceu!", 50, 200, color=(255, 0, 0))
            else:
                display_text("Empate!", 50, 200, color=(0, 0, 255))

            display_text("Pressione ESC para sair ou qualquer tecla para jogar novamente", 20, height - 50)

        pygame.display.update()
        clock.tick(30) 

if __name__ == "__main__":
    main()