Как работает функция:

1. Функция 'print_operation_table' принимает функцию 'operation', а также необязательные аргументы 'num_rows' и 'num_columns', указывающие число строк и столбцов таблицы.
2. Вложенный цикл 'for' перебирает все комбинации строк и столбцов в заданных пределах (от 1 до 'num_rows' и от 1 до 'num_columns' соответственно).
3. Для каждой комбинации строк и столбцов вызывается функция 'operation' и результат выводится на экран в виде пяти символов (при помощи f-строки с форматированием).
4. В конце каждой строки происходит перевод строки, чтобы начать новую строку таблицы.