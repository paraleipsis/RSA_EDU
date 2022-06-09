# RSA_EDU
Курсовая работа по дисциплине "Криптографические методы защиты информации" на тему "Программная реализация криптоалгоритма RSA"


## Шифрование и расшифровка текста при помощи алгоритма RSA - `main.py`:


Для реализации алгоритма RSA необходимо выбрать два простых числа p и q. Число p определяется по порядковому номеру студента в группе по следующей таблице простых чисел от 1000 до 100:


![Image alt](https://github.com/paraleipsis/repo_images/raw/main/RSA_EDU/primes.png)


Для определения числа q необходимо выполнить следующее преобразование: ФИО студента представить в виде последовательности чисел от 1 до 33, где каждой букве фамилии соответствует порядковый номер буквы в русском алфавите. Последовательность чисел – сложить. Если полученная сумма больше 1000 – пошагово отнимаем по 1000, пока не получим число, меньшее 1000. Для полученного числа выбираем наиболее близкое из приведенной ранее таблицы простых чисел. Если число находится между двумя простыми числами, то выбираем ближайшее.


Далее вычисление функции Эйлера по формуле: φ(n)=(p-1)*(q-1)



Дополнительно к указанным числам необходимо выбрать произвольное число e, взаимно простое с φ(n) и лежащее в пределах 1<e<φ(n). В итоге имеем открытый ключ (e,n).


Закрытый ключ (d,n) необходимо вычислить по формуле: d∗e=1(mod φ(n)).


Текст для зашифровки необходимо перевести в числовое отображение. Для этого используем таблицу русского алфавита:


![Image alt](https://github.com/paraleipsis/repo_images/raw/main/RSA_EDU/rus.png)


Для каждого полученного числа выполнить шифрование по алгоритму RSA: ci = mi^e (mod n). В итоге получаем ширфотекст.


При помощи полученных отрытого и закрытого ключей, значения модуля, а так же получившегося зашифрованного текста выполняется обратное преобразование для получения исходного текста.


Интерфейс программы:
![Image alt](https://github.com/paraleipsis/repo_images/raw/main/RSA_EDU/gui.jpg)


## Расчетная часть (была выполнена на коленке за пару вечеров перед защитой курсовой, поэтому код абсолютно нечитаемый, плохо оптимизированный и нуждается в рефакторинге) - `power_series.py`:


Из полученных данных (а именно модуля n) составить степенные последовательности. Для степенных последовательностей найти группы, подгруппы, фактор-группы.
Составить циклические группы. Выполнить прямое произведение двух и трех циклических групп. Для прямого произведения двух и трёх циклических групп найти фактор-группы. Найти двадцать чисел (х) таких, что в степени z при делении на mod(n) давали остаток 1.
Найти последовательность чисел s=px (mod n) и определить, повторяются ли числа в этом ряду, и если да – то определить, через сколько степеней они начинают повторяться.


Вывод работы программы:


![Image alt](https://github.com/paraleipsis/repo_images/raw/main/RSA_EDU/1.png)
![Image alt](https://github.com/paraleipsis/repo_images/raw/main/RSA_EDU/2.png)
![Image alt](https://github.com/paraleipsis/repo_images/raw/main/RSA_EDU/3.png)
![Image alt](https://github.com/paraleipsis/repo_images/raw/main/RSA_EDU/4.png)
