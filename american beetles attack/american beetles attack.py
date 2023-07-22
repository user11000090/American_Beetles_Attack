import pygame; import math; import random; import os; pygame.init(); import time
pygame.mixer.init(); music = pygame.mixer.music.load(os.path.join("american beetles theme.mp3"))
width = 800; height = 600; screen = pygame.display.set_mode((width, height)); music_coin = 1
level = "menu"; beetles = []; speed_plus = 0; next_beetle = 1000; beetle_quant = 0
beetle_graph = pygame.image.load(os.path.join("american beetle.png"))
us_flag = pygame.image.load(os.path.join("us flag.png"))
ladybug = pygame.image.load(os.path.join("biedronka.png"))
testtime = time.time() + 0.1
speedtest = 0
while time.time() < testtime:
    speedtest +=1
spdt = speedtest/1000000
def txt(text, x, y, color, size):
    font = pygame.font.SysFont("Calibri", size)
    rend = font.render(text, 1, color)
    x = (width - rend.get_rect().width) / 2
    screen.blit(rend, (x, y))
class insect():
    def __init__(self, x, y):
        self.size = 30;
        self.x = random.randint(self.size / 2, width - self.size / 2);
        self.y = random.choice([-29, 599]); self.graph = beetle_graph
        self.change_target_speed_x = 0; self.change_target_speed_y = 0
        self.speed_x = random.randint(-10, 10) / 50; self.speed_y = random.randint(-10, 10) / 50
        self.change_speed_countdown_x = 1000*spdt; self.change_speed_countdown_y = 1000*spdt
    def move(self):
        if self.change_target_speed_x > self.speed_x: self.speed_x = self.speed_x + 0.00004
        elif self.change_target_speed_x < self.speed_x: self.speed_x = self.speed_x - 0.00004
        if self.change_target_speed_y > self.speed_y: self.speed_y = self.speed_y + 0.00004
        elif self.change_target_speed_y < self.speed_y: self.speed_y = self.speed_y - 0.00004
        self.change_speed_countdown_x = self.change_speed_countdown_x - 1
        self.change_speed_countdown_y = self.change_speed_countdown_y - 1
        if self.change_speed_countdown_x <= 0:
            self.change_target_speed_x = random.randint(-10, 10) / 10
            self.change_speed_countdown_x = random.randint(800, 2400)
        if self.change_speed_countdown_y <= 0:
            self.change_target_speed_y = random.randint(-10, 10) / 10
            self.change_speed_countdown_y = random.randint(800, 2400)
        self.x = self.x + self.speed_x/spdt; self.y = self.y + self.speed_y/spdt
        if self.x < -30 or self.x > width:
            self.speed_x = self.speed_x * -1
            self.change_target_speed_x = self.change_target_speed_x * -1
        if self.y < -30 or self.y > height:
            self.speed_y = self.speed_y * -1
            self.change_target_speed_y = self.change_target_speed_y * -1
        self.speed_x = self.speed_x * 0.9999; self.speed_y = self.speed_y * 0.9999
    def draw(self):
        screen.blit(self.graph, (self.x, self.y))
    def touch(self,plr):
        if pygame.Rect(self.x, self.y, 30, 30).colliderect(plr): return True
        else: return False
class character():
    def __init__(self, lx, ly):
        self.lx = lx; self.ly = ly; self.speed_lx = 0; self.speed_ly = 0; self.velx = 0;
        self.vely = 0; self.lady_grph = ladybug
    def la_draw(self):
        screen.blit(ladybug, (self.lx, self.ly))
    def la_move(self):
        self.lx = self.lx + self.speed_lx/spdt; self.ly = self.ly + self.speed_ly/spdt;
        self.speed_lx = self.speed_lx + self.velx; self.speed_ly = self.speed_ly + self.vely
        if math.fabs(self.speed_lx) >= 0.3: self.speed_lx = self.speed_lx * 0.99
        if math.fabs(self.speed_ly) >= 0.3: self.speed_ly = self.speed_ly * 0.99
        if self.lx <= -0: self.lx = 0; self.speed_lx = self.speed_lx * -0.6
        if self.lx >= 770: self.lx = 770; self.speed_lx = self.speed_lx * -0.6
        if self.ly <= -0: self.ly = 0; self.speed_ly = self.speed_ly * -0.6
        if self.ly >= 570: self.ly = 570; self.speed_ly = self.speed_ly * -0.6
player = character(400,300)
if level == "menu" and music_coin == 1: pygame.mixer.music.play()
while True:
    for eve in pygame.event.get():
        if eve.type == pygame.QUIT:
            pygame.quit(); quit()
        if eve.type == pygame.KEYDOWN:
            if eve.key == pygame.K_RETURN:
                pygame.mixer.music.stop()
                if level == "menu":
                    level = "game"
                elif level == "game":
                    level = "menu"
                music_coin = 0
            if eve.key == pygame.K_UP:
                player.vely = -0.0002/spdt
            elif eve.key == pygame.K_DOWN:
                player.vely = 0.0002/spdt
            if eve.key == pygame.K_LEFT:
                player.velx = -0.0002/spdt
            elif eve.key == pygame.K_RIGHT:
                player.velx = 0.0002/spdt
            if eve.key == pygame.K_ESCAPE:
                pygame.quit(); quit()
        if eve.type == pygame.KEYUP:
            if eve.key == pygame.K_UP:
                player.vely = 0
            elif eve.key == pygame.K_DOWN:
                player.vely = 0
            if eve.key == pygame.K_LEFT:
                player.velx = 0
            elif eve.key == pygame.K_RIGHT:
                player.velx = 0        
    if level == "menu":
        
        player.lx = width / 2; player.ly = height / 2; player.speed_lx = 0; player.speed_ly = 0
        beetle_quant = 0; wait = 3000*spdt; next_beetle = 5000*spdt
        for a in beetles: beetles.remove(a)
        screen.fill((234, 234, 235))
        txt("American Beetles Attack", 0, 350, (230, 20, 2), 40)
        txt("press Enter to begin", 0, 420, (230, 20, 2), 15)
        txt("engine test points: " + str(spdt), 0, 580, (230, 20, 2), 12)
        screen.blit(us_flag, ((width - us_flag.get_rect().width) / 2, 80))
        screen.blit(beetle_graph, ((width - beetle_graph.get_rect().width) / 2, 470))
    if level == "game":
        screen.fill((234, 234, 235))
        player.la_draw(); player.la_move()
        if next_beetle <= 0:
            beetle_quant = beetle_quant + 1
            beetles.append(insect(random.randint(-100, 100), random.randint(-100, 100)))
            next_beetle = 5000*spdt
        for d in beetles:
            d.draw()
            d.move()
            if d.touch(pygame.Rect(player.lx + 3, player.ly + 3, 24, 24)): level = "game over"
        next_beetle = next_beetle - 1
        txt(str(beetle_quant), 10, 6, (210, 170, 2), 24)
    if level == "game over":
        screen.fill((36, 35, 35));
        txt(str(beetle_quant)+ " american beetles attacked one ladybird", 0, 300, (230, 20, 2), 32)
        wait = wait - 1
        if wait <= 0: level = "menu"
    pygame.display.update()
        
        
        

