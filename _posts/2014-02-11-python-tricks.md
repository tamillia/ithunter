---
layout: post
title: "Интересные приёмы на языке программирования Python"
date: 2014-02-11 17:15:25
category: python
tags: [приемы, языки программирования]
published: true
---

<img src="https://www.python.org/static/community_logos/python-logo-master-v3-TM.png" class="img-responsive" /><br />

Генератор списков и выражений.

Вместо использования цикла для задания списка

{% highlight python linenos %}
>>> b = []
>>> for x in range(10):
b.append(10 * x)
>>> b
[0, 10, 20, 30, 40, 50, 60, 70, 80, 90]
{% endhighlight %}

можно использовать генератор списков

{% highlight python linenos %}
>>> [10 * x for x in range(10)]
[0, 10, 20, 30, 40, 50, 60, 70, 80, 90]
{% endhighlight %}

также Python 2.7 поддерживает генераторы словарей и множеств:

{% highlight python linenos %}
>>> {x: 10 * x for x in range(5)}
{0: 0, 1: 10, 2: 20, 3: 30, 4: 40}
>>> {10 * x for x in range(5)}
set([0, 40, 10, 20, 30])
{% endhighlight %}

Интересные приёмы с zip.

Транспонировать матрицу:

{% highlight python linenos %}
>>> l = [­[1, 2, 3], [4, 5, 6]]
>>> zip(*l)
[(1, 4), (2, 5), (3, 6)]
{% endhighlight %}

Разделение списка на группы из n элементов:

{% highlight python linenos %}
>>> l = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5, 8]
>>> zip(*([iter(l)] * 3))
[(3, 1, 4), (1, 5, 9), (2, 6, 5), (3, 5, 8)]
{% endhighlight %}

А также:

{% highlight python linenos %}
>>> import this
The Zen of Python, by Tim Peters

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one— and preferably only one —obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea — let's do more of those!
{% endhighlight %}

Простой HTTP сервер может быть запущен за секунды:
для python 2.7

{% highlight python linenos %}
>>> python -m SimpleHTTPServer
{% endhighlight %}

для python 3

{% highlight python linenos %}
>>> python3 -m http.server
{% endhighlight %}

Сервер запускается на порте 8080 по умолчанию, но это можно изменить. 

Найти самую длинную строчку в файле:

{% highlight python linenos %}
>>> max(open('test.txt'), key=len)
{% endhighlight %}

Сумма цифр беззнакового целого числа:

{% highlight python linenos %}
>>> sum(map(int, str(n)))
{% endhighlight %}

Искрографы можно строить с помощью [кода, приведенного по ссылке](https://gist.github.com/stefanv/1371985)

Примеры:

{% highlight python linenos %}
spark 1,5,22,13,53
▁▁▃▂▇
spark 0 30 55 80 33 150 
▁▂▃▅▂▇
spark 0.1 0.2 0.9 -0.5
▄▅█▁
{% endhighlight %}

Также можно задавать бесконечность в Python:

{% highlight python linenos %}
>>> my_inf = float('Inf')
>>> 99999999999 > my_inf
False
>>> my_neg_inf = float('-Inf')
>>> my_neg_inf > -9999999999
False
{% endhighlight %}

Попробуйте набрать эту строчку:

{% highlight python linenos %}
import antigravity
{% endhighlight %}

Менять значения переменных между собой:

{% highlight python linenos %}
a, b = b, a
{% endhighlight %}

Интуитивно понятные сравнения:

{% highlight python linenos %}
>>> x = 2
>>> 3 > x == 1
False
>>> 1 < x < 3
True
>>> 10 < 10*x < 30 
True
>>> 10 < x**5 < 30 
False
>>> 100 < x*100 >= x**6 + 34 > x <= 2*x <5
True
{% endhighlight %}

Обратный порядок.
Создать новый массив, элементы которого записаны в обратном порядке элементов старого массива

{% highlight python linenos %}
>>> mylist = [1,2,3]
>>> mylist.reverse()
>>> mylist
[3,2,1]
{% endhighlight %}

Распечатать в обратном порядке:

{% highlight python linenos %}
>>> for element in reversed([1,2,3]): 
print element
3
2
1
{% endhighlight %}

Можно также для обратного порядка использовать [::-1]

{% highlight python linenos %}
>>> "Hello world"[::-1]
'dlrow olleH'
>>> [1,2,3][::-1]
[3, 2, 1]
{% endhighlight %}

Автоматическая распаковка данных.

{% highlight python linenos %}
>>> def foo(a, b, c):
print a, b, c
>>> mydict = {'a':1, 'b':2, 'c':3}
>>> mylist = [10, 20, 30]
>>> foo(*mydict)
a c b
>>> foo(** mydict)
1 2 3
{% endhighlight %}

Возможность пронумеровать элементы:

{% highlight python linenos %}
>>> class PlayerRanking:
Bolt, Green, Johnson, Mom = range(4) 
>>> PlayerRanking.Mom
3
>>> PlayerRanking.Bolt
0
{% endhighlight %}

Словарь(это такое название структуры данных) очень удобен для размещения переключателей частоиспользуемых операций. Например, можно сделать простенький калькулятор:

{% highlight python linenos %}
>>> calculator = {
'plus': lambda x, y: x + y,
'minus': lambda x, y: x - y
}
>>> calculator['minus'](9,3)
6
{% endhighlight %}
