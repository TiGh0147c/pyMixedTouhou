# -*- coding: UTF-8 -*-
import pygame
import globe
import cache
global player

class TamaManager(object):
	"""主要维护子机的位置，至多存在四枚子机"""

	def __init__(self):
		global player
		self.rect = []
		self.tmimg = globe.mgame.rsmanager.anime["player"][4]
		player = globe.scgame.player
		for i in range(4):
			self.rect.append(self.tmimg.get_rect())

	def update(self):
		"""更新子机方位，保证子机位置与高低速模式和自机位置相关"""
		global player
		self.image = cache.cache_rotate(self.tmimg, globe.scgame.time*2, True)
		for i in range(4):
			self.rect[i].size = self.image.get_size()
		power = player.power
		if player.keys[pygame.K_LSHIFT]:	#低速模式下子机收紧
			dis = 18
		else:
			dis = 28
		if power < 100:
			pass							#无子机状态
		elif power < 200:
			self.rect[0].center = player.point   		#1子机
			self.rect[0].top -= dis
		elif power < 300:
			self.rect[0].center = player.point			#2子机
			self.rect[0].left -= dis
			self.rect[1].center = player.point
			self.rect[1].left += dis
		elif power < 400:
			self.rect[0].center = player.point			#3子机
			self.rect[0].left -= dis
			self.rect[1].center = player.point
			self.rect[1].left += dis
			self.rect[2].center = player.point
			self.rect[2].top -= dis
		else:
			self.rect[0].center = player.point			#4子机
			self.rect[0].left -= dis
			self.rect[1].center = player.point
			self.rect[1].left += dis
			self.rect[2].center = self.rect[0].center
			self.rect[2].left -= (dis-10)
			self.rect[3].center=self.rect[1].center
			self.rect[3].left += (dis-10)

	def draw(self, screen):
		"""绘制子机"""
		tp = int(player.power/100)		# 确定子机数量
		if tp > 4:
			tp = 4
		for i in range(tp):
			screen.blit(self.image, self.rect[i])