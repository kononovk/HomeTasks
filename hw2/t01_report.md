`1) 50000`

**Рекурсивный факториал:**
Программа выделяет 16.1 Мб памяти на функциию и 0.6 Мб на ответ

Время работы функции: *0.90625с*

**Циклический факториал:**
Программа выделяет 16.8 Мб на функцию и 0.4 Мб на ответ

Время работы функции: *0.875с*

`2) 80000`

**Рекурсивный факториал**
Программа выделяет 17.2 Мб на функцию и 0.1 Мб на ответ

Время работы функции: *2.265625с*

**Циклический факториал**
Программа выделяет 17.3 Мб на функцию и 0.0 Мб на ответ
(т.к. памяти, выделенной на функцию хватает для записи ответа)

Время работы функции: *2.4375с*

`3) 110000`

**Рекурсивный факториал**
Программа выделяет 16.8 Мб на функцию и 1.0 Мб на ответ

Время работы функции: *4.328125с*

**Циклический факториал**
Программа выделяет 17.8 Мб на функцию и 0.0 Мб на ответ
(т.к. памяти, выделенной на функцию хватает для записи ответа)

Время работы функции: *4.171875с*

Проанализировав работу двух алгоритмов в задании 1, с помощью библиотеки memory_profiler можно прийти к выводу,
что время работы алгоритма вычисления факториала работает быстрее в реализации цикла, особенно сильна разница 
во времени в случае больших входных параметров(в случае 80000 циклический алгоритм работает на 0.2с).
Таким образом, по данным цифрам можно заметить, что циклический алгоритм считает быстрее и оптимальнее по памяти,
так как:
1) **вызов функции более трудоемкий процесс, чем одна итерация цикла, 
                                    так как циклы не заносят в стек каждый вызов функции**.
2) **рекурсия занимает больше памяти, потому что хранит в стеке предыдущие значения.**