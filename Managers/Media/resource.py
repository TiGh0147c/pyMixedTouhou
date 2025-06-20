# -*- coding: UTF-8 -*-
import pygame
from pygame.locals import *


class Resource(object):
	"""贴图资源管理器类, 维护全部的游戏贴图资源"""

	def __init__(self):
		# 储存需导入的文件名
		file_name = [
			"background.png",
			"bubble.png",
			"bullet1.png",
			"bullet2.png",
			"bullet3.png",
			"cirno-fly.png",
			"cirno-left.png",
			"cirno-right.png",
			"enemy.png",
			"enemy2.png",
			"front00.png",
			"loading.png",
			"point.png",
			"resource.png",
			"player.png",
			"bg.png",
			"stg3bg.png",
			"stg3bg2.png",
			"stg3bg3.png",
			"stg3bg4.png",
			"eff02.png",
		]

		self.image = {}					# 初始化储存待处理文件的字典
		self.pic = {}					# 初始化储存经过预处理文件的字典
		self.anime = {}					# 初始化储存动画的字典

		for i in file_name:				# 使用一次循环导入列表中指定的所有贴图
			self.pic[i] = pygame.image.load("./Resources/pic/"+i).convert_alpha()

		# 导入贴图并指定新代号, 预备后续处理
		self.image["background"] = self.pic["background.png"]
		self.image["loading"] = self.pic["loading.png"]
		self.image["front00"] = self.pic["front00.png"]
		self.image["bg"] = self.pic["bg.png"]
		self.image["bg1"] = self.pic["stg3bg.png"]
		self.image["bg2"] = self.pic["stg3bg2.png"]
		self.image["bg3"] = self.pic["stg3bg3.png"]
		self.image["bg4"] = self.pic["stg3bg4.png"]
		self.image["bg5"] = pygame.image.load("./Resources/pic/eff02.png").convert()
		self.image["bg6"] = pygame.image.load("./Resources/pic/sc02.png").convert()

		self.pic["reimu.png"] = pygame.image.load("./Resources/pic/reimu.png").convert()
		self.pic["reimu.png"].set_colorkey((0, 0, 0))
		self.image["reimu"] = self.pic["reimu.png"].subsurface((0, 0, 128, 256))

		self.pic["cirno.png"] = pygame.image.load("./Resources/pic/cirno.png").convert()
		self.pic["cirno.png"].set_colorkey((0, 0, 0))
		self.image["cirno"] = self.pic["cirno.png"].subsurface((0, 0, 128, 256))

		# Title Resources
		# 主页面资源
		self.pic["title_buttons"] = pygame.image.load("./Resources/pic/title01.png")
		self.image["Game_Startb"] = self.pic["title_buttons"].subsurface((0, 0, 128, 16))
		self.image["Game_Startd"] = self.pic["title_buttons"].subsurface((128, 0, 128, 16))
		self.image["Extra_Startb"] = self.pic["title_buttons"].subsurface((0, 16, 128, 16))
		self.image["Extra_Startd"] = self.pic["title_buttons"].subsurface((128, 16, 128, 16))
		self.image["Practise_Startb"] = self.pic["title_buttons"].subsurface((0, 32, 128, 16))
		self.image["Practise_Startd"] = self.pic["title_buttons"].subsurface((128, 32, 128, 16))
		self.image["Replayb"] = self.pic["title_buttons"].subsurface((0, 48, 128, 16))
		self.image["Replayd"] = self.pic["title_buttons"].subsurface((128, 48, 128, 16))
		self.image["Player_Datab"] = self.pic["title_buttons"].subsurface((0, 64, 128, 16))
		self.image["Player_Datad"] = self.pic["title_buttons"].subsurface((128, 64, 128, 16))
		self.image["Music_Roomb"] = self.pic["title_buttons"].subsurface((0, 80, 128, 16))
		self.image["Music_Roomd"] = self.pic["title_buttons"].subsurface((128, 80, 128, 16))
		self.image["Optionb"] = self.pic["title_buttons"].subsurface((0, 96, 128, 16))
		self.image["Optiond"] = self.pic["title_buttons"].subsurface((128, 96, 128, 16))
		self.image["Quitb"] = self.pic["title_buttons"].subsurface((0, 112, 128, 16))
		self.image["Quitd"] = self.pic["title_buttons"].subsurface((128, 112, 128, 16))

		# Menu Buttons Resources
		# 暂停菜单页面资源
		self.pic["menu_buttons"] = pygame.image.load("./Resources/pic/pause.png")
		self.image["menu_title"] = self.pic["menu_buttons"].subsurface((0, 0, 116, 32))
		self.image["confirm_title"] = self.pic["menu_buttons"].subsurface((0, 160, 256, 32))
		self.image["Resume_Start"] = self.pic["menu_buttons"].subsurface((0, 32, 200, 32))
		self.image["To_Title_Start"] = self.pic["menu_buttons"].subsurface((0, 64, 160, 32))
		self.image["Retry_Start"] = self.pic["menu_buttons"].subsurface((0, 96, 178, 32))
		self.image["Yes"] = self.pic["menu_buttons"].subsurface((0, 256, 108, 32))
		self.image["No"] = self.pic["menu_buttons"].subsurface((0, 288, 108, 32))
		self.image["Dead"] = self.pic["menu_buttons"].subsurface((0, 320, 128, 32))
		self.image["Clear"] = self.pic["menu_buttons"].subsurface((0, 352, 128, 32))

		# Bullets Resources
		# 子弹资源
		tmp = Rect(0, 0, 16, 16)
		tp = self.pic["bullet1.png"]
		self.image["bullet1"] = []
		for i in range(12):
			self.image["bullet1"].append([])
			for j in range(16):
				self.image["bullet1"][i].append(tp.subsurface(tmp))
				tmp.left += 16
			tmp.top += 16
			tmp.left -= 256
		tmp = Rect(0, 240, 8, 8)
		self.image["bullet1"].append([])
		for i in range(16):
			self.image["bullet1"][12].append(tp.subsurface(tmp))
			tmp.left += 8
			if i == 7:
				tmp = Rect(0, 248, 8, 8)

		tmp = Rect(0, 0, 32, 32)
		tp = self.pic["bullet2.png"]		# temp-picture
		self.image["bullet2"] = []
		for i in range(6):
			self.image["bullet2"].append([])
			for j in range(8):
				self.image["bullet2"][i].append(tp.subsurface(tmp))
				tmp.left += 32
			tmp.top += 32
			tmp.left -= 256
		tmp = Rect(0, 192, 64, 64)
		self.image["bullet2"].append([])
		for i in range(4):
			self.image["bullet2"][6].append(tp.subsurface(tmp))
			tmp.left += 64

		# Resources
		# 掉点资源
		tmp = Rect(0, 0, 32, 32)
		tp = self.pic["resource.png"]
		self.image["resource"] = []
		for i in range(5):
			self.image["resource"].append([])
			for j in range(4):
				self.image["resource"][i].append(tp.subsurface(tmp))
				tmp.left += 32
			tmp.top += 32
			tmp.left -= 128

		self.anime["bubble"] = []
		tp = self.pic["bubble.png"]
		tmp = tp.get_rect()
		tmp.width /= 8
		tmpw = tmp.width
		for i in range(8):
			self.anime["bubble"].append(tp.subsurface(tmp))
			tmp.left += tmpw

		# Boss
		# Boss资源
		self.anime["cirno"] = [[], [], []] 			# stay left right
		tp = self.pic["cirno-fly.png"]
		tmp = tp.get_rect()
		tmp.width /= 4
		tmpw = tmp.width
		for i in range(4):
			self.anime["cirno"][0].append(tp.subsurface(tmp))
			tmp.left += tmpw
		tp = self.pic["cirno-left.png"]
		tmp = tp.get_rect()
		tmp.width /= 4
		tmpw = tmp.width
		for i in range(4):
			self.anime["cirno"][1].append(tp.subsurface(tmp))
			tmp.left += tmpw
		tp = self.pic["cirno-right.png"]
		tmp = tp.get_rect()
		tmp.width /= 4
		tmpw = tmp.width
		for i in range(4):
			self.anime["cirno"][2].append(tp.subsurface(tmp))
			tmp.left += tmpw

		# Enemies
		# 敌机 (Fairies) 资源
		tmp = Rect(0, 0, 32, 32)
		tp = self.pic["enemy.png"]
		self.anime["enemy"] = []
		for i in range(8):
			self.anime["enemy"].append([[], [], [], [], []])
			for j in range(3):
				for k in range(4):
					self.anime["enemy"][i][j].append(tp.subsurface(tmp))
					tmp.left += 32
			for j in range(2):
				for k in range(4):
					self.anime["enemy"][i][j+3].append(
						pygame.transform.flip(self.anime["enemy"][i][j][k], True, False))
			tmp.top += 32
			tmp.left -= 384
			if i == 3:
				tmp.topleft = (0, 256)

		self.anime["enemy"].append([])
		tmp = Rect(0, 384, 64, 64)
		for i in range(5):
			self.anime["enemy"][8].append(tp.subsurface(tmp))
			tmp.left += 64
			
		tmp = Rect(64, 128, 32, 32)
		self.anime["enemy"].append(tp.subsurface(tmp))
		tmp = Rect(96, 128, 32, 32)
		self.anime["enemy"].append(tp.subsurface(tmp))
		tmp = Rect(64, 160, 32, 32)
		self.anime["enemy"].append(tp.subsurface(tmp))
		tmp = Rect(64, 160, 32, 32)
		self.anime["enemy"].append(tp.subsurface(tmp))

		tp = self.pic["enemy2.png"]
		self.anime["enemy2"] = []
		tmp = Rect(0, 0, 32, 32)
		for i in range(4):
			self.anime["enemy2"].append([])
			for j in range(8):
				self.anime["enemy2"][i].append(tp.subsurface(tmp))
				tmp.left += 32
			tmp.left = 0
			tmp.top += 32

		# Player
		# 自机资源
		tmp = Rect(0, 0, 32, 48)
		tp = self.pic["player.png"]
		self.anime["player"] = [[], [], []] 			# stay left right point tama bullet1 bullet2
		for i in range(3):
			for j in range(8):
				self.anime["player"][i].append(tp.subsurface(tmp))
				tmp.left += 32
			tmp.top += 48
			tmp.left -= 256
		tmp = Rect(0, 16, 64, 64)
		self.anime["player"].append(self.pic["point.png"].subsurface(tmp))
		tmp = Rect(96, 144, 16, 16)
		self.anime["player"].append(tp.subsurface(tmp))
		tmp = Rect(0, 176, 64, 16)
		self.anime["player"].append(tp.subsurface(tmp))
		tmp = Rect(64, 176, 64, 16)
		self.anime["player"].append(tp.subsurface(tmp))
		tmp = Rect(0, 192, 64, 64)
		self.anime["player"].append(tp.subsurface(tmp))
		# Audio Effect Resources
		# 音频资源
		self.se = {}
		se_name = [
			"se_bonus.wav",
			"se_cardget.wav",
			"se_cat00.wav",
			"se_nep00.wav",
			"se_select00.wav",
			"se_pldead00.wav",
			"se_cancel00.wav",
			"se_damage00.wav",
			"se_pause.wav",
			"se_extend.wav",
			"se_plst00.wav",
			"se_tan02.wav",
			"se_enep00.wav",
			"se_item00.wav",
			"se_slash.wav"
		]
		se_myname = [
			"bonus",
			"cardget",
			"connect",
			"invincible",
			"select",
			"miss",
			"cancel",
			"damage",
			"pause",
			"extend",
			"playershoot",
			"tanshoot",
			"enemydead",
			"itemget",
			"schit"
		]
		for i in range(len(se_name)):
			self.se[se_myname[i]] = pygame.mixer.Sound("./Resources/se/"+se_name[i])
