---
layout: post
title: "30 приёмов командной строки Unix"
date: 2016-02-13 3:00:00
description: "Полезные приемы, которые помогут вам почувствовать всю мощь командной строки Unix."
category: tools
tags: "командная строка, команды, командная строка Linux, командная строка Unix, команды Linux, команды Unix"
published: true
---

<img src="http://theasder.github.io/img/hands.jpg" class="img-responsive" /><br />

Полезные приемы, которые помогут вам почувствовать всю мощь командной строки Unix.

<!-- more -->

1. `du -cms .[^.]*/ */ | sort -rn | head `
  Показывает 10 крупнейших по размеру каталогов на верхнем уровне с общей загрузкой. Все в мегабайтах.

2. `ps aux | awk '{if ($8=="Z") { print $2 }}' `
  Для Linux. Распечатывает список ID зомби-процессов.

3. `mplayer -vo png -ss 3:46 -frames 20 stairs.mp4 `
 Выписывает 20 png кадров из видео, начиная с 3 минут, 46 секунд.

4. `exiftool -v '-Directory<DateTimeOriginal' -d %Y . `
  Перемещает фото с EXIF данными в каталоги, сортируя по году создания.

5. `zcat access_log*.gz |cat - access_log |awk '{print $7}' |sed 's/?.*//' |sort|uniq -c|sort -nr `
 Создает список URL адресов верхнего уровня из всех журналов.

6. `df -P | column -t `
  Устали от переноса строки в df утилите? Попробуйте `–P`, чтобы исправить и выровнять строки в колонки.

7. `PS1="#$PS1" `
  Сделайте свой запрос безопаснее со знаком “решетка”: даже если вы его скопируете и вставите, оно не запустится. 

8. `awk '{print $4}' apache_log|sort -n|cut -c1-15|uniq -c|awk '{b="";for(i=0;i<$1/10;i++){b=b"
"}; print $0 " " b;}' `
  Запросы на часовом графике. 

9. `du -h . | grep "^[0-9.]+G"`
  Узнайте, какой из ваших каталогов занимает как минимум 1Гб места.

10. `nohup sleep 8h `
  То, что вы не можете воплотить это в реальной жизни.

11. `ls -la --full-time |tr -s " " |cut -f6 -d` " "|cut -c1-7 | sort | uniq -c `
  Создание месячной гистограммы по датам файлов в текущем каталоге. 

12. `find . -maxdepth 1 -daystart -type f -name '*.jpg' -mtime -$( date +%j ) -exec mv -v {} 2016/ ; `
  Перемещение недавних фотографий в каталог 2016.

13. `du -sh */ | sort -h `
  Показывает размер каталога и сортирует по Мб, Гб и т.д.

14. `awk '$9 == "404" {print $7}' access.log |sort|uniq -c|sort -rn| head -n 50 `
  Список из пятидесяти страниц 404 в убывающем порядке.

15. `vim scp://user@server1//etc/httpd/httpd.conf `
  Редактирует файл на удаленном сервере, используя vim вашего рабочего стола в * nix .

16. `sleep 3m; xmessage -nearmouse "Your tea is ready" `
  Быстрое, всплывающее через 3 минуты уведомление.

17.	`wget -q -O- -U Mozilla "http://translate.google .com/translate_tts?q=hello&tl=en"|mpg123 -q - `
  Скажите привет прекрасным голосом.

18. `find / -size +100M -exec du -h {} ; `
  Находит все файлы меньше 100 Мб и отображает их читабельный размер.

19. `date -d @192179700` 
 Делает Unix время читабельным. Специально для даты GNU.

20. `rsync -a -delete empty/ foo/` 
 Самый быстрый способ удалить пустые файлы.

21. `<ctrl-z> bg ; wait %1 ; echo "done" | mail -s "done" you@example.com `
  Оповещение о завершении текущего процесса в программе.

22. `youtube-dl --max-quality 37 --title --playlist-start=1 --playlist-end=10 --ignore-errors youtube-playlist-url `
  Скачать видео-плейлист с YouTube.

23. `longcmd ; [Ctrl-Z] ; bg ; disown ; screen ; reptyr $( pidof longcmd ) `
Приостановить и прикрепить процесс на экране.

24. `play -n -c1 synth whitenoise band -n 100 20 band -n 50 20 gain +30 fade h 1 86400 1 `
  Представьте, что вы на космическом корабле.

25. `convert +level-colors Firebrick, me.jpg oldme.jpg `
  Марк Цукерберг мог сэкономить миллионы, если бы он знал о ImageMagick (Instagram).

26. `lsof -i TCP:80 `
  Показывает какие процессы использует порт 80 локально и удаленно. 

27. `find . -xdev -ls | sort -n -k 7 | tail -5 `
  Быстро находит 5 самых больших файлов на CWD, не пересекая границы файловой системы. 

28. `wget -m http://www.example.com/ `
  Быстрый и легкий способ сделать отражение (копию) сайта.

29. `function box(){ t="$1xxxx";c=${2:-=}; echo ${t//?/$c}; echo "$c $1 $c"; echo ${t//?/$c}; } `
  Делает рамку вокруг текста.

30. `shasum *.jpg | awk {'print $1'} | sort | uniq -c | grep -v " 1 "`
 Находит дубликаты изображений в текущем каталоге.



Перевод: Софья Лепёхина

[Источник](https://twitter.com/climagic)

**Читайте также:**

[Лучшие ресурсы для изучения Angular 2 с нуля](http://theasder.github.io/learning/2016/02/08/Best-Resources-for-Learning-Angular2-from-Scratch.html)

[Простой способ выучить что-то сложное](http://theasder.github.io/learning/2016/01/30/the-easy-way-to-learn-hard-stuff.html)

[30 ресурсов с головоломками и задачами по программированию](http://theasder.github.io/learning/2016/01/21/where-can-I-find-programming-puzzles-and-challenges.html)
