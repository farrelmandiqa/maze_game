from pygame import *
#Creating a window
win_width = 700
win_height = 500
window = display.set_mode((win_width, win_height))#jendela yang dibuat pada langkah sebelumnya
back = (160, 160, 160)#pengaturan warna sesuai dengan skema warna RGB
 
display.set_caption('Permainan pertama saya')
run = True
class GameSprite(sprite.Sprite):
    def __init__(self,picture,w,h,x,y):
        super().__init__()
        self.image=transform.scale(image.load(picture),(w,h))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    def reset(self): 
        window.blit(self.image,(self.rect.x,self.rect.y))
class Player(GameSprite):
    def __init__(self,picture,w,h,x,y, x_speed,y_speed):
        GameSprite.__init__(self,picture,w,h,x,y)
        self.x_speed = x_speed
        self.y_speed = y_speed
    def update(self):
        self.rect.x += self.x_speed
        self.rect.y += self.y_speed
#creating wall pictures
w1 = GameSprite('platformh.png',win_width / 2 - win_width / 3, win_height / 2, 300, 50)
w2 = GameSprite('platformv.png', 370, 100, 50, 400)
#creating sprites
packman = Player('1-2.png', 5, win_height - 80, 80, 80, 0, 0)
while run:
    time.delay(50)
    window.fill(back)#isi jendela dengan warna
    for e in event.get():
        if e.type == QUIT:
            run = False
        elif e.type == KEYDOWN:
            if e.key == K_LEFT:
                packman.x_speed = -5
            elif e.key == K_RIGHT:
                packman.x_speed = 5
            elif e.key == K_UP:
                packman.y_speed = -5
            elif e.key == K_DOWN:
                packman.y_speed = 5
        elif e.type == KEYUP:
            if e.key == K_LEFT:
                packman.x_speed = 0
            elif e.key == K_RIGHT:
                packman.x_speed = 0
            elif e.key == K_UP:
                packman.y_speed = 0
            elif e.key == K_DOWN:
                packman.y_speed = 0
    w1.reset()
    w2.reset()
    packman.update()

     
    display.update()



