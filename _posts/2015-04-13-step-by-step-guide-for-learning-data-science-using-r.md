---
layout: post
title: "Пошаговое руководство для изучения Data Science на R"
date: 2015-04-13
category: learning
tags: [r, data science, big data]
description: "Пособие по R, которое поможет начать изучение с нуля и пройти этот путь быстро и эффективно."
published: true
---
<img src="http://theasder.github.io/img/data.jpg" class="img-responsive" /><br/>

Для людей, столкнувшихся лицом к лицу с R существует одна общая проблема — это отсутствие структурированного плана изучения. Они не знают, с чего начать, куда двигаться, какой путь выбрать. А огромное количество информации по этой теме в Сети, зачастую, лишь сбивает с толку.

После перебирания бесконечных ресурсов и архивов, получилось данное всеобъемлющее пособие по R, которое поможет начать изучение «с нуля» и пройти этот путь быстро и эффективно.

## **Шаг 0: Подготовка**

Прежде, чем отправиться в путь, ответьте для себя на вопрос: почему R? Как он сможет помочь? Посмотрите [вот этот](https://www.youtube.com/watch?v=TR2bHSJ_eck) 90-секундный ролик от Revolution Analytics, чтобы понять, чем может быть полезен R. К слову, Revolution Analytics не так давно [была](http://blogs.microsoft.com/blog/2015/01/23/microsoft-acquire-revolution-analytics-help-customers-find-big-data-value-advanced-statistical-analysis/) приобретена Microsoft.

## **Шаг 1: Настройка машины**

Теперь, когда вы решились, самое время настроить машину. Первое, что нужно сделать - это загрузить базовую версию R и инструкцию по ее установке с [CRAN](http://cran.r-project.org/) — Comprehensive R Archive Network (Всеобъемлющая архивная сеть R).

Затем, можно поставить различные дополнительные библиотеки. Существует over9000 разных дополнений для R – и это может сбить с толку. Посему, мы будем руководствоваться лишь установкой базовых пакетов, для начала. По этой [ссылке](http://cran.r-project.org/web/views/) можно посмотреть библиотеки из CRAN Views. Собственно, там можно выбрать те подтипы библиотек, которые вам интересны.

Как подключать библиотеки – [смотрите здесь](http://www.r-bloggers.com/installing-r-packages/);

Некоторые важные библиотеки, о которых стоит знать – [смотрите тут](http://blog.yhathq.com/posts/10-R-packages-I-wish-I-knew-about-earlier.html);

Необходимо установить все три нижеследующих GUI вместе с зависимыми пакетами:

* Rattle – для анализа данных ([Ссылка](http://www.analyticsvidhya.com/trainings/data-mining-rattle-big-data-university/)) или `install.packages(“rattle”, dep=c(“Suggests”))`
* R Commander - для базовой статистики ([Ссылка](http://socserv.mcmaster.ca/jfox/Misc/Rcmdr/installation-notes.html)) или `install.packages(“Rcmdr”)`
* Deducer (вместе с JGR) для визуализации данных ([Ссылка](http://www.deducer.org/pmwiki/index.php?n=Main.WindowsInstallation))

Также, нужно установить [RStudio](http://www.rstudio.com/products/rstudio/download/). Работать на R в ней значительно быстрее и проще, так как RStudio позволяет писать множественные строки кода, подключать и поддерживать библиотеки и вообще более продуктивно обустроить свою рабочую среду.

**Задание:**

1. Установить R и RStudio;
2. Установить библиотеки Rcmdr, rattle и Deducer. Установить все предложенные или сопутствующие пакеты, включая GUI;
3. Загрузить эти библиотеки, используя соответсвующие команды, поочередно открыть GUI.

## **Шаг 2: Изучение основ языка R**

Чтобы начать, необходимо постичь основы R, его библиотек и структуры данных. Начать изучение лучше всего с [Datacamp](https://www.datacamp.com/). Особое внимание обратите на бесплатный курс введения в R ([вот тут можно почитать](https://www.datacamp.com/courses/introduction-to-r)). К концу этого курса вы сможете писать небольшие скрипты на R, а также понять принципы анализа данных. В качестве альтернативы, можно пройти «Школу программирования на R» вот [здесь](http://tryr.codeschool.com/).

Если вы хотите изучать R офлайн в свободное время, можно использовать интерактивный пакет со [Swirlstats](http://swirlstats.com).

Особое внимание следует уделить изучению read.table, структур данных, таблиц, сводок, описаний, загрузки и установки библиотек, визуализации данных с использованием команд.

**Задание:**

1. Подписаться на ежедневную рассылку, относительно проекта R [здесь](http://r-bloggers.com);
2. Создать аккаунт на [Github](http://github.com);
3. Учиться разбираться с установкой проблемных библиотек, используя Google для справки;
4. Установить swirl-пакеты (см. выше) и изучать программирование на R;
5. Черпать знания с [Datacamp](https://www.datacamp.com/).

Дополнительные источники: 

Если интерактивное программирование &mdash; не ваш стиль, можно смотреть двухминутные туториалы по R [тут](http://www.twotorials.com/). Данный видеокурс частично затрагивает поднятые здесь вопросы. Также, можно ознакомиться с [этим постом](http://decisionstats.com/2013/11/24/50-functions-to-clear-a-basic-interview-for-business-analytics-rstats/), чтобы получить более ясное представление о функциях языка R.

## **Шаг 3: Управление данными**

Вам придется много с этим работать для чистки данных, особенно, если доведется обрабатывать текстовую информацию. Самое правильное, что можно сделать для начала – это пройти соответствующие упражнения. О соединенении с базами данных можно узнать с помощью библиотеки [RODBC](http://cran.r-project.org/web/packages/RODBC/index.html), а о написании sql-запросов к структурам данных через [sqldf](https://code.google.com/p/sqldf/).

**Задание:**

1. Почитайте о разделенном, прикладном и комбинированном подходах к анализу данных в [Journal of Statisical Software](http://www.jstatsoft.org/v40/i01/paper);
2. Попытайтесь изучить подход "[аккуратных данных](http://www.jstatsoft.org/v59/i10/paper)" для проведения анализа;
3. Почитайте о работе R с реляционными базами данных в [статье](http://decisionstats.com/2011/10/16/using-r-with-mysql/) на decisionstats.com;
4. Сделайте несколько [упражнений](http://decisionstats.com/2013/06/12/data-munging-using-rstats-part-1-understanding-data-quality/) на понимание качества данных;
5. Не сидите только на анализе цифр. Разберите с помощью R спортивную аналитику на [примере](http://decisionstats.com/2013/04/25/using-r-for-cricket-analysis-rstats-ipl/) крикета.

Если вам нужно больше практики, на Datacamp можно [оформить](https://www.datacamp.com/subscriptions/r-programmer-and-data-analyst) подписку на все обучающие программы за $25/месяц. Но начать стоит с введения в plyr вот [здесь](http://courses.had.co.nz/09-user/).

## **Шаг 4: Изучение специализированных библиотек data.table и dplyr**

Вот здесь и начинается самая веселая часть! Ниже – рекомендации к прочтению и выполнению. Практику начнем с некоторых общих операций.

* Основательно изучите [учебное пособие по data.table](http://user2014.stat.ucla.edu/files/tutorial_Matt.pdf). Распечатайте и заучите [шпаргалку](http://blog.datacamp.com/data-table-cheat-sheet/) по data.table;
* Затем, можно взглянуть на [туториал по dplyr](http://rpubs.com/justmarkham/dplyr-tutorial);
* Чтобы понять основы анализа текста, сделайте [облако слов на R](http://www.analyticsvidhya.com/blog/2014/05/build-word-cloud-text-mining-tools/), потом пройдите следующий курс по неструктурированным данным: [часть раз](http://www.analyticsvidhya.com/blog/2014/08/step-step-guide-extract-inforation-free-text-unstructured-data/), [часть два](http://www.analyticsvidhya.com/blog/2014/08/understanding-analyzing-hidden-structures-unstructured-dataset/);
* Для понимания анализа социальных сетей, следует прочесть [эту статью](http://web.stanford.edu/~messing/RforSNA.html);
* Сделайте анализ настроений, используя данные Твиттера, как, например, [здесь](http://www.analyticsvidhya.com/blog/2014/07/world-cheering-2014-fifa-wc-winner-twitter/) и [здесь](http://www.slideshare.net/ajayohri/twitter-analysis-by-kaify-rais);
* По оптимизации с помощью R почитайте [это](http://www.magesblog.com/2013/03/how-to-use-optim-in-r.html) и [это](http://cran.r-project.org/web/views/Optimization.html).

Дополнительные источники:

* Если вам нужна книга по бизнес-аналитике на R, то [вот](http://www.amazon.com/R-Business-Analytics-A-Ohri/dp/1461443423) — "R for Business Analytics" от Аджая Ори;
* Если нужна книга для изучения R по-быстрому, то ее можно найти [тут](http://statmethods.net/).

## **Шаг 5: Увеличение эффективности визуализации данных с помощью ggplot2**

1. Почитайте об Эдварде Тафте и его мыслях о том, как стоит (и не стоит) делать визуализацию данных [здесь](http://thedoublethink.com/2009/08/tufte’s-principles-for-visualizing-quantitative-information/).
2. Также, почитайте о подводных камнях при разработке дашбордов в [материале](http://www.perceptualedge.com/articles/Whitepapers/Common_Pitfalls.pdf) Стивена Фью.
3. Освойте грамотное построение графиков и практические способы их построения на R. По [ссылке](http://courses.had.co.nz/10-tokyo/) доступен курс по ggplot2 от доктора Хардли Уикхэма, создателя ggplot2 — одной из самых лучших библиотек для R на сегодняшний день.
4. Если вы заинтересованы в пространственной визуализации данных, не проходите мимо библиотеки [ggmap](http://journal.r-project.org/archive/2013-1/kahle-wickham.pdf).
5. Если интересуетесь анимацией данных, взгляните на [эти](http://vis.supstat.com/categories.html# animation-ref) примеры. Взять библиотеку для анимации можно [здесь](http://yihui.name/animation/).
6. С помощью [Slidify](http://slidify.org/samples/intro/# 1) можно визуализировать данные в виде слайдов на HTML5.

## **Шаг 6: Data Mining и машинное обучение**

Сейчас мы подошли к наиболее ценным для аналитика навыкам – глубокому анализу и машинному обучению. Исчерпывающий набор информации о глубоком анализе с помощью R можно найти на [RDM](http://www.rdatamining.com). А так же свободно распространяемую и простую для понимания книгу по этой теме за авторством Грэхэма Уильямса можно найти [здесь](http://togaware.com/datamining/survivor/index.html).

Обзор таких алгоритмов, как регрессия, дерева решений, ансамбли моделирования и кластеризация, а также опции для машинного обучения, доступные в R можно найти по [этой](http://cran.r-project.org/web/views/MachineLearning.html) ссылке.

Дополнительные источники:

* "Data Mining with Rattle and R" — [хорошая книга](http://www.amazon.com/gp/product/1441998896/ref=as_li_qf_sp_asin_tl?ie=UTF8&tag=togaware-20&linkCode=as2&camp=217145&creative=399373&creativeASIN=1441998896) по глубокому анализу данных.
* Почитать о прогнозировании временных рядов на R можно [тут](http://a-little-book-of-r-for-time-series.readthedocs.org/en/latest/src/timeseries.html).
* Кое-что по машинному обучению в R есть [здесь](http://www.dataschool.io/15-hours-of-expert-machine-learning-videos/), а так же [здесь](https://class.stanford.edu/courses/HumanitiesScience/StatLearning/Winter2014/about) можно записаться на бесплатные курсы.

## **Шаг 7: Практика, практика и еще раз практика**

Поздравления! Вы добились своего. Теперь у вас есть все что нужно, осталось оттачивать технические навыки.

1. Итак, теперь необходимо практиковаться и для этого как нельзя лучше подойдут соревнования с коллегами-аналитиками на Kaggle. Начать этот практический курс можно [отсюда](https://www.kaggle.com/c/titanic-gettingStarted).
2. О более продвинутых исследованиях с Kaggle можно узнать [здесь](http://0xdata.com/blog/2014/09/r-h2o-domino/).
3. Оставаться на связи с коллегами по R-цеху можно подписавшись на [R-bloggers](http://www.r-bloggers.com/).
4. Для большего социального взаимодействия, можно использовать в Твиттере хештег [# rstats](https://twitter.com/search?q=%23rstats&src=typd).
5. Если на чем-то застряли – этот [сайт](http://www.statmethods.net/) поможет быстро разобраться и даст нужное количество информации.

## **Шаг 8: Сложные темы**

Теперь, когда вы знаете об анализе данных с помощью R все, что нужно, настало время получить некоторые дополнительные задания. Есть вероятность, что кое-что из этого вы уже видели, но, все же, ознакомьтесь с этими материалами тоже.

1. Об использовании R и Hadoop можно узнать в [этом туториале](http://hortonworks.com/hadoop-tutorial/using-rhadoop-to-predict-visitors-amount/).
2. Занятие на тему совместного использования R и MongoDB есть [тут](https://gist.github.com/Btibert3/7751989).
3. Еще один хороший [материал](http://cdn.oreillystatic.com/en/assets/1/event/102/Big%20Data%20Analyses%20with%20R%20Presentation.pdf) по анализу Больших Данных с помощью R в NoSQL-эру.
4. К слову, используя [Shiny](http://rstudio.github.io/shiny/tutorial/) из RStudio, можно сделать интерактивное веб-приложение.
5. Гайд для интересующихся в изучении синтаксиса R и Python [здесь](http://www.slideshare.net/ajayohri/python-for-r-users).

**P.S. В случае, если вам приходится много работать с большими данными, взгляните на библиотеку [RevoScaleR](https://gist.github.com/joseph-rickert/4742529) от Revolution Analytics. Это коммерческая библиотека, но она бесплатна для академического пользования. Пример проекта приведен [здесь](http://www.slideshare.net/Wyendrila/forecasting-analysis-on-us-flights-v1)**

[Первоисточник](http://www.analyticsvidhya.com/learning-paths-data-science-business-analytics-business-intelligence-big-data/learning-path-r-data-science/)

**Перевод подготовил Сергей Ворничес**
