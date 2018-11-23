#!/usr/bin/python3
# -*- coding: utf-8 -*-

# Данный скрипт позволяет установить "Вечный онлайн" на аккаунт.

import requests
from time import gmtime, strftime, sleep

# Укажите в access_token токен 
# (его можно получить например здесь https://vkhost.github.io/)

access_token = ""


def call(method, param={}, **kwargs):
	"""Выполнение указанного метода"""
	global access_token
	param['access_token'] = access_token
	param['v']:'5.89'
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
			call("account.setOnline")
			print(strftime("%d.%m.%Y %H:%M:%S") + " Установлен статус Online")
			sleep(300)

	except Exception as e:
		print(e)