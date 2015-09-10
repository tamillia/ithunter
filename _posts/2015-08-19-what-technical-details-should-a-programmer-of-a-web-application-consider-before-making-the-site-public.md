---
layout: post
title: "Какие детали полезно знать каждому программисту перед тем, как сделать сайт доступным для широкой публики?"
date: 2015-08-19 10:02:34
category: development
tags: [web, tips, production, release]
published: true
---
<img src="http://webplanet.com.ua/uploads/services/3_%D0%92%D0%B5%D0%B1-%D1%85%D0%BE%D1%81%D1%82%D0%B8%D0%BD%D0%B3.jpg" class="img-responsive" />

<!-- more -->

<p>По идее большинство из нас <em>уже</em> в курсе <em>большинства вещей</em> в этом списке.  Но существует один или два пункта, которые вы могли не изучать до этого, либо не до конца понимаете, либо вовсе не слышали.</p>

<h2>Интерфейс и User Experience</h2>

<ul>
<li>Держитесь в курсе того, как непоследовательно браузеры реализуют стандарты и удостоверьтесь, что сайт работает разумно на всех основных браузерах. Как минимум, протестируйте на последнем браузере на движке  <a href="https://en.wikipedia.org/wiki/Gecko_%28layout_engine%29">Gecko</a> (Например, на <a href="http://firefox.com/">Firefox</a>), на движке WebKit (Например, на <a href="http://www.apple.com/safari/">Safari</a> или мобильных браузерах), <a href="http://www.google.com/chrome">Chrome</a>, и что сайт нормально отображается на <a href="https://en.wikipedia.org/wiki/Internet_Explorer">IE</a> (воспользуйтесь <a href="http://www.microsoft.com/Downloads/details.aspx?FamilyID=21eabb90-958f-4b64-b5f1-73d0a413c8ef&amp;displaylang=en">Application Compatibility VPC Images</a>), а также на <a href="http://www.opera.com/">Opera</a>. Также посмотрите на то, как <a href="http://www.browsershots.org">браузеры отображают ваш сайт</a> на разных операционных системах.</li>
<li>Проверьте, как люди будут использовать ваш сайт в других браузерах: на телефонах, ридерах. — Некоторая информация о доступности здесь: <a href="http://www.w3.org/WAI/">WAI</a> и <a href="http://www.section508.gov/">Section508</a>, мобильная разработка: <a href="http://mobiforge.com/">MobiForge</a>.</li>
<li>Подготовка: как развернуть обновления без воздействия на ваших пользователей. Имейте одну или несколько проверок или подготовительных сред, доступных для реализации изменений архитектуры, кода или меняющегося содержания и удостоверьтесь, что они могут быть развернуты  контролируемым образом без поломок чего-либо. Имейте автоматизированный способ развертывания сделанных изменений для живого сайтаэ. Самый эффективный способ &mdash; использовать систему контроля версий (CVS, Subversion и т.д.) и автоматизированный механизм сборки (Ant, NAnt, и т.д.).</li>
<li>Не отображайте недружелюбные ошибки прямо пользователю.</li>
<li>Не отображайте прямым текстом пользовательские адреса электронные почты, потому что их заспамят.</li>
<li>Добавьте атрибут <code>rel="nofollow"</code> к сгенерированным пользователями ссылкам, <a href="https://ru.wikipedia.org/wiki/Nofollow">чтобы избежать спама</a>.</li>
<li><a href="http://www.codinghorror.com/blog/archives/001228.html">Придумайте хорошо продуманные пределы в вашем сайте</a> &mdash; это также относится и к разделу безопасности</li>
<li>Изучите как делать <a href="https://en.wikipedia.org/wiki/Progressive_enhancement">постепенные улучшения</a>.</li>
<li><a href="https://ru.wikipedia.org/wiki/Post/Redirect/Get">Перенаправляйте запрос после POST-запроса</a>, если тот POST-запрос был успешен, чтобы предотвратить обновление от передачи на усмотрение формы еще раз.</li>
<li>Не забывайте брать в счет доступность для всех (в том числе и для людей с ограниченными возможностями). Это всегда хорошая задумка и в некоторых обстоятельствах <a href="http://www.section508.gov/">юридическое требование</a>.  <a href="http://www.w3.org/WAI/intro/aria">WAI-ARIA</a> и <a href="http://www.w3.org/TR/WCAG20/">WCAG 2</a> &mdash; хорошие ресурсы на эту тему.</li>
<li><a href="http://www.sensible.com/dmmt.html">Не делайте непонятный для пользователя интерфейс</a></li>
</ul>

<h2>Безопасность</h2>

<ul>
<li>Полно дайджестов на эту тему, но <a href="http://www.owasp.org/index.php/Category:OWASP_Guide_Project">Гайд по разработке OWASP</a> полностью раскрывает тему безопасности сайта.</li>
<li>Изучите внедрения, особенно <a href="https://ru.wikipedia.org/wiki/%D0%92%D0%BD%D0%B5%D0%B4%D1%80%D0%B5%D0%BD%D0%B8%D0%B5_SQL-%D0%BA%D0%BE%D0%B4%D0%B0">внедрения SQL-кода</a> и то, как это предовратить.</li>
<li>Никогда не доверяйте пользовательскому вводу, ни тем более всему том, что указано в запросе (которое может включать куки и спрятанные от поля значения!).</li>
<li>Используйте пароли, используя <a href="https://security.stackexchange.com/q/21263/396">соль</a> и другие различные соли для ваших строчек в базе данных для предотвращения «радужных атак». Используйте медленный алгоритм хеширования, такой как bcrypt (проверенный временем) или scrypt (даже сильнее, но новее) (<a href="http://www.tarsnap.com/scrypt.html">1</a>, <a href="http://it.slashdot.org/comments.pl?sid=1987632&amp;cid=35149842">2</a>) для хранения паролей. (<a href="http://codahale.com/how-to-safely-store-a-password/">Посмотрите статью «Как безопасно хранить пароли»</a>). <a href="https://security.stackexchange.com/q/7689/396">организация NIST также одобряет использования PBKDF2 вместо хешированных паролей</a>, и <a href="https://security.stackexchange.com/a/2136/396">организация FIPS одобрила такой способ в .NET</a> (больше информации на эту тему <a href="https://security.stackexchange.com/questions/211/how-to-securely-hash-passwords">здесь</a>). <em>Избегайте</em> испрользования алгоритма MD5 или семейства алгоритмов SHA напрямую.</li>
<li><a href="http://stackoverflow.com/questions/1581610/how-can-i-store-my-users-passwords-safely/1581919#1581919">Не пробуйте создавать  свои собственные необычные системы аутентификации</a>. Очень легко ошибиться в хитроумных и непроверенных способах и вы даже не узнаете об этом <em>до того,</em> как вас взломают.</li>
<li>Узнайте о <a href="https://www.pcisecuritystandards.org/">правилах для обработки информации с кредитных карт</a>. (<a href="https://stackoverflow.com/questions/51094/payment-processors-what-do-i-need-to-know-if-i-want-to-accept-credit-cards-on-m">Посмотрите также этот вопрос.</a>)</li>
<li>Используйте <a href="http://www.mozilla.org/projects/security/pki/nss/ssl/draft302.txt">SSL</a>/<a href="https://ru.wikipedia.org/wiki/HTTPS">HTTPS</a> для входа и для других страниц, где вводится важная информация (например, информация о кредитной карте).</li>
<li><a href="https://en.wikipedia.org/wiki/Session_hijacking#Prevention">Предотвращайте TCP hijacking</a>.</li>
<li>Отстерегайтесь <a href="https://ru.wikipedia.org/wiki/%D0%9C%D0%B5%D0%B6%D1%81%D0%B0%D0%B9%D1%82%D0%BE%D0%B2%D1%8B%D0%B9_%D1%81%D0%BA%D1%80%D0%B8%D0%BF%D1%82%D0%B8%D0%BD%D0%B3">межсайтового скриптинга</a> (XSS).</li>
<li>Отстерегайтесь <a href="https://ru.wikipedia.org/wiki/%D0%9C%D0%B5%D0%B6%D1%81%D0%B0%D0%B9%D1%82%D0%BE%D0%B2%D0%B0%D1%8F_%D0%BF%D0%BE%D0%B4%D0%B4%D0%B5%D0%BB%D0%BA%D0%B0_%D0%B7%D0%B0%D0%BF%D1%80%D0%BE%D1%81%D0%B0">межсайтовую подделку запроса</a> (CSRF).</li>
<li>Отстерегайтесь <a href="https://ru.wikipedia.org/wiki/%D0%9A%D0%BB%D0%B8%D0%BA%D0%B4%D0%B6%D0%B5%D0%BA%D0%B8%D0%BD%D0%B3">кликджекинга</a>.</li>
<li>Держитесь в курсе последних патчей для вашей системы.</li>
<li>Удостоверьтесь, что информация о подключении к базе данных в безопасности.</li>
<li>Будьте в курсе самых последних техник атак и уязвимостей, воздействующих на вашу платформу.</li>
<li>Почитайте <a href="http://code.google.com/p/browsersec/wiki/Main">The Google Browser Security Handbook</a>.</li>
<li>Почитайте <a href="http://amzn.com/0470170778">The Web Application Hacker's Handbook</a>.</li>
<li>Рассмотрите <a href="https://ru.wikipedia.org/wiki/%D0%9F%D1%80%D0%B8%D0%BD%D1%86%D0%B8%D0%BF_%D0%BC%D0%B8%D0%BD%D0%B8%D0%BC%D0%B0%D0%BB%D1%8C%D0%BD%D1%8B%D1%85_%D0%BF%D1%80%D0%B8%D0%B2%D0%B8%D0%BB%D0%B5%D0%B3%D0%B8%D0%B9">принцип минимальных привилегий</a>. Попробуйте запустить сервер вашего приложения <a href="https://security.stackexchange.com/questions/47576/do-simple-linux-servers-really-need-a-non-root-user-for-security-reasons">не как суперпользователь</a>. (<a href="http://tomcat.apache.org/tomcat-8.0-doc/security-howto.html#Non-Tomcat_settings">пример tomcat</a>)</li>
</ul>

<h2>Производительность</h2>

<ul>
<li>Реализуйте кеширование в случае необходимости, поймите и используйте <a href="http://www.mnot.net/cache_docs/">HTTP кеширование</a> должным образом, как и <a href="http://www.w3.org/TR/2011/WD-html5-20110525/offline.html">манифест HTML5</a>.</li>
<li>Оптимизируйте картинки: не используйте изображение размером 20 KB для повторяющегося фона.</li>
<li>Изучите как сжимать содержимое с помощью <a href="http://developer.yahoo.com/performance/rules.html#gzip">gzip/deflate</a> (<strike><a href="https://stackoverflow.com/questions/1574168/gzip-vs-deflate-zlib-revisited">deflate лучше</a></strike>).</li>
<li>Комбинируйте/соединяйте несколько CSS-файлов или несколько скриптов в один, чтобы уменьшеить количество соединений с браузером и улучшить способность gzip сжимать дупликаты среди файлов.</li>
<li>Посмотрите на <a href="http://developer.yahoo.com/performance/">подборку материалов от Yahoo по производительности</a>, включающую хорошие требования и производительность фронт-енда и их инструмент <a href="http://developer.yahoo.com/yslow/">YSlow</a> (для использования нужны Firefox, Safari, Chrome или Opera). Также <a href="https://developers.google.com/speed/docs/best-practices/rules_intro">Google page speed</a> (используйте <a href="https://developers.google.com/speed/pagespeed/insights_extensions">дополенение к браузеру</a>) &mdash; другой инструмент для проверки производительности и он оптимизирует изображения тоже.</li>
<li>Используйте <a href="http://alistapart.com/articles/sprites">CSS Image Sprites</a> для маленьких изображений как тулбары (обратите внимание на пункт "минимизация HTTP запросов")</li>
<li>Для разработки деловых веб-сайтов рассмотрите <a href="http://developer.yahoo.com/performance/rules.html#split">разделение компонент среди доменов</a>.</li>
<li>Статический контент (такие как картинки, CSS, JavaScript и общее содержание, не нуждающееся в куки) должно идти на отдельный домен, <em><a href="http://blog.stackoverflow.com/2009/08/a-few-speed-improvements/">который не нуждается в куки</a></em>, потому что все куки для домена и его поддоменов посылаются с каждым запросом к домену и поддомену. Одна хорошая опция здесь &mdash; это использовать Content Delivery Network (CDN), но рассмотрим случай, где CDN может упасть вместе со всеми альтернативыми CDN или локальные копии, которые могут быть доставлены вместо этого.</li>
<li>Минимизируйте общее число HTTP-запросов, которые нужны браузеру для показа вашей страницы.</li>
<li>Используйте <a href="http://developers.google.com/closure/compiler/">компилятор Closure от Google</a> для JavaScript'a и <a href="http://developer.yahoo.com/yui/compressor/">другие инструменты минификации</a>.</li>
<li>Удостоверьтесь, что у вас есть файл <code>favicon.ico</code> в корневой папке вашего сайта, т.е. <code>/favicon.ico</code>. <a href="http://mathiasbynens.be/notes/rel-shortcut-icon">Браузеры будут автоматически запрашивать его</a>, даже если иконка не указана в HTML совсем. Если у вас нет <code>/favicon.ico</code>, то в результате будет много вызвано страниц 404, что повлияет на пропускную способность вашего сервера.</li>
</ul>

<h2>SEO (Поисковая оптимизация)</h2>

<ul>
<li>Используйте "дружелюбные для поисковика" URL'ы, например, <code>example.com/pages/45-article-title</code> вместо <code>example.com/index.php?page=45</code></li>
<li>Когда используется <code>#</code> для динамического контента, измените <code>#</code> на <code>#!</code>, и тогда на сервере <code>$_REQUEST["_экранированный_фрагмент_"]</code> &mdash; это то, что гуглбот использует вместо <code>#!</code>. Другими словами <code>./#!page=1</code> становится <code>./?_экранированные_фрагменты_=page=1</code>. Также для пользователей, использующих FF.b4 или Chromium, <code>history.pushState({"foo":"bar"}, "About", "./?page=1");</code> &mdash; хорошая команда. Таким образом, даже если адресная строка изменилась, страница не обновляется заново. Это позволяет использовать  <code>?</code> вместо <code>#!</code>, чтобы оставить в покое меняющееся содержание.
</li>
<li>Не используйте ссылки, которые пишут что-то вроде <a href="https://ux.stackexchange.com/questions/12100/why-shouldnt-we-use-the-word-here-in-a-textlink">"нажмите здесь"</a>. Вы тратите впустую возможность поискового продвижения и такие ссылки усложняют жизнь людям со screen reader'ами.</li>
<li>Сделайте <a href="http://www.sitemaps.org/">карту сайта на XML</a>, желательно в корневой папке <code>/sitemap.xml</code>.</li>
<li>Используйте <a href="http://googlewebmastercentral.blogspot.com/2009/02/specify-your-canonical.html"><code>&lt;link rel="canonical" ... /&gt;</code></a>, когда у вас есть несколько ссылок, указывающих на один и тот же контент, эта проблема также рассмотрена здесь <a href="http://www.google.com/webmasters/">Google Webmaster Tools</a>.</li>
<li>Используйте <a href="http://www.google.com/webmasters/">Google Webmaster Tools</a> и <a href="http://www.bing.com/toolbox/webmaster">Bing Webmaster Tools</a>.</li>
<li>Установите <a href="http://www.google.com/analytics/">Google Analytics</a> прямо в начале (или какой-нибудь опенсорсный инструмент вроде <a href="http://piwik.org/">Piwik</a>).</li>
<li>Почитайте про то, как <a href="https://ru.wikipedia.org/wiki/%D0%A1%D1%82%D0%B0%D0%BD%D0%B4%D0%B0%D1%80%D1%82_%D0%B8%D1%81%D0%BA%D0%BB%D1%8E%D1%87%D0%B5%D0%BD%D0%B8%D0%B9_%D0%B4%D0%BB%D1%8F_%D1%80%D0%BE%D0%B1%D0%BE%D1%82%D0%BE%D0%B2">robots.txt</a> и поисковые пауки работают.</li>
<li>Перенаправляйте запросы (используя код <code>301 Moved Permanently</code>), спрашивующие <code>www.example.com</code> к <code>example.com</code> (или каким-нибудь еще способом) для предотвращения раздробления ранжирования гугла между двумя сайтами.</li>
<li>Держите в голове, что существуют поисковые пауки, которые плохо себя ведут.</li>
<li>Если у вас есть нетекстовый контент, загляните в дополнение Google для построения карты сайта для видеоконтента и т.д. Также немного хорошей информации можно найти в <a href="http://stackoverflow.com/questions/72394/what-should-a-developer-know-before-building-a-public-web-site#167608">одном из ответов на сайте</a>.</li>
</ul>

<h2>Технология</h2>

<ul>
<li>Поймите <a href="http://www.ietf.org/rfc/rfc2616.txt">HTTP-протокол</a> и такие вещи, GET, POST, сессии, куки и что означает <a href="https://en.wikipedia.org/wiki/Stateless_protocol">протокол «stateless»</a>.</li>
<li>Напишите ваш <a href="http://www.w3.org/TR/xhtml1/">XHTML</a>/<a href="http://www.w3.org/TR/REC-html40/">HTML</a> и <a href="http://www.w3.org/TR/CSS2/">CSS</a> согласно <a href="http://www.w3.org/TR/">спецификациям W3C</a> и удостоверьтесь, что они <a href="http://validator.w3.org/">валидны</a>. Цель здесь &mdash; избежать причуды брузера и в качестве бонуса сайт будет легче заставить работать на скрин ридерах и мобильных устройствах.</li>
<li>Понимайте как Javascript-код обрабатывается в браузере.</li>
<li>Понимайте как JavaScript, стили и другие ресурсы используются для того, чтобы страница загрузилась и рассмотрите их влияние на <em>полученную</em> производительность. Широко распространена практика <a href="https://developer.yahoo.com/blogs/ydn/high-performance-sites-rule-6-move-scripts-bottom-7200.html">перемещать подключенные скрипты вниз</a> ваших страниц за исключением приложений для аналитики и библиотек для поддержки совместимости HTML5 во всех браузерах.</li>
<li>Понимайте как работает JavaScript-песочница, особенно, если вы намеренны использовать iframe'ы.</li>
<li>Будьте готовы к тому, что JavaScript может быть и будет отключен и что AJAX поэтому будет дополнением, а не основанием. Даже если обычные пользователи разрешат выполнение JS, помните, что расширение <a href="http://noscript.net/">NoScript</a> становится все более популярным, мобильные устройства могут не работать, как ожидалось и Google не запустит большинство ваших скриптов во время индексации сайта.</li>
<li>Изучите <a href="http://www.bigoakinc.com/blog/when-to-use-a-301-vs-302-redirect/">разницу между перенаправленями 301 и 302</a> (это также и к вопросу о поисковой оптимизации).</li>
<li>Изучите как можно больше о вашей платформе для развертки.</li>
<li>Рассмотрите использование <a href="http://stackoverflow.com/questions/167531/is-it-ok-to-use-a-css-reset-stylesheet">Reset Style Sheet</a> или <a href="http://necolas.github.com/normalize.css/">normalize.css</a>.</li>
<li>Рассмотрите Javascript фреймворки (такие как <a href="http://jquery.com/">jQuery</a>, <a href="http://mootools.net/">MooTools</a>, <a href="http://www.prototypejs.org/">Prototype</a>, <a href="http://dojotoolkit.org">Dojo</a> или <a href="http://developer.yahoo.com/yui/3/">YUI 3</a>), которые спрячут многие специфические для браузеров особенности использования Javascript для манипуляции DOM.</li>
<li>Осозновая проблему производительности и использование JS фреймворков, рассмотрите использование таких сервисов как <a href="http://developers.google.com/speed/libraries/devguide">Google Libraries API</a>, чтобы загружать фреймворки, таким образом браузер может использовать копию фреймворка, которые он уже кешировал вместо того, чтобы загружать копию с вашего сайта.</li>
<li>Не изобретайте велосипед. Прежде чем что-то делать, поищите компоненту или пример того, как это делать. 99% вероятность того, что кто-то делал это до вас и выпустил готовую работающую версию кода.</li>
<li>С другой стороны, не начинайте с подключения 20 библиотек, прежде чем вы не определитесь со своими нуждами. Особенно на клиентской стороне очень важно делать вещи легкими, быстрыми и гибкими.</li>
</ul>

<h2>Исправление ошибок</h2>

<ul>
<li>Поймите, что вы потратите 20% своего времени на кодинг и 80% на поддержку кода, поэтому пишите код соответствующе.</li>
<li>Установите хорошую систему для уведомлении об ошибках.</li>
<li>Поставьте систему, где люди смогут с вами связаться с предложениями и критикой.</li>
<li>Документируйте то, как работает приложение для будущей команды поддержки и людей, осуществляющих будущую поддержку проекта.</li>
<li>Делайте частые бекапы! (и удостоверьтесь, что эти бекапы смогут функционировать) Имейте стратегию восстановления, а не только стратегию бекапа.</li>
<li>Пользуйтесь системой контроля версий, такой как <a href="http://subversion.apache.org/">Subversion</a>, <a href="http://mercurial.selenic.com/">Mercurial</a> или <a href="http://git-scm.org">Git</a>.</li>
<li>Не забывайте тестировать. Фреймворки как <a href="http://seleniumhq.org/">Selenium</a> могут помочь. Особенно если вы полностью  автоматизируете тестирование, возможно с использованием инструмента непрерывной интеграции, таким как <a href="http://jenkins-ci.org/">Jenkins</a>.</li>
<li> Удостоверьтесь, что у вас происходит подробное логгирование с использованием таких фреймворков, как <a href="http://logging.apache.org/log4j/">log4j</a>, <a href="http://logging.apache.org/log4net/">log4net</a> или <a href="http://log4r.rubyforge.org/">log4r</a>. Если что-то идет не так с вашим живым сайтом, вам легко будет узнать что именно.</li>
<li>В процессе логгирования удостоверьтеся, что идет запись как предусмотренных исключений, так и непредусмотренных. Записывайте и анализируйте вывода логгирования, и это покажет вам, какие ключевые проблемы есть на вашем сайте.</li>
</ul>

<h2>Другое</h2>

<ul>
<li>Реализуйте как серверную, так и клиентскую часть мониторинга и аналитики (они должен быть скорее активные, чем реактивные).</li>
<li>Используйте сервисы как UserVoice и Intercom (или любые другие похожие инструменты) для того, чтобы быть в контакте с вашими пользователями.</li>
<li>Почитайте книгу <a href="http://nvie.com/posts/a-successful-git-branching-model/">«Модель ветвления Git»</a>, написанную <a href="http://nvie.com/about/">Vincent Driessen</a></li>
</ul>

<p>Много вещей пропущено, не потому что они бесполезны, но потому что они слишком детализованы, выходят за рамки или идут слишком далеко для того, кто хочет увидеть обзор вещей, который было бы полезно знать. Не стесняйтесь предлагать что-то новое или изменить что-то из написанного, наверняка что-то пропущено или сделаны некоторые ошибки.</p>

<a href="http://programmers.stackexchange.com/questions/46716/what-technical-details-should-a-programmer-of-a-web-application-consider-before"> Источник </a>
