import random
import pygame


class Button():

    def __init__(self, x, y, pos, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.pos = pos

    def clicked(self, pos):
        self.pos = pygame.mouse.get_pos()
        if self.pos[0] > self.x and self.pos[0] < self.x + self.width:
            if self.pos[1] > self.y and self.pos[1] < self.y + self.height:
                return True
        return False


class RpsGame():

    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((960, 640))
        pygame.display.set_caption("RPS Smasher")

        self.bg = pygame.image.load("background.jpg").convert_alpha()
        self.rock = pygame.image.load("rock.png").convert_alpha()
        self.paper = pygame.image.load("paper.png").convert_alpha()
        self.scissors = pygame.image.load("scissors.png").convert_alpha()

        self.r_button_bg = pygame.image.load("r_button.png").convert_alpha()
        self.p_button_bg = pygame.image.load("p_button.png").convert_alpha()
        self.s_button_bg = pygame.image.load("s_button.png").convert_alpha()

        self.screen.blit(self.r_button_bg, (60, 500))
        self.screen.blit(self.p_button_bg, (260, 500))
        self.screen.blit(self.s_button_bg, (460, 500))

        self.r_button = Button(60, 500, pygame.mouse.get_pos(), 120, 120)
        self.p_button = Button(260, 500, pygame.mouse.get_pos(), 120, 120)
        self.s_button = Button(460, 500, pygame.mouse.get_pos(), 120, 120)

        self.font = pygame.font.Font(None, 36)
        self.text = self.font.render("True", True, (255, 255, 255))


def player(self):
    if self.rock_btn.clicked(30):
        self.pl_option = "rock"
        self.screen.blit(self.choose_rock, (120, 200))
    elif self.paper_btn.clicked(30):
        self.pl_option = "paper"
        self.screen.blit(self.choose_paper, (120, 200))
    else:
        self.scissors_btn.clicked(60)
        self.pl_option = "scissors"
        self.screen.blit(self.choose_scissors, (120, 200))

    return self.pl_option


def computer(self):
    self.pc_random_choice = ""
    pc_choice = ["rock", "paper", "scissors"]
    pc_choice = random.choice(list(option))
    if pc_choice == "rock":
        self.pc_random_choice = "rock"
        self.pc_choice = self.choose_rock
    elif pc_choice == "paper":
        self.pc_random_choice = "paper"
        self.pc_choice = self.choose_paper
    else:
        self.pc_random_choice = "scissors"
        self.pc_choice = self.choose_scissors

        pc_option = self.screen.blit(pc_choice, (600, 200))
    return pc_option


def pl_score_cache(self):
    self.pl_score = 0
    self.pl_score = 0

    pl = self.pl_option
    pc = self.pc_random_choice

    if pl == "rock" and pc == "paper" or pl == "paper" and pc == "scissors" or pl == "scissors" and pc == "rock":
        self.pc_score += 1
    elif pl == pc:
        pass
    else:
        self.pl_score += 1

    return self.pl_score


def pc_score_cache(self):
    self.pl_score = 0
    self.pc_score = 0

    pl = self.pl_option
    pc = self.pc_random_choice

    if pl == "rock" and pc == "paper" or pl == "paper" and pc == "scissors" or pl == "scissors" and pc == "rock":

        self.pc_score += 1
    elif pl == pc:
        pass
    else:
        self.pl_score += 1
    return self.pc_score


def image_reset(self):
    self.screen.blit(self.text, (330, 0))
    self.text = self.font.render(" ", True, (0, 0, 0))
    self.screen.blit(self.bg, (0, 0))
    self.screen.blit(self.r_btn, (300, 500))
    self.screen.blit(self.p_btn, (400, 500))
    self.screen.blit(self.s_btn, (500, 500))


def game_loop(self):
    run = True
    clock = pygame.time.Clock()
    rps_game = RpsGame()

    while run:
        pygame.display.update()
        self.screen.blit(self.text, (330, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.rock_btn.clicked(30) or self.paper_btn.clicked(340) or \
                 self.scissors_btn.clicked(640):
                    rps_game.image_reset()
                    rps_game.player()
                    rps_game.computer()

                    self.pl_score += rps_game.pl_score_cache()
                    self.pc_score += rps_game.pc_score_cache()
                    self.text = self.font.render(
                        f'{self.pl_score} : {self.pc_score}', True,
                        (255, 255, 255))

            pygame.display.flip()
            clock.tick(30)

    pygame.quit()


if __name__ == '__main__':
    game = RpsGame()
    game.game_loop()
