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
['Степень расширения в критическом сечении канала = ' , ''],    #7
['Cкорость потока в критическом сечении канала = ' , ''],       #8
['Удельный объём продуктов сгорания = ' , ''],                  #9
['Удельная площадь критического сечения = ' , ''],              #10
['Степень расширения на срезе канала = ' , ''],                 #11
['Скорость потока на срезе канала = ' , ''],                    #12
['Удельную площадь сопла = ' , ''],                             #13
['Геометрическая степень расширения сопла = ' , ''],            #14
    #   second part
['Удельный импульс на земле = ' , ''],                          #15
['Расход топлива = ' , ''],                                     #16
['Удельный импульс в пустоте = ' , ''],                         #17
['Тяга в пустоте = ' , ''],                                     #18
['Площадь критического сечения и среза сопла = ' , ''],         #19
['Расходный комплекс и коэффициент тяги = ' , ''],              #20
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
['' , '']]

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
    fuel_p = fuel[0][0]
    fuel_Jct = fuel[0][1]
    fuel_Tpl = fuel[0][2]
    fuel_Tkip = fuel[0][3]

    #   Select oxidizer
print("\nВыберите вид окислителя...")
print("1. Фтор")
user_input_oxidizer = int(input("Ответ: "))
if user_input_oxidizer == 1:
    oxidizer_p = oxidizer[0][0]
    oxidizer_Jct = oxidizer[0][1]
    oxidizer_Tpl = oxidizer[0][2]
    oxidizer_Tkip = oxidizer[0][3]

#   User data Input
P0 = float(input("Тяга Р0 = "))
Pk = float(input("Давление в камере сгорания Pк = "))
Pc = float(input("Давление на срезе сопла Pс = "))

#   FIRST PART

print("\nРЯД ПРИБЛИЖЕННЫХ РАСЧЁТОВ\n")

print("\nГазовая постоянная")
Rk = answer[1][1] = 8314 / fuel_p                               #fuel
Rc = answer[2][1] = 8314 / oxidizer_p                           #oxidizer
print("Газовая постоянная топлива = ", Rk)
print("Газовая постоянная окислителя = ", Rc)

print("\nОпределяем удельный объём")
Tk = float(input("Температура камеры сгорания = "))
Tc = float(input("Температура на срезе сопла = "))
uk = answer[3][1] = (Rk * Tk) / Pk                              #fuel
uc = answer[4][1] = (Rc * Tc) / Pc                              #oxidizer
print("Удельный объём топлива = ", uk)
print("Удельный объём окислителя = ", uc)

print("\nПоказатель процесса")
n = answer[5][1] = math.log(Pk / Pc) / math.log(uc / uk)
print("Показатель процесса = ", n)

print("\nСтепень расширения в критическом сечении канала")
PIkp = answer[6][1] = (2 / n + 1)**(n / n - 1)
Pkp = answer[7][1] = PIkp * Pkp
print("Степень расширения в критическом сечении канала = ", PIkp, " и ", Pkp)

print("\nCкорость потока в критическом сечении канала")
wkp = answer[8][1] = math.sqrt(2 * (n / n + 1) * Rk * Tk)
print("Cкорость потока в критическом сечении канала = ", wkp)

print("\nУдельный объём продуктов сгорания")
ukp = answer[9][1] = uk * ((n + 1) / 2)**(1 / (n - 1))
print("Удельный объём продуктов сгорания = ", ukp)

print("\nУдельная площадь критического сечения")
fkp = answer[10][1] = ukp / wkp
print("Удельная площадь критического сечения = ", fkp)

print("\nСтепень расширения на срезе канала")
PIc = answer[11][1] = Pc / Pk
print("Степень расширения на срезе канала", PIc)

print("\nСкорость потока на срезе канала")
wc = answer[12][1] = math.sqrt(2 * (n / n - 1) * Rk *Tk * (1 - (Pc / Pk)**((n - 1) / n)))
print("Скорость потока на срезе канала = ", wc)

print("\nУдельная площадь сопла")
fc = answer[13][1] = uc / wc
print("Удельная площадь сопла = ", fc)

print("\nГеометрическая степень расширения сопла")
Fc = answer[14][1] = fc / fkp
print("Геометрическая степень расширения сопла = ", Fc)

#   SECOND PART

print("\nРАСЧЁТ ПАРАМЕТРОВ ДВИГАТЕЛЯ\n")

print("Удельный импульс на земле")
J0yd = wc + fc * (Pc - Ph)
print("Удельный импульс на земле = ", J0yd)


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
