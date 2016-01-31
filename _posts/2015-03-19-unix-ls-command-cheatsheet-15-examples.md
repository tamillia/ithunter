---
layout: post
title: "15 практических примеров использования Unix команды ls"
date: 2015-03-20 20:01:53
category: tools
tags: [unix, ls, console, terminal, superuser, cheatsheet]
description: "Шпаргалка: Как использовать всю мощь команды ls."
published: true
---
<img src="https://theasder.github.io/img/terminal.png" class="img-responsive" /><br />

Пользователи Unix и системные администраторы не могут жить без команды `ls`. Используете ли вы эту команду 10 или 100 раз в день, знание всей мощи команды `ls` позволит сделать процесс использования консоли приятнее.

В этой статье мы сделаем обзор по 15 практическим примерам этой команды.

## 1. Открыть последний редактированный файл `ls -t`

Также, команда `head -1` позволяет извлечь этот первый файл.

Пример: откроем в vim'e последний редактируемый текстовый файл

    $ vim `ls -t | head -1`


## 2. Отобразить название файлов на отдельной строчке `ls -1`

    $ ls -1 ~
    Applications
    Desktop
    Documents
    Downloads
    Dropbox
    Library
    $


## 3. Отобразить всю информацию о файлах/директориях `ls -l`

    $ ls -l ~
    total 0
    drwx------    3 theasder  staff   102 Dec  7 15:20 Applications
    drwx------+   9 theasder  staff   306 Mar 19 21:23 Desktop
    drwx------@  62 theasder  staff  2108 Mar 17 10:44 Documents
    drwx------+ 143 theasder  staff  4862 Mar 17 22:41 Downloads
    drwx------@ 125 theasder  staff  4250 Mar 19 19:51 Dropbox
    drwx------@  58 theasder  staff  1972 Feb 15 01:03 Library

- Первый символ &mdash; тип файла.
    - - обычный файл
    - `d` директория
    - `s` файл-сокет
    - `l` файл-ссылка
- Первое поле &mdash; расширение файла: следующие 9 символов определяют права использования файла. Каждые три символа ссылкаются на чтение, запись и выполнение для пользователя, группы и всех остальных. Например, -rw-r---- определяет разрешения на чтение и запись для пользователя, чтения для группы и никаких разрешений для использования всеми остальными.
- Второе поле &mdash; число ссылок на этот файл или директорию.
- Третье поле отображает владельца файла или директории.
- Четвертое поле отображает название группы файла или директории.
- Пятое поле отображает размер файла в байтах.
- Шестое поле отображает дату и время последних изменений.
- Седьмое поле отображает имя пользователя.

## 4. Отобразить размер файла в читабельном для человека виде `ls -lh`

    $ ls -l
    total 352
    -rw-r--r--   1 theasder  staff     114 Aug 23  2014 README.md
    -rw-r--r--   1 theasder  staff     119 Aug 23  2014 _config.yml
    drwxr-xr-x   5 theasder  staff     170 Mar 12 23:35 _layouts
    drwxr-xr-x  30 theasder  staff    1020 Mar 19 23:58 _posts
    -rw-r--r--   1 theasder  staff     570 Aug 23  2014 categories.html
    -rw-r--r--   1 theasder  staff    8737 Aug 23  2014 complexity.html

    $ ls -lh
    total 352
    -rw-r--r--   1 theasder  staff   114B Aug 23  2014 README.md
    -rw-r--r--   1 theasder  staff   119B Aug 23  2014 _config.yml
    drwxr-xr-x   5 theasder  staff   170B Mar 12 23:35 _layouts
    drwxr-xr-x  30 theasder  staff   1.0K Mar 19 23:58 _posts
    -rw-r--r--   1 theasder  staff   570B Aug 23  2014 categories.html
    -rw-r--r--   1 theasder  staff   8.5K Aug 23  2014 complexity.html


## 5. Отобразить всю информацию о директории `ls -ld`

Аналогичная команда `ls -l`, но отображает вместо подробной информации о файлах, информацию о директории:

    $ ls -l
    total 352
    -rw-r--r--   1 theasder  staff     114 Aug 23  2014 README.md
    -rw-r--r--   1 theasder  staff     119 Aug 23  2014 _config.yml
    drwxr-xr-x   5 theasder  staff     170 Mar 12 23:35 _layouts
    drwxr-xr-x  30 theasder  staff    1020 Mar 19 23:58 _posts
    -rw-r--r--   1 theasder  staff     570 Aug 23  2014 categories.html
    -rw-r--r--   1 theasder  staff    8737 Aug 23  2014 complexity.html

    $ ls -ld
    drwxr-xr-x  26 theasder  staff  884 Mar  9 13:48 .


## 6. Рассортировать файлы по времени их изменения `ls -lt`

На примере репозитория этого сайта: посты обновляются чаще, чем что-либо.

    $ ls -lt
    total 352
    drwxr-xr-x  30 theasder  staff    1020 Mar 20 00:04 _posts
    drwxr-xr-x  35 theasder  staff    1190 Mar 19 20:06 img
    drwxr-xr-x   4 theasder  staff     136 Mar 19 20:03 script
    drwxr-xr-x   5 theasder  staff     170 Mar 12 23:35 _layouts
    drwxr-xr-x   9 theasder  staff     306 Mar  9 15:14 css
    drwxr-xr-x   7 theasder  staff     238 Mar  9 13:46 fonts
    drwxr-xr-x  12 theasder  staff     408 Feb 10 22:39 schedule


## 7. Рассортировать файлы по времени их изменения в обратном порядке `ls -ltr`

    $ ls -ltr
    total 352
    -rw-r--r--   1 theasder  staff     140 Aug 23  2014 yandex_7efa16da5b528035.html
    -rw-r--r--   1 theasder  staff    4513 Aug 23  2014 wiki.html
    -rw-r--r--   1 theasder  staff     981 Aug 23  2014 sitemap.xml
    -rw-r--r--   1 theasder  staff      53 Aug 23  2014 google45dcee434783937d.html
    -rw-r--r--   1 theasder  staff    1406 Aug 23  2014 favicon.ico
    -rw-r--r--   1 theasder  staff    8737 Aug 23  2014 complexity.html
    -rw-r--r--   1 theasder  staff     570 Aug 23  2014 categories.html


## 8. Отобразить скрытые файлы `ls -a` или `ls -A`

Дополнительно помимо скрытых файлов (они начинаются с точки) показываются '.'(текущая директория) и '..'(родительская директория), чтобы избежать этого, используйте опцию `-A`. 

    $ ls -a
    .					demo
    ..					favicon.ico
    .DS_Store				fonts
    .Rhistory				google45dcee434783937d.html
    .git					img
    README.md				index.html

    $ ls -A
    .DS_Store				favicon.ico
    .Rhistory				fonts
    .git					google45dcee434783937d.html
    README.md				img


## 9. Отобразить файлы рекурсивно `ls -R`

Распечатывает все файлы и все содержимое каждой из директорий, а также содержимое директорий директорий и т.д.:

    $ ls -R
    ./_layouts:
    default.html	post.html

    ./_posts:
    2014-02-11-python-tricks.md
    2014-02-14-debugging-regex.md
    2014-05-08-git-cheatsheet.md
    2014-05-11-webdev-tools.md
    2014-05-14-beginners-guide-to-nodejs.md
    2014-05-30-project-ideas.md
    2014-06-02-most-popular-programming-language.md

## 10. Отобразить номер индексного дескриптора `ls -i`

Это команда бывает полезной, когда есть необходимость удалить файлы, имеющие специальные символы.

    $ ls -i
     1136427 README.md				 1136479 google45dcee434783937d.html
	 1136480 img                     1136429 _config.yml
	 1136482 index.html              1136430 _layouts
	 1136559 js



## 11. Отобразить вместо непечатаемых символов в имени файла при выводе будут ставиться знаки вопроса `ls -q`



## 12. Отобразить UID и GID файла `ls -n`

Аналогично `ls -l`, но дополнительно выводятся значения UID и GID (пользовательский и групповой ID)

    $ ls -n
    total 352
    -rw-r--r--   1 501  20     114 Aug 23  2014 README.md
    -rw-r--r--   1 501  20     119 Aug 23  2014 _config.yml
    drwxr-xr-x   5 501  20     170 Mar 12 23:35 _layouts
    drwxr-xr-x  30 501  20    1020 Mar 20 00:40 _posts

    $ ls -l
    total 352
    -rw-r--r--   1 theasder  staff     114 Aug 23  2014 README.md
    -rw-r--r--   1 theasder  staff     119 Aug 23  2014 _config.yml
    drwxr-xr-x   5 theasder  staff     170 Mar 12 23:35 _layouts
    drwxr-xr-x  30 theasder  staff    1020 Mar 20 00:40 _posts


## 13. Классификация файлов с помощью специальных символов `ls -F` 

Команда позволяет классифицировать содержимое директории. 
`/` &mdash; директория, `@` &mdash; файл-ссылка, `*` &mdash; выполняемый файл и ничего не ставится, если это обычный файл.

    $ ls -F
    README.md				google45dcee434783937d.html
    img/                    schedule/
    _config.yml		        index.html
    _layouts/				js/
    _posts/					


## 14. Классификация файлов по цвету `ls --color=auto` 

Папки выделяются синим, ссылки зеленым, обычные файлы цветом по умолчанию.

## 15. В `~/.bashrc` можно внести сокращения указанных сверху команд.

Вы можете упростить себе жизнь, создав aliases в файле `.bashrc`, находящимся в корневой директории (зайти в него можно, к примеру, набрав `nano ~/.bashrc`). После вы вносите изменения и после перезагрузки консоли можете уже пользоваться введенными командами. Мы предлагаем такие:

Вывести в читабельном виде размер файлов
    
    alias ll="ls -lh"

Классифицировать файлы, добавив специальные символы

    alias lv="ls -F"

Классифицировать файлы, добавив специальные символы и по цвету

    alias ls="ls -F --color=auto"

