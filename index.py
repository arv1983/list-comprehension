def list_comprehension_exercise_1():
    list_comprehension = [ i for i in range(11)]
    print(list_comprehension)
list_comprehension_exercise_1()
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def list_comprehension_exercise_2():
    list_comprehension = [ i for i in range(22) if i % 2 == 0 or i % 3 == 0]
    print(list_comprehension)
list_comprehension_exercise_2()
#  [0, 2, 3, 4, 6, 8, 9, 10, 12, 14, 15, 16, 18, 20, 21]


def list_comprehension_exercise_3():
    list_comprehension = [ i for i in range(-3, 32) if i % 2 != 0 and i % 5 != 0]
    print(list_comprehension)
list_comprehension_exercise_3()
# Produza uma lista num intervalo de -5 a 31 em que seus valores não sejam divisíveis nem por 2 e nem por 5.
# > [-3, -1, 1, 3, 7, 9, 11, 13, 17, 19, 21, 23, 27, 29, 31]

def list_comprehension_exercise_4():
    list_comprehension = [ x ** 2 for x in range(0, 11)]
    print(list_comprehension)
list_comprehension_exercise_4()
# > [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100] quadrado


def list_comprehension_exercise_5(sentence: str):
    list_comprehension = [palavra for palavra in sentence if palavra.isupper()]
    print(list_comprehension)
sentence = 'O Rato Rui Gosta De QueiJo FresQuiNho'
list_comprehension_exercise_5(sentence)
# > ['O', 'R', 'R', 'G', 'D', 'Q', 'J', 'F', 'Q', 'N']
# list_comprehension_exercise_6(sentence: str)


def list_comprehension_exercise_6(sentence: str):
    list_comprehension = [palavra for palavra in sentence.split() if len(palavra) >= 4 and palavra[0] == 'r']
    print(list_comprehension)
sentence = 'o rato rui roeu a roupa do rei de goma'
# ['rato', 'roeu', 'roupa', 'roma']
list_comprehension_exercise_6(sentence)