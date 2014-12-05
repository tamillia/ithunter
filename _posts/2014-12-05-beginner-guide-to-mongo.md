---
layout: post
title: "Руководство для начинающих в Mongodb"
date: 2014-12-05 22:22:00
category: tutorial
tags: [webdev, back-end, databases, javascript]
published: true
---

<img src="http://theasder.github.io/img/mongo.jpeg" class="img-responsive"><br />

Mongoose — это библиотека Node.js, которая предосставляет возможность объектно-реляционного отображения, схожего со знакомым интерфейсом внутри Node.js. Если слова «объектно-реляционное отображение» или, в случае с Mongoose, «отображение объектных данных» вам ни о чём не говорят, объясняем: это значит, что Mongoose переводит данные в базу данных объектов JavaScript для дальнейшего их использования вашим приложением. Теперь давайте рассмотрим процессы создания и хранения документов в коллекции с помощью MongoDB и Mongoose. 

Примечание: предполагается, что Node.js и MongoDB у вас уже установлены. Для проверки приведённых ниже примеров необходимо запустить MongoDB. 

###Соединение с MongoDB
В рамках этого поста мы будем соединяться с тестовой базой данных, установленной по умолчанию в MongoDB. Для начала необходимо убедиться, что в консоли прописаны все ошибки соединения. Обратите внимание на использование события open — именно так вы будете создавать схемы и компилировать модели. 
```sh
var mongoose = require('mongoose');

var db = mongoose.connection;

db.on('error', console.error);
db.once('open', function() {
  // Здесь создаём схемы и модели.
});

mongoose.connect('mongodb://localhost/test');
```
###Схемы и модели
Для начала работы с данными в базе данных MongoDB нам понадобится одна схема и одна модель. Схемы определяют структуру документов внутри коллекции, а модели используются для создания копий данных, хранящихся в документах. Сейчас мы будем создавать базу данных фильмов, которые содержат «пасхальные яйца» (те самые смешные эпизоды, которые часто показываются во время титров). Начнём с создания схемы и модели Movie. 
```sh
var movieSchema = new mongoose.Schema({
  title: { type: String }
, rating: String
, releaseYear: Number
, hasCreditCookie: Boolean
});

// Компиляция модели Movie с помощью movieSchema в качестве структуры. 
// Mongoose также создаёт для этих документов коллекцию под названием Movies.
var Movie = mongoose.model('Movie', movieSchema);
```
Обратите внимание на то, что модель Movie написана с заглавной буквы; поскольку при компиляции модели производится функция-конструктор для создания копий модели. Копии, созданные с помощью конструктора, являются документами, с которыми будет работать Mongo. 

###Создание, чтение, обновление и удаление (CRUD)
Создание нового документа Movie будет несложным, поскольку вы определили модель: просто припишите значение модели Movie. Процессы обновления и сохранения так же просты: внесите изменения и вызовите функцию сохранения документа. 
```sh
var thor = new Movie({
  title: 'Thor'
, rating: 'PG-13'
, releaseYear: '2011'  // Обратите внимание на использование текстового значения вместо числового — Mongoose автоматически сконвертирует его. 
, hasCreditCookie: true
});

thor.save(function(err, thor) {
  if (err) return console.error(err);
  console.dir(thor);
});
```
Функция сохранения приведёт к созданию нового документа, в логах консоли это будет видно. 
```sh
{
  "title": "Thor",
  "rating": "PG-13",
  "releaseYear": 2011,
  "hasCreditCookie": true,
  "_id": "519a979e918d4d0000000001",
  "__v": 0
}
```
Извлечение существующего документа можно произвести разными способами. Вы можете найти документы по любому признаку из схемы, а также можно ограничить поиск любым количеством документов — используйте findOne, чтобы сузить поле результатов до одного документа.  
```sh
// Найти отдельный фильм по названию.
Movie.findOne({ title: 'Thor' }, function(err, thor) {
  if (err) return console.error(err);
  console.dir(thor);
});

// Найти все фильмы.
Movie.find(function(err, movies) {
  if (err) return console.error(err);
  console.dir(movies);
});

// Найти все фильмы с пасхалками.
Movie.find({ hasCreditCookie: true }, function(err, movies) {
  if (err) return console.error(err);
  console.dir(movies);
});
```
Mongoose позволяет с лёгкостью создавать статичные вспомогательные функции для поиска данных. 
```sh
movieSchema.statics.findAllWithCreditCookies = function(callback) {
  return this.find({ hasCreditCookie: true }, callback);
};

// Используйте вспомогательную статическую функцию компилированной модели Movie. 
Movie.findAllWithCreditCookies(function(err, movies) {
  if (err) return console.error(err);
  console.dir(movies);
});
```
Это всё, что требуется для CRUD-операций с данными из MongoDB — Mongoose делает их чрезвычайно простыми и позволяет быстро создавать нужные сервисы.  