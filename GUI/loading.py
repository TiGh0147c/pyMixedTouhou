# -*- coding: UTF-8 -*-
import pygame
import sys
from GUI import gaming
import globe
from random import *

sakuras = []
clock = pygame.time.Clock()
print(sys.path)


class Loading(object):
	screen = pygame.display.set_mode((640, 480))
	res = pygame.image.load("./Resources/pic/loading2.png").convert_alpha()
	loading = res.subsurface(4, 0, 124, 57)

	def __init__(self):
		self.count = 0
		# 设定页面切换效果: 淡出
		self.fade = pygame.Surface(globe.mgame.screen.get_size())  # 设定遮罩尺寸
		self.fade.fill((0, 0, 0))  # 以纯黑色填充遮罩

	def draw(self, screen):
		screen.blit(self.fade, (0, 0))
		for sakura in sakuras:
			now = sakura.image
			nowRect = now.get_rect()
			new = pygame.transform.rotate(now, sakura.rinit)
			newRect = new.get_rect(center=nowRect.center)
			newRect.center = (sakura.rect.x, sakura.rect.y)
			screen.blit(new, newRect)
		screen.blit(self.loading, [460, 380])
		if self.count >= 120:
			self.fade.set_alpha((self.count - 120) * 12)  # 对黑色遮罩进行透明化
			screen.blit(self.fade, (0, 0))

	def update(self):
		pygame.init()
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()
			else:
				pass
		if (self.count % 13 == 0) and (len(sakuras) <= 10):
			maple = Sakura()
			print(maple)
			sakuras.append(maple)
		sakura_update()
		self.count += 1
		if self.count >= 150:
			globe.mgame.goto(gaming.Gaming)

class Sakura(object):

	def __init__(self):
		self.xspeed = 0
		self.yspeed = 1
		self.rinit = 1
		self.rspeed = randint(1, 6)
		self.image = Loading.res.subsurface(0, 64, 33, 33)
		self.rect = self.image.get_rect()
		self.rect.x = randint(460, 600)
		self.rect.y = 360.0


def sakura_update():
	for sakura in sakuras:
		sakura.rinit += sakura.rspeed
		sakura.rect.y += sakura.yspeed
		sakura.rect.x += sakura.xspeed
		if (sakura.rect.y >= 440):
			sakuras.remove(sakura)