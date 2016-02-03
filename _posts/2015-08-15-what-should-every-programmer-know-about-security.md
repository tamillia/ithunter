---
layout: post
title: "Что полезно знать о безопасности каждому программисту?"
date: 2015-08-15 09:27:34
category: development
tags: [security, tips]
description: "Базовые знания о безопасности, которые нужно знать каждому программисту."
published: true
---
<img src="https://pp.vk.me/c543107/v543107696/45d9/WFkpd0ZfWV0.jpg" class="img-responsive" /><br />

Никто не может знать всего о безопасности, но существуют ли некоторые минимальные знания, которые было бы полезно знать каждому программисту? Какие книги или статьи помогут начать разбираться в этой теме? Обо всём этом в этой статье. 

<!-- more -->

Принципы, которым полезно следовать, если вы хотите писать безопасные приложения:
<ul>
<li>Никогда не доверяйте вводу! </li>
<li><a href="http://www.ibm.com/developerworks/library/l-sp2.html">Проверяйте на валидность ввод</a> от недостоверных источников: используйте <a href="https://en.wikipedia.org/wiki/Whitelist">белые списки</a>, а не черные.</li>
<li>Планируйте заранее работу с безопасностью, а не занимайтесь этим в конце.</li>
<li>Делайте код простым - увеличение сложности увеличит вероятность появления дырок в безопасноти</li>
<li>Старайтесь свести <a href="https://ru.wikipedia.org/wiki/%D0%9F%D0%BE%D0%B2%D0%B5%D1%80%D1%85%D0%BD%D0%BE%D1%81%D1%82%D1%8C_%D0%B0%D1%82%D0%B0%D0%BA%D0%B8">поверхность атаки</a> к минимуму</li>
<li>Удостоверьтесь, <a href="http://www.owasp.org/index.php/Fail_securely">что если ваше приложение упадет, то это будет безопасно</a></li>
<li>Используйте <a href="https://buildsecurityin.us-cert.gov/bsi/articles/knowledge/principles/347-BSI.html">глубинную защиту</a></li>
<li>Придерживайтесь принципа <a href="https://buildsecurityin.us-cert.gov/bsi/articles/knowledge/principles/351-BSI.html">наименьшей привилегии</a>  </li>
<li><a href="http://www.owasp.org/index.php/Threat_Risk_Modeling">Моделируйте угрозу</a></li>
<li><a href="http://www.cgisecurity.com/owasp/html/ch04s09.html">Пользуйтесь принципом изолирования</a> &mdash; таким образом ваша система это не «все или ничего»</li>
<li>Трудно спрятать секретную информацию: секретная информация, спрятанная в коде, вряд ли будет секретной долгое время.</li>
<li>Не пишите свой шифратор.</li>
<li>Использование шифратора не означает, что вы в безопасноти (хакеры будут в поисках слабой ссылки)</li>
<li>Остерегайтейсь <a href="http://www.linuxjournal.com/article/6701">переполнения буфера</a></li>
</ul>

<p>Существуют замечательные книги и статьи о том, как сделать ваши приложения безопасными: </p>

<ul>
<li><a href="http://rads.stackoverflow.com/amzn/click/0735617228"><strong>Writing Secure Code 2nd Edition</strong></a> &mdash; наверно, каждому разработчику стоило бы ее прочитать</li>
<li><a href="http://rads.stackoverflow.com/amzn/click/020172152X">Building Secure Software: How to Avoid Security Problems the Right Way </a></li>
<li><a href="http://rads.stackoverflow.com/amzn/click/0596003943">Secure Programming Cookbook</a></li>
<li><a href="https://docs.google.com/viewer?url=http://www.usenix.org/events/sec04/tech/slides/mcgraw.pdf">Exploiting Software</a></li>
<li><a href="http://www.cl.cam.ac.uk/~rja14/book.html">Security Engineering</a> &mdash; отличная книга</li>
<li><a href="http://www.dwheeler.com/secure-programs/Secure-Programs-HOWTO/index.html">Secure Programming for Linux and Unix HOWTO</a></li>
</ul>


<a href="http://stackoverflow.com/questions/2794016/what-should-every-programmer-know-about-security">Источник</a>

**Перевод: Артём Дрёмов**

