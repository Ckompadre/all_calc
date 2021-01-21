#   library
import math

#   massives
answer = [
    #   first part
['Ответы'],                                                     #0
['Газовая постоянная топлива = ', ''],                          #1
['Газовая постоянная окислителя = ' , ''],                      #2
['Удельный объём топлива = ' , ''],                             #3
['Удельный объём окислителя = ' , ''],                          #4
['Показатель процесса = ' , ''],                                #5
['Степень расширения в критическом сечении канала = ' , ''],    #6
['Cкорость потока в критическом сечении канала = ' , ''],       #7
['Удельный объём продуктов сгорания = ' , ''],                  #8
['Удельная площадь критического сечения = ' , ''],              #9
['Степень расширения на срезе канала = ' , ''],                 #10
['Скорость потока на срезе канала = ' , ''],                    #11
['Удельную площадь сопла = ' , ''],                             #12
['Геометрическая степень расширения сопла = ' , ''],            #13
    #   second part
['Удельный импульс на земле = ' , ''],                          #14
['Расход топлива = ' , ''],                                     #15
['Удельный импульс в пустоте = ' , ''],                         #16
['Тяга в пустоте = ' , ''],                                     #17
['Площадь критического сечения и среза сопла = ' , ''],         #18
['Расходный комплекс и коэффициент тяги = ' , ''],              #19
    #   third part
['' , ''],
['' , ''],
['' , ''],
['' , ''],
['' , ''],
['' , ''],
['' , ''],
['' , ''],
['' , ''],
['' , ''],
]

fuel = [[76.8 , -4465.3 , 14.9 , 21.2]]                         # Hydrogen

oxidizer = [[1512.7 , -339.58 , 54.39 , 85.87]]                 # Fluoride

#   Main action
print("Приветствую!")
print("Программу разработал: Ckompadre\n")

    #   Select fuel
print("Выберите вид топлива...")
print("1. Водород")
user_input_fuel = int(input("Ответ: "))
if user_input_fuel == 1:
    p = fuel[0][0]
    Jct = fuel[0][1]
    Tpl = fuel[0][2]
    Tkip = fuel[0][3]

    #   Select oxidizer
print("\nВыберите вид окислителя...")
print("1. Фтор")
user_input_oxidizerr = int(input("Ответ: "))
if user_input_oxidizerr == 1:
    p = oxidizer[0][0]
    Jct = oxidizer[0][1]
    Tpl = oxidizer[0][2]
    Tkip = oxidizer[0][3]

#   User data Input
P0 = float(input("Тяга Р0 = "))
Pk = float(input("Давление в камере сгорания Pк = "))
Pc = float(input("Давление на срезе сопла Pс = "))

print("\nГазовая постоянная")
Rk = answer[1][1] = 8314 / fuel[0][0]                           #fuel
Rc = answer[2][1] = 8314 / oxidizer[0][0]                       #oxidizer
print("Газовая постоянная топлива = ", Rk)
print("Газовая постоянная окислителя = ", Rc)

print("\nОпределяем удельный объём")
Tk = float(input("В"))
Tc = float(input("В"))
uk = answer[3][1] = (Rk * Tk) / Pk                              #fuel
uc = answer[4][1] = (Rc * Tc) / Pc                              #oxidizer
print("Удельный объём топлива = ", uk)
print("Удельный объём окислителя = ", uc)

print("\nПоказатель процесса")

print("\nСтепень расширения в критическом сечении канала")

print("\nCкорость потока в критическом сечении канала")

print("\nУдельный объём продуктов сгорания")

print("\nУдельную площадь критического сечения")

print("\nСтепень расширения на срезе канала")

print("\nСкорость потока на срезе канала")

print("\nУдельная площадь сопла")

print("\nГеометрическая степень расширения сопла")

#   Final action
print("")
print(answer[0][0])
print(answer[1][0],  answer[1][1])
print(answer[2][0],  answer[2][1])
print(answer[3][0],  answer[3][1])
print(answer[4][0],  answer[4][1])
print(answer[5][0],  answer[5][1])
print(answer[6][0],  answer[6][1])
print(answer[7][0],  answer[7][1])
print(answer[8][0],  answer[8][1])
print(answer[9][0],  answer[9][1])
print(answer[10][0], answer[10][1])
print(answer[11][0], answer[11][1])
print(answer[12][0], answer[12][1])
print(answer[13][0], answer[13][1])
print(answer[14][0], answer[14][1])
print(answer[15][0], answer[15][1])
print(answer[16][0], answer[16][1])
print(answer[17][0], answer[17][1])
print(answer[18][0], answer[18][1])
print(answer[19][0], answer[19][1])
