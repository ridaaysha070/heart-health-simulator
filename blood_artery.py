import pygame,random

xmax = 1000
ymax = 600

red = (128,0,0)


class Particle():
    def __init__(self, x, y, dx, dy, col):
        self.x = x
        self.y = y
        self.col = red
        self.ry = y
        self.rx = x
        self.dx = dx
        self.dy = dy

    def move(self):
        if self.y >= 10:
            if self.dy < 0:
                self.dy = -self.dy

        self.ry -= self.dy
        self.y = int(self.ry + 0.5)

        self.dy -= .1
        if self.y < 1:
            self.y += 500

def main():
    pygame.init()
    screen = pygame.display.set_mode((xmax,ymax))

    particles = []
    for part in range(10000000000000000000000000000000000000):
        if part % 2 > 0:
        particles.append( Particle(random.randint(500, 530), random.randint(0, 500), 0, 0, col))

    exitflag = False
    while not exitflag:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

        screen.fill(white)
        for p in particles:
            p.move()
            pygame.draw.circle(screen, p.col, (p.x, p.y), 8)

        pygame.display.flip()
    pygame.quit()

if __name__ == "__main__":
    main()
