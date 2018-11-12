#!/usr/bin/python3
# -*- coding: utf-8 -*-

# Данный скрипт позволяет установить "Вечный онлайн" на аккаунт.

import time
import datetime
import requests

# Укажите в access_token токен (его можно получить например здесь https://vkhost.github.io/)
access_token = ""


def method(method, param={}, **kwargs):
	"""Выполнение указанного метода"""
	global access_token
	param['access_token'] = access_token
	param['v']:'5.89'
	param.update(kwargs)

	resp = requests.get("https://api.vk.com/method/" + method,
	 params=param, timeout=10).json()

	if 'error' in resp:
		print("#{error_code}: {error_msg}".format(**resp['error']))

	return resp


def get_time():
	"""Получение текущего времени"""
	return str(datetime.datetime.strftime(
		datetime.datetime.now(), "%d.%m.%Y %H:%M:%S"))


if __name__ == '__main__':
	try:
		while True:
			print(get_time() + " Установлен статус Online")
			method("account.setOnline")
			time.sleep(300)

	except Exception as e:
		print(e)