# -*- coding: utf-8 -*-
import pygame
from sys import exit
from pygame.locals import *
import random

# 设置游戏屏幕大小
SCREEN_WIDTH = 480
SCREEN_HEIGHT = 800

# 子弹类
class Bullet(pygame.sprite.Sprite):
    def __init__(self, bullet_img, init_pos):
        pygame.sprite.Sprite.__init__(self)
        self.image = bullet_img
        self.rect = self.image.get_rect()
        self.rect.midbottom = init_pos
        self.speed = 10

    def move(self):
        self.rect.top -= self.speed

# 玩家飞机类
class Player1(pygame.sprite.Sprite):
    def __init__(self, plane_img, player_rect, init_pos):
        pygame.sprite.Sprite.__init__(self)
        self.image = []                                 # 用来存储玩家飞机图片的列表
        for i in range(len(player_rect)):
            self.image.append(plane_img.subsurface(player_rect[i]).convert_alpha())
        self.rect = player1_rect[0]                      # 初始化图片所在的矩形
        self.rect.topleft = init_pos                    # 初始化矩形的左上角坐标
        self.speed = 8                                  # 初始化玩家飞机速度，这里是一个确定的值
        self.bullets = pygame.sprite.Group()            # 玩家飞机所发射的子弹的集合
        self.img_index = 0                              # 玩家飞机图片索引
        self.is_hit = False                             # 玩家是否被击中

    # 发射子弹
    def shoot(self, bullet_img):
        bullet = Bullet(bullet_img, self.rect.midtop)
        self.bullets.add(bullet)

    # 向上移动，需要判断边界
    def moveUp(self):
        if self.rect.top <= 0:
            self.rect.top = 0
        else:
            self.rect.top -= self.speed

    # 向下移动，需要判断边界
    def moveDown(self):
        if self.rect.top >= SCREEN_HEIGHT - self.rect.height:
            self.rect.top = SCREEN_HEIGHT - self.rect.height
        else:
            self.rect.top += self.speed

    # 向左移动，需要判断边界
    def moveLeft(self):
        if self.rect.left <= 0:
            self.rect.left = 0
        else:
            self.rect.left -= self.speed

    # 向右移动，需要判断边界
    def moveRight(self):
        if self.rect.left >= SCREEN_WIDTH - self.rect.width:
            self.rect.left = SCREEN_WIDTH - self.rect.width
        else:
            self.rect.left += self.speed

# 玩家飞机类
class Player2(pygame.sprite.Sprite):
    def __init__(self, plane_img, player_rect, init_pos):
        pygame.sprite.Sprite.__init__(self)
        self.image = []                                 # 用来存储玩家飞机图片的列表
        for i in range(len(player_rect)):
            self.image.append(plane_img.subsurface(player_rect[i]).convert_alpha())
        self.rect = player2_rect[0]                      # 初始化图片所在的矩形
        self.rect.topleft = init_pos                    # 初始化矩形的左上角坐标
        self.speed = 8                                  # 初始化玩家飞机速度，这里是一个确定的值
        self.bullets = pygame.sprite.Group()            # 玩家飞机所发射的子弹的集合
        self.img_index = 0                              # 玩家飞机图片索引
        self.is_hit = False                             # 玩家是否被击中
    
    # 发射子弹
    def shoot(self, bullet_img):
        bullet = Bullet(bullet_img, self.rect.midtop)
        self.bullets.add(bullet)
    
    # 向上移动，需要判断边界
    def moveUp(self):
        if self.rect.top <= 0:
            self.rect.top = 0
        else:
            self.rect.top -= self.speed

    # 向下移动，需要判断边界
    def moveDown(self):
        if self.rect.top >= SCREEN_HEIGHT - self.rect.height:
            self.rect.top = SCREEN_HEIGHT - self.rect.height
        else:
            self.rect.top += self.speed
                
    # 向左移动，需要判断边界
    def moveLeft(self):
        if self.rect.left <= 0:
            self.rect.left = 0
        else:
            self.rect.left -= self.speed
    
    # 向右移动，需要判断边界
    def moveRight(self):
        if self.rect.left >= SCREEN_WIDTH - self.rect.width:
            self.rect.left = SCREEN_WIDTH - self.rect.width
        else:
            self.rect.left += self.speed


# 敌机类
class Enemy(pygame.sprite.Sprite):
    def __init__(self, enemy_img, enemy_down_imgs, init_pos):
       pygame.sprite.Sprite.__init__(self)
       self.image = enemy_img
       self.rect = self.image.get_rect()
       self.rect.topleft = init_pos
       self.down_imgs = enemy_down_imgs
       self.speed = 2
       self.down_index = 0

    # 敌机移动，边界判断及删除在游戏主循环里处理
    def move(self):
        self.rect.top += self.speed

# 更快的敌机
class Enemyfaster(pygame.sprite.Sprite):
    def __init__(self, enemy_img, enemy_down_imgs, init_pos):
        pygame.sprite.Sprite.__init__(self)
        self.image = enemy_img
        self.rect = self.image.get_rect()
        self.rect.topleft = init_pos
        self.down_imgs = enemy_down_imgs
        self.speed = 3
        self.down_index = 0

    # 敌机移动，边界判断及删除在游戏主循环里处理
    def move(self):
        self.rect.top += self.speed

#飞一样的敌机
class Enemyfastest(pygame.sprite.Sprite):
    def __init__(self, enemy_img, enemy_down_imgs, init_pos):
        pygame.sprite.Sprite.__init__(self)
        self.image = enemy_img
        self.rect = self.image.get_rect()
        self.rect.topleft = init_pos
        self.down_imgs = enemy_down_imgs
        self.speed = 4
        self.down_index = 0
    
    # 敌机移动，边界判断及删除在游戏主循环里处理
    def move(self):
        self.rect.top += self.speed

#1. 初始化 pygame
pygame.init()

#2. 设置游戏界面大小、背景图片及标题
# 游戏界面像素大小
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# 游戏界面标题
pygame.display.set_caption('飞机大战')

# 背景图
background = pygame.image.load('/Users/han/Desktop/aa/PythonShootGame/resources/image/background.png').convert()
#
### Game Over 的背景图
game_over = pygame.image.load('/Users/han/Desktop/aa/PythonShootGame/resources/image/gameover.png')
#
## 飞机图片
plane_img = pygame.image.load('/Users/han/Desktop/aa/PythonShootGame/resources/image/shoot.png')

# 设置玩家飞机不同状态的图片列表，多张图片展示为动画效果
player1_rect = []
player1_rect.append(pygame.Rect(0, 99, 102, 126))        # 玩家飞机图片
player1_rect.append(pygame.Rect(165, 360, 102, 126))
player1_rect.append(pygame.Rect(165, 234, 102, 126))     # 玩家爆炸图片
player1_rect.append(pygame.Rect(330, 624, 102, 126))
player1_rect.append(pygame.Rect(330, 498, 102, 126))
player1_rect.append(pygame.Rect(432, 624, 102, 126))
player2_rect = []
player2_rect.append(pygame.Rect(0, 99, 102, 126))        # 玩家飞机图片
player2_rect.append(pygame.Rect(165, 360, 102, 126))
player2_rect.append(pygame.Rect(165, 234, 102, 126))     # 玩家爆炸图片
player2_rect.append(pygame.Rect(330, 624, 102, 126))
player2_rect.append(pygame.Rect(330, 498, 102, 126))
player2_rect.append(pygame.Rect(432, 624, 102, 126))
player1_pos = [100, 600]
player2_pos = [380, 600]
player1 = Player1(plane_img, player1_rect, player1_pos)
player2 = Player2(plane_img, player2_rect, player2_pos)

# 子弹图片
bullet_rect = pygame.Rect(1004, 987, 9, 21)
bullet_img = plane_img.subsurface(bullet_rect)

# 敌机不同状态的图片列表，多张图片展示为动画效果
enemy1_rect = pygame.Rect(534, 612, 57, 43)
enemy1_img = plane_img.subsurface(enemy1_rect)
enemy1_down_imgs = []
enemy1_down_imgs.append(plane_img.subsurface(pygame.Rect(267, 347, 57, 43)))
enemy1_down_imgs.append(plane_img.subsurface(pygame.Rect(873, 697, 57, 43)))
enemy1_down_imgs.append(plane_img.subsurface(pygame.Rect(267, 296, 57, 43)))
enemy1_down_imgs.append(plane_img.subsurface(pygame.Rect(930, 697, 57, 43)))

enemies1 = pygame.sprite.Group()
enemies2 = pygame.sprite.Group()
enemies3 = pygame.sprite.Group()

# 存储被击毁的飞机，用来渲染击毁动画
enemies_down1 = pygame.sprite.Group()
enemies_down2 = pygame.sprite.Group()

# 初始化射击及敌机移动频率
shoot_frequency = 0
enemy_frequency = 0
enemyfaster_frequency = 0

# 玩家飞机被击中后的效果处理
player1_down_index = 16
player2_down_index = 16

# 初始化分数
score1 = 0
score2 = 0

# 游戏循环帧率设置
clock = pygame.time.Clock()

# 判断游戏循环退出的参数
running = True

# 游戏主循环
while running:
    # 控制游戏最大帧率为 60
    clock.tick(60)
    
    # 生成子弹，需要控制发射频率
    #控制发射频率
    j = 15
    m = range(5)
    Cnum = 15
    
    if m in range(5):
        if score1+score2 in range(20*m,20*n+20):
            Enum = i-m

    if score1+score2 > 100:
        Cnum = 10

    # 首先判断玩家飞机没有被击中
    if not player1.is_hit:
        if shoot_frequency % Cnum == 0:
            player1.shoot(bullet_img)
        shoot_frequency += 1
        if shoot_frequency >= 99:
            shoot_frequency = 0

    if not player2.is_hit:
        if shoot_frequency % Cnum == 0:
            player2.shoot(bullet_img)
        shoot_frequency += 1
        if shoot_frequency >= 99:
            shoot_frequency = 0

# 生成敌机，需要控制生成频率
    #控制生成频率
    i = 30
    n = range(20)
    Enum = 30
    
    if n in range(20):
        if score1+score2 in range(5*n,5*n+5):
            Enum = i-n

    if score1+score2 > 100:
        Enum = 10

    if enemy_frequency % Enum == 0:
        enemy1_pos = [random.randint(0, SCREEN_WIDTH - enemy1_rect.width), 0]
        enemy1 = Enemy(enemy1_img, enemy1_down_imgs, enemy1_pos)
        enemies1.add(enemy1)
    enemy_frequency += 1
    if enemy_frequency >= 100:
        enemy_frequency = 0

    #生成更快的敌机
    if score1+score2 > 15:
        if enemy_frequency % 166 == 0:
            enemy1_pos = [random.randint(0, SCREEN_WIDTH - enemy1_rect.width), 0]
            enemy1 = Enemyfaster(enemy1_img, enemy1_down_imgs, enemy1_pos)
            enemies2.add(enemy1)
        enemyfaster_frequency += 1
        if enemyfaster_frequency >= 500:
            enemyfaster_frequency = 0
    if score1+score2 > 30:
        if enemy_frequency % 249 == 0:
            enemy1_pos = [random.randint(0, SCREEN_WIDTH - enemy1_rect.width), 0]
            enemy1 = Enemyfastest(enemy1_img, enemy1_down_imgs, enemy1_pos)
            enemies2.add(enemy1)
        enemyfaster_frequency += 1
        if enemyfaster_frequency >= 500:
            enemyfaster_frequency = 0


    for bullet in player1.bullets:
        # 以固定速度移动子弹
        bullet.move()
        # 移动出屏幕后删除子弹
        if bullet.rect.bottom < 0:
            player1.bullets.remove(bullet)

    for bullet in player2.bullets:
        # 以固定速度移动子弹
        bullet.move()
        # 移动出屏幕后删除子弹
        if bullet.rect.bottom < 0:
            player2.bullets.remove(bullet)

    for enemy in enemies1:
        #2. 移动敌机
        enemy.move()
        #3. 敌机与玩家飞机碰撞效果处理
        if pygame.sprite.collide_circle(enemy, player1):
            enemies_down1.add(enemy)
            enemies1.remove(enemy)
            player1.is_hit = True
            break
        #4. 移动出屏幕后删除飞机
        if enemy.rect.top < 0:
            enemies1.remove(enemy)

    for enemy in enemies1:
        #2. 移动敌机
        enemy.move()
        #3. 敌机与玩家飞机碰撞效果处理
        if pygame.sprite.collide_circle(enemy, player2):
            enemies_down2.add(enemy)
            enemies1.remove(enemy)
            player2.is_hit = True
            break
        #4. 移动出屏幕后删除飞机
        if enemy.rect.top < 0:
            enemies1.remove(enemy)

    for enemy in enemies2:
        #2. 移动更快的敌机
        enemy.move()
        #3. 敌机与玩家飞机碰撞效果处理
        if pygame.sprite.collide_circle(enemy, player1):
            enemies_down1.add(enemy)
            enemies2.remove(enemy)
            player1.is_hit = True
            break
        #4. 移动出屏幕后删除飞机
        if enemy.rect.top < 0:
                enemies2.remove(enemy)

    for enemy in enemies3:
        #2. 移动飞一样的敌机
        enemy.move()
        #3. 敌机与玩家飞机碰撞效果处理
        if pygame.sprite.collide_circle(enemy, player1):
            enemies_down1.add(enemy)
            enemies1.remove(enemy)
            player1.is_hit = True
            break
        #4. 移动出屏幕后删除飞机
        if enemy.rect.top < 0:
            enemies3.remove(enemy)

    for enemy in enemies2:
        #2. 移动更快的敌机
        enemy.move()
        #3. 敌机与玩家飞机碰撞效果处理
        if pygame.sprite.collide_circle(enemy, player2):
            enemies_down2.add(enemy)
            enemies2.remove(enemy)
            player2.is_hit = True
            break
        #4. 移动出屏幕后删除飞机
        if enemy.rect.top < 0:
            enemies2.remove(enemy)

    for enemy in enemies3:
        #2. 移动飞一样的敌机
        enemy.move()
        #3. 敌机与玩家飞机碰撞效果处理
        if pygame.sprite.collide_circle(enemy, player2):
            enemies_down2.add(enemy)
            enemies2.remove(enemy)
            player2.is_hit = True
            break
        #4. 移动出屏幕后删除飞机
        if enemy.rect.top < 0:
                enemies3.remove(enemy)


#敌机被子弹击中效果处理
    # 将被击中的敌机对象添加到击毁敌机 Group 中，用来渲染击毁动画
    enemies1_down = pygame.sprite.groupcollide(enemies1, player1.bullets, 1, 1)
    for enemy_down in enemies1_down:
        enemies_down1.add(enemy_down)

#敌机被子弹击中效果处理
    # 将被击中的敌机对象添加到击毁敌机 Group 中，用来渲染击毁动画
    enemies2_down = pygame.sprite.groupcollide(enemies2, player1.bullets, 1, 1)
    for enemy_down in enemies2_down:
        enemies_down1.add(enemy_down)

#敌机被子弹击中效果处理
    # 将被击中的敌机对象添加到击毁敌机 Group 中，用来渲染击毁动画
    enemies3_down = pygame.sprite.groupcollide(enemies3, player1.bullets, 1, 1)
    for enemy_down in enemies3_down:
        enemies_down1.add(enemy_down)

#敌机被子弹击中效果处理
    # 将被击中的敌机对象添加到击毁敌机 Group 中，用来渲染击毁动画
    enemies1_down = pygame.sprite.groupcollide(enemies1, player2.bullets, 1, 1)
    for enemy_down in enemies1_down:
        enemies_down2.add(enemy_down)

#敌机被子弹击中效果处理
    # 将被击中的敌机对象添加到击毁敌机 Group 中，用来渲染击毁动画
    enemies2_down = pygame.sprite.groupcollide(enemies2, player2.bullets, 1, 1)
    for enemy_down in enemies2_down:
        enemies_down2.add(enemy_down)

#敌机被子弹击中效果处理
    # 将被击中的敌机对象添加到击毁敌机 Group 中，用来渲染击毁动画
    enemies3_down = pygame.sprite.groupcollide(enemies3, player2.bullets, 1, 1)
    for enemy_down in enemies3_down:
        enemies_down2.add(enemy_down)



# 绘制背景
    screen.fill(0)
    screen.blit(background, (0, 0))

    # 绘制玩家飞机
    if not player1.is_hit:
        screen.blit(player1.image[player1.img_index], player1.rect)
        # 更换图片索引使飞机有动画效果
        player1.img_index = shoot_frequency / 50
    else:
        # 玩家飞机被击中后的效果处理
        player1.img_index = player1_down_index / 50
        screen.blit(player1.image[player1.img_index], player1.rect)
        player1_down_index += 8
        #玩家死后移除玩家飞机
        player1.rect.top = 1000
        player1.rect.left = 680
        if player1_down_index > 298:
            player1_down_index = 299
            # 击中效果处理完成后游戏结束
#            running = False

    if not player2.is_hit:
        screen.blit(player2.image[player2.img_index], player2.rect)
        # 更换图片索引使飞机有动画效果
        player2.img_index = shoot_frequency / 50
    else:
        # 玩家飞机被击中后的效果处理
        player2.img_index = player2_down_index / 50
        screen.blit(player2.image[player2.img_index], player2.rect)
        player2_down_index += 8
        #玩家死后移除玩家飞机
        player2.rect.top = 1000
        player2.rect.left = 680
        if player2_down_index > 298:
            player2_down_index = 299
            # 击中效果处理完成后游戏结束
#            running = False
    if player2_down_index == 299 and player1_down_index == 299:
        running = False


# 敌机被子弹击中效果显示
    for enemy_down in enemies_down1:
        if enemy_down.down_index == 0:
            pass
        if enemy_down.down_index > 7:
            enemies_down1.remove(enemy_down)
            score1 += 1
            continue
        screen.blit(enemy_down.down_imgs[enemy_down.down_index / 2], enemy_down.rect)
        enemy_down.down_index += 1

    for enemy_down in enemies_down2:
        if enemy_down.down_index == 0:
            pass
        if enemy_down.down_index > 7:
            enemies_down2.remove(enemy_down)
            score2 += 1
            continue
        screen.blit(enemy_down.down_imgs[enemy_down.down_index / 2], enemy_down.rect)
        enemy_down.down_index += 1

    # 显示子弹
    player1.bullets.draw(screen)
    player2.bullets.draw(screen)
    # 显示敌机
    enemies1.draw(screen)
    enemies2.draw(screen)
    enemies3.draw(screen)

    # 绘制得分
    score1_font = pygame.font.Font(None, 36)
    score1_text = score1_font.render(str(score1), True, (128, 128, 128))
    text_rect = score1_text.get_rect()
    text_rect.topleft = [10, 10]
    screen.blit(score1_text, text_rect)

    score2_font = pygame.font.Font(None, 36)
    score2_text = score2_font.render(str(score2), True, (128, 128, 128))
    text_rect = score2_text.get_rect()
    text_rect.topleft = [400, 10]
    screen.blit(score2_text, text_rect)
    
    # 更新屏幕
    pygame.display.update()
    
    # 处理游戏退出
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
            
    # 获取键盘事件（上下左右按键）
    key_pressed = pygame.key.get_pressed()
    
    # 处理键盘事件（移动飞机的位置）
    if key_pressed[K_w]:
        player1.moveUp()
    if key_pressed[K_s]:
        player1.moveDown()
    if key_pressed[K_a]:
        player1.moveLeft()
    if key_pressed[K_d]:
        player1.moveRight()

    if key_pressed[K_UP]:
        player2.moveUp()
    if key_pressed[K_DOWN]:
        player2.moveDown()
    if key_pressed[K_LEFT]:
        player2.moveLeft()
    if key_pressed[K_RIGHT]:
        player2.moveRight()


# 游戏 Game Over 后显示最终得分
font = pygame.font.Font(None, 48)
text1 = font.render('Score1: '+ str(score1), True, (255, 0, 0))
text2 = font.render('Score2: '+ str(score2), True, (255, 0, 0))
text1_rect = text1.get_rect()
text1_rect.centerx = screen.get_rect().centerx
text1_rect.centery = screen.get_rect().centery + 24
text2_rect = text2.get_rect()
text2_rect.centerx = screen.get_rect().centerx
text2_rect.centery = screen.get_rect().centery + 72
screen.blit(game_over, (0, 0))
screen.blit(text1, text1_rect)
screen.blit(text2, text2_rect)

# 显示得分并处理游戏退出
while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    pygame.display.update()


