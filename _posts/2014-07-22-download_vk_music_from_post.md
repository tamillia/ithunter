---
layout: post
title: "Пишем программу-загрузчик для музыки ВКонтакте"
date: 2014-07-22 19:55:00
category: tutorial
tags: [python, vk, api]
description: "Скрипт на Python для скачивания песен из постов из ВКонтакте"
published: true
---

<img src="http://theasder.github.io/img/8387270418a6.png" class="img-responsive" /><br />

Для всех нетерпеливых есть [ссылка](https://gist.github.com/theasder/73c3f0a9270ebe611a80) на скрипт. UPD: была предложена версия для Python 3, вот [ссылка](http://pastebin.com/Px81WfEe). Чтобы его запустить требуется интерпретатор языка Python 3, и нужно написать в консоли `python3 название_скрипта.py`

Для запуска нужен интерпретатор языка Python 2, в консоли нужно ввести `python название_скрипта.py`. Чтобы скачать прикрепленную музыку из конкретного поста, достаточно ввести два последних числа из него, разделенные знаком _ . Например, мы хотим скачать музыку от сюда: [http://vk.com/wall-35193970_951](http://vk.com/wall-35193970_951). Достаточно ввести `-35193970_951`.

### Работа с API
API ВКонтакте предоставляет достаточно много методов, достаточно лишь посмотреть в [документацию](http://vk.com/dev/methods). Мы будем в данном случае пользоваться методом `wall.getById`, предоставляющий нам полную информацию о записи с заданным адресом. 

Как этим пользоваться? Чтобы получить то, что выведет данный метод нам нужно посмотреть в аргументы и присвоить им значения: в первом аргументе `post` мы должны присвоить адрес поста, аргументу `extended` присвоим 1, `copy_history_depth` присвоим 2. Нам два последних аргумента не так важны, оставим их такими, какие они в примере на странице [документации](http://vk.com/dev/wall.getById). Теперь мы должны оформить ссылку с данным методом, его аргументами и переданными значениями. Она будет выглядеть так: https://api.vk.com/method/**wall.getById**?**posts**=\_адрес\_поста\_ &**extended**=1&**copy\_history\_depth**=2

### Обрабатываем запрос

Напомним, что адресом поста будет два последних числа из ссылки на него (например, `-35193970_951`). У нас есть функция `urlopen` библиотеки `urllib2`, позволяющая скачать все содержание страницы, а также метод `read`, позволяющий записать все содержание в одну переменную:

{% highlight python linenos %}
#!/usr/bin/python
# -*- coding: utf-8 -*-
import urllib2
import ast
import re
 
def get_items_of_post(address):
    url = "https://api.vk.com/method/wall.getById?posts=" + address + "&extended=1&copy_history_depth=2"
    response = urllib2.urlopen(url)
    text = response.read()
{% endhighlight %}

Итак, в переменной `text` у нас записано содержание вывода метода `wall.getById` в виде строки(ее можно увидеть на [странице метода в документации](http://vk.com/dev/wall.getById)). Со строкой работать неудобно, её можно преобразовать в словарь с помощью функции `literal_eval` библиотеки `ast`. Пишем:

{% highlight python linenos %}
post_info = ast.literal_eval(text)
{% endhighlight %}

Функция будет вовращать массив с всеми прикрепленными файлами в записи. Если записи не существует, то пустой массив:
    
{% highlight python linenos %}
if post_info['response']['wall'] == []:
    return []
else:
    return post_info['response']['wall'][0]['attachments']
{% endhighlight %}

Дальше пишем то, что будем выполняться программой при ее запуске:

{% highlight python linenos %}
address = raw_input("Enter string of two right numbers of url of post\n") # ввод адреса
music = get_items_of_post(address)
{% endhighlight %}
   
Дальше мы должны просмотреть каждый из прикреплений к записи и, если это аудиозапись, мы должны обработать ссылку на нее, скачать содержимое файла и записать его в новый файл, который будет находиться там же, где и программа.

{% highlight python linenos %}
for attachment in music:
	type_of_attachment = attachment['type']
	if type_of_attachment != 'audio':
		pass
	else:
		artist = attachment[type_of_attachment]['artist']
		title = attachment[type_of_attachment]['title']
		name_of_file = artist + ' - ' + title + '.mp3'
		url = attachment[type_of_attachment]['url']
		if url == '': # предусмотрен случай, когда аудиозапись удалена из общего доступа
			print name_of_file + " was removed from public access"
			continue
		url = re.sub('\\\\\/', '/', url) # вместо простых слэшей изначально записываются `\\/`, поэтому нужно их заменить на просто слэши во всей строке
		url = re.sub('\?.*', '', url) # убираем все символы после расширения `.mp3`, они нам не нужны
		response = urllib2.urlopen(url)
		f = open(name_of_file, 'w')
		f.write(response.read())
		print name_of_file + " was downloaded" # оповещаем о том, что файл успешно скачался
{% endhighlight %}

