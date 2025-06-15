# -*- encoding: UTF-8 -*-
import pygame
from pygame.locals import *
from GUI import menu
import globe
import sys

global globaltext

globaltext = ["showright",
	['这个基于Pygame的小游戏','是我们小组所做的大作业。'],
	['算是用Pygame还原了','一款比较经典的STG游戏，'],[ '为什么选这个？因为游戏就是','能够体现人机交互的软件类型。' ],
	['所以剧情什么的,我们', '只是想展现出有在做而已。'],
	['先不说了，前面有动静……'],
	"showleft",
	['我穿越了？这不是星莲船么……'],
	"showright",
	['啊这，难道你没有发现，', '实际上你的背景在风神录么？'],
	['而且你我的立绘来自辉针城，', '你能跨越版边的能力来自地灵殿……'],
	"showleft",
	['啊？难道我陷入了时空异变？'],
	"showright",
	['不知道，可能只是技术力太低，', '但是我现在好像必须要和你打。'],
	"showleft",
	['好吧，虽然搞不明白，','但是干就完了对吧。'],
]


class TextPlayer(object):
	def __init__(self):
		self.backgroundB = (
			pygame.image.load("./Resources/pic/ascii.png").convert_alpha()).subsurface(0, 89, 256, 38)
		self.backgroundA = (
			pygame.image.load("./Resources/pic/ascii.png").convert_alpha()).subsurface(0, 153, 256, 38)
		self.texts = globaltext
		self.index = 0
		self.lpic = globe.mgame.rsmanager.image["reimu"]
		# globe.mgame是main.py中的Main_Window类，其中的rsmanager是self.rsmanager = Managers.resource.Resource()，定位贴图资源管理器
		# 从Managers文件夹中的resource.py里的Resource()类，
		# 从中取出cirno的图像
		self.rpic = globe.mgame.rsmanager.image["cirno"]
		self.lpic_av = False
		self.rpic_av = False
		self.font = pygame.font.SysFont("SimHei", 18)
		# 从系统字体库中加载并返回一个新的字体对象。name是字体，size是大小，找不到会加载默认的pygame字体
		# 还可以加italic斜体和bold加粗的参数要求，默认false
		self.rc = pygame.Rect(
			globe.game_active_rect.left, globe.game_active_rect.bottom-96, globe.game_active_rect.width, 68)

	def command(self, cm=None):
		if cm == "next":
			self.index += 1
		else:
			cm = self.texts[self.index]
			if cm == "showleft":
				self.lpic_av = True
				self.rpic_av = False
				self.index += 1
			elif cm == "showright":
				self.rpic_av = True
				self.lpic_av = False
				self.index += 1

	def update(self):
		if self.index < len(self.texts):
			self.command()
		else:
			globe.scgame.time += 1
			globe.scgame.tstart()
			return
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()

			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_z:
					self.command("next")
				elif event.key == pygame.K_ESCAPE:
					globe.mgame.msmanager.play_SE("pause")
					globe.mgame.call(menu.Menu)

	def draw(self, screen):
		if globe.scgame.timestop:
			if not self.lpic_av:
				screen.fill((100, 100, 100), self.rc, BLEND_RGB_ADD)
				screen.blit(self.backgroundA, (50, 400))
				if type(self.texts[self.index]) == str:
					txtimg = self.font.render(self.texts[self.index], True, (0, 255, 255))
					screen.blit(txtimg,(self.rc.left+10,self.rc.top+10))
				elif type(self.texts[self.index]) == list:
					for i in range(len(self.texts[self.index])):
						txtimg = self.font.render(self.texts[self.index][i], True, (0, 255, 255))
						screen.blit(txtimg, (self.rc.left+10, self.rc.top+10+i*30))
				if self.rpic_av:
					tprc = self.rpic.get_rect()
					tprc.right = self.rc.right
					tprc.bottom = self.rc.bottom + 28
					screen.blit(self.rpic, tprc)
				elif self.lpic_av:
					tprc = self.lpic.get_rect()
					tprc.left = self.rc.left
					tprc.bottom = self.rc.bottom + 28
					screen.blit(self.lpic, tprc)

			else:
				tp = self.rc.copy()
				screen.fill((100, 100, 100), tp, BLEND_RGB_ADD)
				screen.blit(self.backgroundB, (170, 400))
				if type(self.texts[self.index]) == str:
					txtimg = self.font.render(self.texts[self.index], True, (255, 255, 0))
					screen.blit(txtimg,(self.rc.left+5+128,self.rc.top+10))
				elif type(self.texts[self.index]) == list:
					for i in range(len(self.texts[self.index])):
						txtimg = self.font.render(self.texts[self.index][i], True, (255, 255, 0))
						screen.blit(txtimg, (tp.left+5+128, tp.top+10+i*30))
				if self.rpic_av:
					tprc = self.rpic.get_rect()
					tprc.right = tp.right
					tprc.bottom = tp.bottom + 28
					screen.blit(self.rpic, tprc)
				elif self.lpic_av:
					tprc = self.lpic.get_rect()
					tprc.left = tp.left
					tprc.bottom = tp.bottom + 28
					screen.blit(self.lpic, tprc)
