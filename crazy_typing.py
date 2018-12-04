#!/usr/bin/python3
# -*- coding: utf-8 -*-

# Данный скрипт постоянно отправляет статус в фоновом режиме о том,
# что вы печатаете сообщение относительно выбранных диалогов.
import json
import requests
from time import gmtime, strftime, sleep

# Укажите в access_token токен 
# (его можно получить например здесь https://vkhost.github.io/)

access_token = ""

# Укажите через запятую id диалогов в dialogs

dialogs = []


def call(method, param={}, **kwargs):
	"""Выполнение указанного метода"""
	global access_token
	param['access_token'] = access_token
	param['v']='5.80'
	param.update(kwargs)

	try:
		resp = requests.get("https://api.vk.com/method/" + method,
	 	 params=param, timeout=10).json()
	except Exception as e:
		raise e

	if 'error' in resp:
		raise Exception("Error #{error_code}: {error_msg}".format(**resp['error']))

	return resp


if __name__ == '__main__':
	try:
		while True:
			for dialog in dialogs:
				call("messages.setActivity", {'peer_id': dialog, 'type':'typing'})
				print(strftime("%d.%m.%Y %H:%M:%S") + " Отправлен статус в диалог: " + str(dialog))
				sleep(3)
				
	except Exception as e:
		print(e)