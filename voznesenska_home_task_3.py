# 1. Сформируйте строку, содержащую определенную информацию о символе по его индексу в известном слове.
# Например "The [индекс символа] symbol in [здесь слово] is '[символ с соответствующим порядковым номером]'".
# Получите слово и номер с помощью input() или воспользуйтесь константой.
# Например (слово - "Python" а номер символа 3) - "3 symbol в "Python" is 't'".

word = 'Project'
first_symbol = word[0]
print(f'The first symbol in "{word}" is "{first_symbol}".')

# 2.Вести з консолі строку зі слів за допомогою input() (або скористайтеся константою).
# Напишіть код, який визначить кількість слів, в цих даних.
my_str = 'Welcom to Ukraine'
print(f'List of Words ={my_str.split()}')
print('word_count_in_string:', len(my_str.split()))

# 3.Існує ліст з різними даними, наприклад lst1 = ['1', '2', 3, True, 'False', 5, '6', 7, 8, 'Python', 9, 0, 'Lorem Ipsum'].
# Напишіть код, який сформує новий list (наприклад lst2), який би містив всі числові змінні (int, float), які є в lst1.
# Майте на увазі, що данні в lst1 не є статичними, можуть змінюватись від запуску до запуску.

lst1 = ['1', '2', 3, True, 'False', 5, '6', 7, 8, 'Python', 9, 0, 'Lorem Ipsum']
lst2 = [elem for elem in lst1 if type(elem) == int or type(elem) == float]
print('lst2:', lst2)
