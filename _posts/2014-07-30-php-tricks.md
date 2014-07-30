---
layout: post
title: "Интересные приёмы на языке программирования PHP"
date: 2014-07-30 17:15:25
category: php
tags: [приемы, языки программирования]
published: true
---

<img src="http://s52.radikal.ru/i135/1407/12/91e792482c57.png" class="img-responsive" />

Начиная с версии PHP 5.3 поддерживается более короткая версия тернарного оператора.

{% highlight php linenos %}
<?php
$c = $a ?: $b;
?>
{% endhighlight %}
тождественно
{% highlight php linenos %}
<?php
$c = $a ? $a : $b;
?>
{% endhighlight %}


Обмен значениями переменных можно осуществить так:
{% highlight php linenos %}
<?php
list($a, $b) = array($b, $a);
?>
{% endhighlight %}
или так в PHP 5.4:
{% highlight php linenos %}
<?php
list($a, $b) = [$b, $a];
?>
{% endhighlight %}

Есть возможность возвращать массив из результата выполнения функции и кода ошибки. Очень удобно использовать для функций, выполняющих валидацию:
{% highlight php linenos %}
<?php
list($result, $error) = validateString($str);

if($error){
  // Что-нибудь сделать.
}

function validateString($str){
  return array(false, "Строка не валидна");
}
?>
{% endhighlight %}

Буферизация вывода может быть очень полезной:
{% highlight php linenos %}
<?php
ob_start(); // Начать захват вывода.
print "this";
echo "that";
$buffer = ob_get_contents();
ob_end_clean(); // Окончить захват.

// ... Сюда можно еще добавить какой-нибудь код...

print $buffer; // Распечатает "thisthat".
?>
{% endhighlight %}

[Функции контроля вывода](http://php.net/manual/ru/ref.outcontrol.php)

Есть удобные функции, проверяющие на наличие в строке тех или иных типов символов:
1. `ctype_alnum` — Проверяет на наличие буквенно-цифровых символов 
2. `ctype_alpha` — Проверяет на наличие буквенных символов
3. `ctype_cntrl` — Проверяет на наличие управляющих символов
4. `ctype_digit` — Проверяет на наличие цифровых символов в строке

[Читать документацию.](http://php.net/manual/ru/book.ctype.php)

В PHP много интересных строковых функций:
1. [levenshtein](http://php.net/manual/ru/function.levenshtein.php) -- смотрим насколько схожи по написанию строки
2. [soundex](http://php.net/manual/ru/function.soundex.php) -- смотрим насколько схожи по звучанию строки
3. [similar_text](http://php.net/manual/ru/function.similar-text.php) -- проверяем текст на схожесть

Использование **and** и **or**:
{% highlight php linenos %}
<?php
$foo and $this->bar(); // вызывается $this->bar(), если $foo имеет значение true
$bar or $this->foo(); // вызывается $this->foo(), когда $bar имеет значение false
?>
{% endhighlight %}

Более удобный способ реализовать несколько условных конструкций
{% highlight php linenos %}
<?php
switch(TRUE){
  case email_is_valid($email):
    // Что-то сделать здесь.
    break;
  case username_is_valid($user):
    // И здесь.
    break;
  case pass_too_short($pass) && pass_not_save($pass):
    // И здесь.
    break;
}
?>
{% endhighlight %}

Конструкции
{% highlight php linenos %}
<?php
for($i = 0, $count = count($my_array); $i < $count; $i++){
  // Do loopy things.
}
?>
{% endhighlight %}

{% highlight php linenos %}
<?php
for($i = 0; $i < count($my_array); $i++){}
?>
{% endhighlight %}
существенно различаются, так как во втором случае мы каждый раз вызываем функцию `count`, которая способна менять свое значение при изменении длины массива.

Есть более лаконичный способ написать
{% highlight php linenos %}
<?php
$array = [1, 2, 3, 4, 5];
if (!empty($array)) {
    do_something();
}
?>
{% endhighlight %}
используя оператор `or`:
{% highlight php linenos %}
<?php
$array = [1, 2, 3, 4, 5];
empty($array) OR do_something();
?>
{% endhighlight %}
Другой пример:
{% highlight php linenos %}
<?php
<input type="text" value="<?php $check AND print 'Hello World!' ?>" />
<input type="text" value="<?php echo $check ? 'Hello World!' : NULL ?>" />
?>
{% endhighlight %}

Есть возможность написать перехватчик ошибок:
{% highlight php linenos %}
<?php
fatal_error_handler_function( function() {
 
  $last_error = error_get_last();
 
  if ( !empty( $last_error['message'] ) ) {
    // Сюда нужно записать какие-нибудь инструкции, если произойдет ошибка
  } 
});
?>
{% endhighlight %}

Иногда бывает удобно воспользоваться динамическими переменными, данный код выведет "YES!":
{% highlight php linenos %}
<?php
<?php
    ${date("M")} = "Worked";
    $Worked = 'YES!';
    echo ${${date("M")}};
?>
?>
{% endhighlight %}
Это фича особенно удобна для вызова пользовательских функций.

Во время отладки у вас нет возможности выслеживать с помощью var_dump, в этом случае можно воспользоваться таким приемом:
{% highlight php linenos %}
<?php
file_put_contents('php://stderr', $someVar)
?>
{% endhighlight %}
Эта строчка распечатает значение переменной `$someVar` в php log.

`array_map` очень удобна. Она применяет фунцию по отношению к каждому элементу массива и возвращает массив из возвращенных значений. [Читать документацию](http://php.net//manual/ru/function.array-map.php)

Печатаем массив в читабельном виде:
{% highlight php linenos %}
<?php
private function displayTree($array)
{
  $newline = "<br>";
  $output = "";
  foreach($array as $key => $value) {
      if (is_array($value) || is_object($value)) {
          $value = "Array()" . $newline . "(<ul>" . $this->displayTree($value) . "</ul>)" . $newline;
      }
     $output .= "[$key] => " . $value . $newline;
  }
  return $output;
}
?>
{% endhighlight %}

{% highlight php linenos %}
<?php
$a = array_unique($a); // удаляем дубликаты из массива $a
?>
{% endhighlight %}

Можно в консоли запустить локальный сервер в PHP 5.4:

    php -S localhost:8080

Конвертация из массива в класс возможна с помощью явного приведения типа: `(object)$array`, но это не сработает на вложенных массивах, для этого можно использовать `json_decode(json_encode($arr));`
