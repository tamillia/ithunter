---
layout: post
title: "Как отлаживать регулярные выражения"
date: 2014-02-14 19:42:00
category: regexp
published: true
---

<img src="http://i.piccy.info/i7/eb81480d8311cba9bce9f4266eaf0e17/4-67-114/4639962/unknown.jpg" class="img-responsive" /> <br />

[http://regex101.com/](http://regex101.com/)

Этот сервис позволяет тестировать ваши регулярные выражения на примере, но еще он выделяет другим цветом группы:<br />
<a target="_blank" href="http://qph.is.quoracdn.net/main-qimg-ae64948db789ce154ab7804daa242fae?convert_to_webp=true"><img src="http://qph.is.quoracdn.net/main-qimg-ae64948db789ce154ab7804daa242fae?convert_to_webp=true" class="img-responsive" /></a><br />

Еще предоставляет полное объяснение о том, что происходит:<br />
<a target="_blank" href="http://qph.is.quoracdn.net/main-qimg-61225b629452cf3e345c45e2db762d32?convert_to_webp=true"><img src="http://qph.is.quoracdn.net/main-qimg-61225b629452cf3e345c45e2db762d32?convert_to_webp=true" class="img-responsive" /></a><br />

Однако нужно держать в голове то, регулярные выражения в разных языках программирования будут иметь
свои особенности(например, некоторые вещи не поддерживаются в каком-то языке). Есть веб-сервисы,
позволяющие переводить ваше регулярное выражение так, чтобы оно поддерживалось в определенном языке
программирования, но некоторые из них могут быть не всегда надежными.

Рекомендуется сервис [http://regexplanet.com](http://regexplanet.com), он поддерживает следующие
технологии:<br />
<a target="_blank" href="http://qph.is.quoracdn.net/main-qimg-3d70886b7dca6b96f25e3b53de5a86dc?convert_to_webp=true"><img src="http://qph.is.quoracdn.net/main-qimg-3d70886b7dca6b96f25e3b53de5a86dc?convert_to_webp=true" class="img-responsive" /></a><br />
Можно убедиться в значительных различиях вот [здесь](http://www.regular-expressions.info/refflavors.html)
Там достаточно кликнуть по ссылке в таблице содержаний, чтобы увидеть как поддерживается что-нибудь
в разных языках программирования.

Если вы хотите веб-сервис для большей визуальной отладки, то можно попробовать вот этот ресурс:
[http://www.debuggex.com/](http://www.debuggex.com/).

Но этот сервис не поддерживает глобальный поиск, то есть вы можете находить подходящую под шаблон строку
только один раз.

Если вас интересует сервис, который на ходу отмечает те подстроки, которые соответствуют шаблону,
то удобным инструментом может быть [http://rubular.com/](http://rubular.com/). Там можно сохранить
"пермалинк"(то есть ссылка на ваше регулярное выражение прямо внутри сервиса) и название пермалинка
есть регулярное выражение, на которое пермалинк ссылается.
