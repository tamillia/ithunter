---
layout: post
title: "11 наиболее часто используемых фрагментов кода на питоне"
date: 2015-09-16 18:42:43
category: python
tags: [python, snippets, code, examples]
published: true
---
<img src="https://theasder.github.io/img/pylogo.png" class="img-responsive" /><br />

Python &mdash; один из наиболее популярных языков программирования, [превзошедший по популярности по индексу TIOBE язык PHP](http://www.tiobe.com/index.php/content/paperinfo/tpci/index.html).
Синтаксис Python может показаться странным по началу, особенно для разработчиков на Java. Некоторые фрагменты кода используются довольно часто, но для новичков их воспроизведение может оказаться не под силу. Такие фрагменты называют «идиомами». Их прочтение может оказаться зачастую полезным для изучения нового языка программирования. В этой статье мы познакомим вас с некоторыми из наиболее популярными фрагментами кода.

<!-- more -->

## Фильтруем список

    # убираем пустые строки в списке
    list = [x for x in list if x.strip() != '']
    # или
    list = filter(lambda x: len(x) > 0, list)
    
## Читаем файл строчкой за строчкой

    with open("/путь/к/файлу") as f:
        for line in f:
            print line
    
## Ищем совпадения с помощью регулярного выражения

    sentence = "this is a test, not testing."
    it = re.finditer('\\btest\\b', sentence)
    for match in it:
        print "match position: " + str(match.start()) + "-" + str(match.end())
        

## Поиск с помощью регулярного выражения

    m = re.search('\d+-\d+', line) # ищем строки, совпадающие по шаблону "число-число"
    if m:
        current = m.group(0)
        
## Кидаем запрос в базу данных

    db = MySQLdb.connect("localhost", "username", "password", "dbname")
    cursor = db.cursor()
    sql = "select Column1, Column2 from Table1"
    cursor.execute(sql)
    results = cursor.fetchall()
     
    for row in results:
        print row[0] + row[1]
     
    db.close()
    
## Соединяем элементы списка воедино с помощью заданного разделителя

    theList = ["a", "b", "c"]
    joinedString = ",".join(theList)
    
## Убрать из списка элементы-дупликаты

    targetList = list(set(targetList))
    
## Прикрепить один список к другому

    anotherList.extend(aList)
    
## Итерировать словарь

    for k, v in aDict.iteritems():
        print(k+v)

## Проверить присутствует ли какой-нибудь элемент из списка строк в заданной строке

    if any(x in targetString for x in aList):
        print("true")
        

