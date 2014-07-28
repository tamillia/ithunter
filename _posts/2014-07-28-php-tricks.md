---
published: false
---

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
list($a, $b) = array($b, $a);
{% endhighlight %}
или так в PHP 5.4:
{% highlight php linenos %}
list($a, $b) = [$b, $a];
{% endhighlight %}

Есть возможность возвращать массив из результата выполнения функции и кода ошибки. Очень удобно использовать для функций, выполняющих валидацию:
{% highlight php linenos %}
list($result, $error) = validateString($str);

if($error){
  // Что-нибудь сделать.
}

function validateString($str){
  return array(false, "Строка не валидна");
}
{% endhighlight %}

Буферизация вывода может быть очень полезной:
{% highlight php linenos %}
ob_start(); // Начать захват вывода.
print "this";
echo "that";
$buffer = ob_get_contents();
ob_end_clean(); // Окончить захват.

// ... Сюда можно еще добавить какой-нибудь код...

print $buffer; // Распечатает "thisthat".
{% endhighlight %}

[Функции контроля вывода](http://php.net/manual/ru/ref.outcontrol.php)

Есть удобные функции, проверяющие на наличие в строке тех или иных типов символов:
ctype_alnum — Проверяет на наличие буквенно-цифровых символов
ctype_alpha — Проверяет на наличие буквенных символов
ctype_cntrl — Проверяет на наличие управляющих символов
ctype_digit — Проверяет на наличие цифровых символов в строке
[Читать документацию](http://php.net/manual/ru/book.ctype.php)







