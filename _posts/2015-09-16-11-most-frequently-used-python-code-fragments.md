---
layout: post
title: "11 наиболее часто используемых фрагментов кода на Python"
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


{% highlight python linenos %}
# убираем пустые строки в списке
list = [x for x in list if x.strip() != '']
# или
list = filter(lambda x: len(x) > 0, list)
{% endhighlight %}

## Читаем файл строчкой за строчкой


{% highlight python linenos %}
with open("/путь/к/файлу") as f:
    for line in f:
        print line
{% endhighlight %}
   
## Ищем совпадения с помощью регулярного выражения


{% highlight python linenos %}
sentence = "this is a test, not testing."
it = re.finditer('\\btest\\b', sentence)
for match in it:
    print "match position: " + str(match.start()) + "-" +   str(match.end())
{% endhighlight %}      

## Поиск с помощью регулярного выражения

{% highlight python linenos %}
m = re.search('\d+-\d+', line) # ищем строки, совпадающие по шаблону "число-число"
if m:
    current = m.group(0)
{% endhighlight %}
       
## Кидаем запрос в базу данных

{% highlight python linenos %}
db = MySQLdb.connect("localhost", "username", "password", "dbname")
cursor = db.cursor()
sql = "select Column1, Column2 from Table1"
cursor.execute(sql)
results = cursor.fetchall()
 
for row in results:
    print row[0] + row[1]
 
db.close()
{% endhighlight %}
   
## Соединяем элементы списка воедино с помощью заданного разделителя

{% highlight python linenos %}
theList = ["a", "b", "c"]
joinedString = ",".join(theList)
{% endhighlight %}
  
## Убрать из списка элементы-дупликаты

{% highlight python linenos %}
targetList = list(set(targetList))
{% endhighlight %}
    
## Прикрепить один список к другому

{% highlight python linenos %}
anotherList.extend(aList)
{% endhighlight %}
  
## Итерировать словарь

{% highlight python linenos %}
for k, v in aDict.iteritems():
    print(k+v)
{% endhighlight %}

## Проверить присутствует ли какой-нибудь элемент из списка строк в заданной строке

{% highlight python linenos %}
if any(x in targetString for x in aList):
    print("true")
{% endhighlight %}
     
        
[Источник](http://www.programcreek.com/2015/05/most-frequently-used-python-code-fragments-for-java-developers/)
        

