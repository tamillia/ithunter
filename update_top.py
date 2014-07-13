#!/usr/bin/python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from bs4 import BeautifulSoup
import unicodedata
import re
import regex
import urllib2
import ast


def get_id_of_recent_post():
    url = "https://api.vk.com/method/wall.get?owner_id=-54530371&count=1&filter=owner"
    response = urllib2.urlopen(url)
    text = response.read()
    post_info = ast.literal_eval(text)
    return post_info['response'][1]['id']

def get_items_of_post(id, flag = 0):
    url = "https://api.vk.com/method/wall.getById?posts=-54530371_" + str(id) + "&extended=1&copy_history_depth=2"
    response = urllib2.urlopen(url)
    text = response.read()
    post_info = ast.literal_eval(str(text))
    if post_info['response']['wall'] == []:
        return []
    else:
    	if flag == 0:
        	return post_info['response']['wall'][0]['likes']['count']
        else:
        	return post_info['response']['wall'][0]['text']

last_id = get_id_of_recent_post()


f = open("top.html", 'r')
html_doc = f.read()
soup = BeautifulSoup(html_doc)

links = []

max_id = 0


for link in soup.find_all('a'):
	id = int(str(re.findall('\d+$', link.get('href'))[0]))
	like = get_items_of_post(id)
	if id > max_id:
		max_id = id
	content = link.get_text()
	links.append([id, like, content])

j = 0

for i in range(max_id + 1, last_id + 1):
    if get_items_of_post(i) != []:
    	#content = get_items_of_post(i, 1)
    	#content = str(regex.sub('\?.*', "", content))
    	#content = str(regex.sub('/<br>[а-яА-Яёйы\s–№\:\#\;\-\+\w\.\(\)\,\"\\\/—\*\?\=\&«»\[\]!]+/g', "", content))
    	#content = str(regex.sub('%.*', "", content))
    	#content = str(regex.sub('http.*', "", content))
    	#content = str(regex.sub('\#[^\s]+', "", content))
    	#content = str(regex.sub('(<br>|\?)[а-яА-Яё\s–№\:\#\;\-\+\w\.\(\)\,\"\\\/—\*\?\=\&«»\[\]]*', "", content))

        links.append([i, get_items_of_post(i), get_items_of_post(i, 1)])
        j = j + 1

sorted_likes = sorted(links, key = lambda tup: tup[1], reverse = True)
f = open("new_top.html", 'w')
f.write("""<html>
    <link rel="shortcut icon" href="http://theasder.github.io/favicon.ico" type="image/icon" />
    <link rel="icon" type="image/icon" href="http://theasder.github.io/favicon.ico" />
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <meta name="description" content="Полезные материалы по всему, что может быть интересно программисту." />
    <meta name="keywords" content="программирование, веб-разработка, programming, web-development, сервисы, tools, python, regexp, git, github, проекты, прием на работу, стажировка" />
    <meta name="author" content="Artyom Dryomov" />
    <link href='http://fonts.googleapis.com/css?family=PT+Serif:400,700,400italic,700italic&subset=latin,cyrillic,cyrillic-ext,latin-ext' rel='stylesheet' type='text/css'>

<head><meta charset="UTF-8" /></head><title>Самые популярные записи в сообществе "Библиотека программиста"</title>
<link href="http://theasder.github.io/css/bootstrap.css" rel="stylesheet" />
<style type="text/css">
	a {
		line-height: 200%;
		color: black;
	}
</style>
<body>
<div class="container">
	<h3>Самые популярные контентные записи в сообществе "Библиотека программиста"</h3>""")

for item in sorted_likes:
    f.write('<a href = "http://vk.com/wall-54530371_')
    f.write(str(item[0]))
    f.write('">')
    f.write(get_items_of_post(item[0], 1))
    f.write('</a><br />')

f.write("""</div>
</body>
</html>
""")



