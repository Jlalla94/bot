<?php

    require_once("utils.php");

    /**
     * Function receives an array with integer numbers,
     * should return its sum. It is not alowed to use built-in php functions.
     *
     * Функция получает на вход массив чисел, должна вернуть сумму этих чисел.
     * Не использовать встроенные функции суммирования php.
     *
     * @param array $arr
     * @return integer
     */
    function my_sum($arr) {
        foreach ($arr as $value){
        $summ += $value; 
        }return $summ;
    }


    /**
     * Function receives a long string with many words.
     * It should return the same string, but words,
     * larger then 6 symbols, should be changed, symbols
     * after the sixth one should be replaced by symbol *
     *
     * Функция получает на вход длинную строку с множеством слов.
     * Она должна вернуть ту же строку, но в словах, которые длиннее 6 символов,
     * функция должна вместо всех символов после шестого поставить одну звездочку.
     * Пример: Из слова 'verwijdering' должно получиться 'verwij*'
     *
     * @param string $shortMe
     * @return string
     */
    function shortener($shortMe) {
    $arr = explode(" ",$shortMe);
    foreach ($arr as &$str){
        if (strlen($str)>=7)
            $str = $str[0] .  $str[1] . $str[2] . $str[3] . $str[4] . $str[5] . '*';
    }
        return implode(" ", $arr);
    }

    /**
     * Function receives an array of strings.
     * Please return number of strings, which
     * length is at least 2 symbols and first character
     * is equal to the last character
     *
     * Функция получает на вход массив строк. Вернуть надо количество строк,
     * которые не короче двух символов и у которых первый и последний
     * символ совпадают.
     *
     * @param array $arr
     * @return number
     */
    function compare_ends($arr) {
    
    foreach ($arr as $str){
        if (strlen($str)>=2)
            if ($str[0]==$str[(strlen($str)-1)])
                $k=$k+1;
    }   
    return $k;
    }




    /**
     * Function receives a string, should return this string reversed.
     *
     * Функция получает на вход строку, должна вернуть ее перевернутой.
     *
     * @param string $str
     * @return string
     */
    function reverse_string($str) {
       for ($i =  strlen($str); $i >-1;$i--){
            $str2=$str2 . $str[$i];
        }
    return ($str2);
    }

test_shortener();

test_compare_ends();

test_my_sum();

test_reverse_string();










