---
layout: post
title: "Как устроиться работать разработчиком"
date: 2016-02-06 2:00:00
description: "Полезные практические советы по подготовке к собеседованию и его прохождению."
category: job
tags: "job, interview, programming, как пройти интервью на позицию инженера-программиста, как пройти техническое собеседование, как получить работу программистом, как стать программистом"
published: true
---

<img src="http://theasder.github.io/img/459009.gif" class="img-responsive" /><br />

Полезные практические советы по подготовке к собеседованию и его прохождению.

<!-- more -->

Будьте уверены, что будете честны с собой прежде, чем отвечать на следующие вопросы: являетесь вы хорошей кандидатурой на данную должность? Как вы можете оценить свой профессионализм? В скольких компаниях вы проходили интервью? Сколько предложений о работе вы получили? 

Вы можете попробовать следующую формулу. Я придумал её смеха ради и, по сути, она ничего не значит, но если интересно:

x = количество компаний, в которых вы проходили интервью

y = количество полученных предложений

**Значение = 100 * ln(x) * y / x**

Если значение <90, вы должны прочитать эту статью. Если >120, возможно, ничего нового отсюда вы и не почерпнёте, но прочитать всё-таки не помешает.

### Кто я?

У меня нет высшего образования. Я начал профессионально программировать в 19 лет, после того, как переехал из Чикаго в Южную Калифорнию. Все, что у меня было, влезло в машину. У меня было всего 400 долларов в кармане и предложение работы за 40000 долларов в год. Это было 12 лет назад. Но это уже [другая история](https://medium.com/this-happened-to-me/four-steps-to-google-without-a-degree-8f381aa6bd5e#.rtiombt0x).

С тех пор я работал в [Double Helix](https://www.doublehelixgames.com/), [Namco Bandai](http://www.bandainamcoent.com/), [Google](https://www.google.es/), [Obvious](https://medium.com/obvious) и [Square](https://squareup.com/global/en/register). Также я получал предложения от других компаний, например, [Naughty Dog](http://www.naughtydog.com/), [Activision](https://www.activision.com/), [Riot Games](http://www.riotgames.com/), [Blizzard](http://eu.blizzard.com/ru-ru/), [Pinterest](https://fr.pinterest.com/), [Goldman Sachs](http://www.goldmansachs.com/) и т.д. Таким образом, мой результат согласно формуле &mdash; 132.

Я интервьюировал как минимум 500 кандидатов. Грубо говоря, только 10% из них получили предложение работать в компании. Менее 3% я посчитал действительно достойными кандидатами, и я помню каждого из них.

На самом деле идеального и безошибочного способа получить работу просто не существует. Есть слишком много возможных сценариев. Особенно у таких компаний, как Google, где вас будут опрашивать 5-7 рандомных разработчиков ПО. И только от них зависит, какие вопросы прозвучат во время интервью. Некоторые разработчики &mdash; просто ужасные интервьюеры, они задают сложные вопросы и делают поспешные выводы. Но это нормально, такое случается с лучшими из нас. Как показывает опыт, в данных обстоятельствах завалить одно собеседование &mdash; норма. 

Лучшее, что я могу сделать &mdash; это рассказать вам, как подготовиться надлежащим образом. Так что, без лишних слов, дам вам советы.

### Технические советы:

**1. Продолжайте программировать.** Чем больше вы программируете, тем лучше. Программируя, вы практикуетесь. Но лучшая практика &mdash; это целенаправленная практика. Держите цели в своей голове, изучайте новое, и мотивируйте себя. Через некоторое время вы должны сделать портфолио законченных и незаконченных проектов. GitHub &mdash; это отличное место для размещения портфолио.

**2. Совершенствуйте хотя бы один мультипарадигмальный язык.** Совершенствование языка дает вам чувство перспективы. Чтобы сделать это, вам нужно много программировать, много читать, и изучить все тонкости и практики. Хороший выбор для начала &mdash;  C#, C++, Java, PHP, Python, и Ruby.

Есть главный вопрос, который интервьюеры C++ любят задавать кандидатам: “По шкале от 1 до 10, где 10 &mdash; это самая высокая отметка, насколько вы оцените свои знания C++?”. Я ненавижу этот вопрос. И Бог в помощь тем, кто ответит 9-10, потому что интервьюеры выпустят когти. Сам Бьёрн Страуструп ответил бы 8 или меньше. Язык слишком сложный и богатый, и постоянно развивается. 

**3. Знайте свои слабости.** [Прочитайте этот список.](http://bigocheatsheet.com/) Затем, убедитесь, что вы понимаете, как все это работает. Затем, выполните базовые вычислительные алгоритмы, такие как алгоритм Дейкстры, алгоритм Флойда — Уоршелла, задача коммивояжёра, алгоритм A*, фильтр Блума, итеративный поиск в ширину, бинарный поиск, k-way merge, сортировка пузырьком, вставками, выбором, in-place quick sort, блочная/поразрядочная сортировка, алгоритм двух ближайших точек и т.д. И снова &mdash; продолжайте программировать. [Вот еще одна хорошая статья.](http://discrete.gr/complexity/)

**4. Изобретайте колесо.** Вы должны реализовать самые общие структуры данных в выбранном вами языке. Не полагайтесь на общие библиотеки. Реализуйте следующее и напишите тесты: вектор (динамический массив), связанный список, стек, очередь, замкнутая очередь, хэш-карта, набор, приоритетная очередь, дерево бинарного поиска и т.д. Вы должны быть готовы реализовать их быстро.

**5. Решайте задачи.** Забудьте о [таких вопросах.](https://www.google.es/search?q=google+programming+interview+questions&gws_rd=cr&ei=eq60VrTCF8eiU87ji-gG). Все сводится к фундаментальным понятиям программирования. Потратьте хотя бы 40 часов на программирование, решая разные задачи. Один из лучших ресурсов &mdash; TopCoder. [Прочитайте это.](https://www.topcoder.com/community/data-science/data-science-tutorials/) Затем, попробуйте решать задачи. Выберите те, которые проверяют вашу способность реализовывать рекурсивные алгоритмы, динамическое программирование и задачи с графами. [Архив с задачами.](https://community.topcoder.com/tc?module=MatchList)

Это, полагаю, одна из главных причин, почему меня взяли в Google. Я провел, грубо говоря, две недели на TopCoder. После этого, я мог писать алгоритм Дейкстры с закрытыми глазами. Я мог решить почти все задачи с графами. Все это благодаря повторению решения задач. А как говорит Эрик Шмидт: “Повторение не портит молитву”.

**6. Смотрите на программирование проще.** Как минимум, сделайте так, чтобы оно выглядело просто. Через некоторое время я понял, что программирование является самым простым этапом в профессии разработчика. Я часто использую фразу “простейший этап программирования”, потому что верю, что самые сложные этапы в профессии разработчика &mdash; до и после написания кода. Например, разработка того, что вы собираетесь программировать и проверка того, что ваш код работает и выполняет все задачи. Дайте вашему интервьюеру понять, что вы знаете, что программирование является лишь инструментом для достижениея цели. 

Запомните, программирование под наблюдением может быть сложным. Найдите способ практиковать написание кода на доске и парное программирование. Google обычно использует эти способы. Подробнее об этом вы можете прочитать в [статье](https://medium.com/@dpup/whiteboarding-4df873dbba2e#.uvtcftdaz) моего друга и бывшего коллеги Дэна.

### Общие советы:

Я не могу утверждать, что я эксперт. На самом деле, некоторые бы сказали, что я не очень хорошо лажу с людьми. Но я должен дать вам несколько нетехнических советов. Полагаю, что некоторые их них будут для вас очевидны.

**1. Осознайте, зачем вы здесь.** Если вы на собеседовании в компании и не совсем понимаете, зачем она нужна, кто эти люди и что они делают; уходите оттуда. Разработчики, которые отвечают за набор сотрудников, учуют это за версту. Вы можете уйти только из больших компаний, в маленьких такое не пройдет. 

**2. Будьте увлечены чем-то.** Если вам без разницы, всем без разницы. Будьте увлечены чем-то. Это может программирование, но а если конкретнее? Нравится ли вам разрабатывать компиляторы в свободное время? Строите ли вы квадрокоптеры? Если вы увлечены чем-то, постепенно вы становитесь экспертом в этой области. 

**3. Не делайте предположений.** Спросите, если в чем-то сомневаетесь. Если у вас есть вопрос и вы не знаете точного ответа, спросите. Несколько раз я видел кандидатов, которые пошли по не той дороге, никогда ничего не спрашивали и в результате тратили время на решение неверных проблем.

**4. Улыбайтесь.**  Будьте радостными и позитивными. Но не переусердствуйте. Я замечал, что люди любят делать поспешные выводы. Будьте уверены, что вы производите хорошее впечатление. Улыбка заразительна. Я часто приходил на интервью в плохом настроении или просто загруженным, но улыбка кандидата быстро поднимала мне настроение. 

Как я уже сказал, нет безошибочного способа получить работу. Но, как разработчик, лучшее, что вы можете сделать &mdash; продолжайте программировать.

Перевод: Софья Лепёхина

[Источник](https://medium.com/@davidbyttow/abc-always-be-coding-d5f8051afce2#.gri8ogqwo)

**Читайте также:**

[Как я стал веб-разработчиком за 5 месяцев](http://theasder.github.io/job/2016/01/27/how-I-became-a-web-developer-in-5-months.html)

[Подготовка к интервью на позицию разработчика ПО](http://theasder.github.io/job/2016/01/20/what-is-the-best-way-to-prepate-for-software-engeneer-interview.html)

[Лучший формат для резюме](http://theasder.github.io/job/2015/06/20/the-best-formats-for-a-resume.html)