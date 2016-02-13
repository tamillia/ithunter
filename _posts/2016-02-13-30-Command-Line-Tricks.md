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

* Показывает 10 крупнейших по размеру каталогов на верхнем уровне с общей загрузкой. Все в мегабайтах.

```
du -cms .[^.]*/ */ | sort -rn | head
```

* Для Linux. Распечатывает список ID зомби-процессов.

```
ps aux | awk '{if ($8=="Z") { print $2 }}'
```

* Выписывает 20 png кадров из видео, начиная с 3 минут, 46 секунд.

```
mplayer -vo png -ss 3:46 -frames 20 stairs.mp4
```

* Перемещает фото с EXIF данными в каталоги, сортируя по году создания.

```
exiftool -v '-Directory<DateTimeOriginal' -d %Y . 
```

* Создает список URL адресов верхнего уровня из всех журналов.

```
zcat access_log*.gz |cat - access_log |awk '{print $7}' |sed 's/?.*//' |sort|uniq -c|sort -nr 
```

* Устали от переноса строки в df утилите? Попробуйте `–P`, чтобы исправить и выровнять строки в колонки.

```
df -P | column -t
```

* Сделайте свой запрос безопаснее со знаком “решетка”: даже если вы его скопируете и вставите, оно не запустится. 

```
PS1="#$PS1" 
```

* Ежечасовые запросы на графике. 

```
awk '{print $4}' apache_log|sort -n|cut -c1-15|uniq -c|awk '{b="";for(i=0;i<$1/10;i++){b=b"#"}; print $0 " " b;}'
```

* Узнайте, какой из ваших каталогов занимает как минимум 1Гб места.

```
du -h . | grep "^[0-9.]+G"
```

* То, что вы не можете воплотить это в реальной жизни.

```
nohup sleep 8h 
```

* Создание месячной гистограммы по датам файлов в текущем каталоге.

```
ls -la --full-time |tr -s " " |cut -f6 -d " "|cut -c1-7 | sort | uniq -c
```

* Перемещение недавних фотографий в каталог 2016.

```
find . -maxdepth 1 -daystart -type f -name '*.jpg' -mtime -$( date +%j ) -exec mv -v {} 2016/ ; 
```

* Показывает размер каталога и сортирует по Мб, Гб и т.д.

```
du -sh */ | sort -h 
```

* Список из пятидесяти страниц 404 в убывающем порядке.

```
awk '$9 == "404" {print $7}' access.log |sort|uniq -c|sort -rn| head -n 50 
```

* Редактирует файл на удаленном сервере, используя vim вашего рабочего стола в *nix.

```
vim scp://user@server1//etc/httpd/httpd.conf
```

* Быстрое, всплывающее через 3 минуты уведомление.

```
sleep 3m; xmessage -nearmouse "Your tea is ready"
```

* Скажите "Здравствуйте" милым голосом.

```
wget -q -O- -U Mozilla "http://translate.google\.com/translate_tts?q=hello&tl=en"|mpg123 -q -
```

* Находит все файлы меньше 100 Мб и отображает их читабельный размер.

```
find / -size +100M -exec du -h {} ; 
```

* Делает Unix время читабельным. Специально для даты GNU.

```
date -d @192179700
```

* Самый быстрый способ удалить пустые файлы.

```
rsync -a -delete empty/ foo/
```

* Оповещение о завершении текущего процесса в программе.

```
<ctrl-z> bg ; wait %1 ; echo "done" | mail -s "done" you@example.com
```

* Скачать видеоплейлист с YouTube.

```
youtube-dl --max-quality 37 --title --playlist-start=1 --playlist-end=10 --ignore-errors youtube-playlist-url 
```

* Приостановить и прикрепить процесс на экране.

```
longcmd ; [Ctrl-Z] ; bg ; disown ; screen ; reptyr $( pidof longcmd ) 
```

* Представьте, что вы на космическом корабле.

```
play -n -c1 synth whitenoise band -n 100 20 band -n 50 20 gain +30 fade h 1 86400 1 
```

* Марк Цукерберг мог сэкономить миллионы, если бы он знал о ImageMagick (Instagram).

```
convert +level-colors Firebrick, me.jpg oldme.jpg
```

* Показывает какие процессы использует порт 80 локально и удаленно. 

```
lsof -i TCP:80
```

* Быстро находит 5 самых больших файлов на CWD, не пересекая границы файловой системы. 

```
find . -xdev -ls | sort -n -k 7 | tail -5 
```

* Быстрый и легкий способ сделать отражение (копию) сайта. 

```
wget -m http://www.example.com/ 
```

* Делает рамку вокруг текста.
```
function box(){ t="$1xxxx";c=${2:-=}; echo ${t//?/$c}; echo "$c $1 $c"; echo ${t//?/$c}; } 
```

* Находит дубликаты изображений в текущем каталоге.
```
shasum *.jpg | awk {'print $1'} | sort | uniq -c | grep -v " 1 " 
```
