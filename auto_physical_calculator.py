#   library
import math

#   massives
answer = [
    #   first part
[''],                                                                   #0
['Газовая постоянная топлива = ', ''],                                  #1
['Газовая постоянная окислителя = ' , ''],                              #2
['Удельный объём топлива = ' , ''],                                     #3
['Удельный объём окислителя = ' , ''],                                  #4
['Показатель процесса = ' , ''],                                        #5
['Степень расширения в критическом сечении канала = ' , ''],            #6
['Степень расширения в критическом сечении канала = ' , ''],            #7
['Cкорость потока в критическом сечении канала = ' , ''],               #8
['Удельный объём продуктов сгорания = ' , ''],                          #9
['Удельная площадь критического сечения = ' , ''],                      #10
['Степень расширения на срезе канала = ' , ''],                         #11
['Скорость потока на срезе канала = ' , ''],                            #12
['Удельную площадь сопла = ' , ''],                                     #13
['Геометрическая степень расширения сопла = ' , ''],                    #14
    #   second part
['Удельный импульс на земле = ' , ''],                                  #15
['Расход топлива = ' , ''],                                             #16
['Удельный импульс в пустоте = ' , ''],                                 #17
['Тяга в пустоте = ' , ''],                                             #18
['Площадь критического сечения Fkp = ' , ''],                           #19
['Площадь среза сопла Fc = ' , ''],                                     #20
['Расходный комплекс = ' , ''],                                         #21
['Коэффициент тяги = ' , ''],                                           #22 
    #   third part
['Коэффициент потерь в закритической части канала в пустоте = ' , ''],  #23
['Коэффициент, учитывающий влияние земного противодавления = ' , ''],   #24
['Коэффициент потерь в закритической части канала на земле = ' , ''],   #25
    #   fourth part
['Удельный импульс в пустоте = ' , ''],									#26
['Удельный импульс на земле = ' , ''],									#27
['Расход топлива = ' , ''],												#28
['Расход горючего = ' , ''],											#29
['Расход окислителя = ' , ''],											#30
['Площадь критического сечения = ' , ''],								#31
['Площадь среза канала = ' , ''],										#32
['Диаметр критического сечения = ', ''],								#33
['Диаметр среза канала = ', ''],										#34
['Тяга в пустоте = ', ''],												#35
['Расходный комплекс = ', ''],											#36
['Коэффициент тяги = ', ''],											#37
	#	fiveth part
[],
[],
[],
[],
[]
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

print("\n\nРЯД ПРИБЛИЖЕННЫХ РАСЧЁТОВ\n")

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

print("\n\nРАСЧЁТ ПАРАМЕТРОВ ДВИГАТЕЛЯ\n")

print("\nУдельный импульс на земле")
J0yd = answer[15][1] = wc + fc * (Pc - 0,1013)
print("Удельный импульс на земле = ", J0yd)

print("\nРасход топлива")
m = answer[16][1] = P / J0yd
print("Расход топлива = ", m)

print("\nУдельный импульс в пустоте")
J00yd = answer[17][1] = wc + fc * Pc
print("Удельный импульс в пустоте = ", J00yd)

print("\nТяга в пустоте")
P00 = answer[18][1] = J00yd * m
print("Тяга в пустоте = ", P00)

print("\nПлощадь критического сечения и среза сопла")
Fkp = answer[19][1] = fkp * m
Fc = answer[20][1] = fc * m
print("Площадь критического сечения Fkp = ", Fkp)
print("Площадь среза сопла Fc = ", Fc)

print("\nРасходный комплекс")
B = answer[21][1] (Pk * Fkp) / m
print("Расходный комплекс = ", B)

print("\nКоэффициент тяги")
k00T = answer[22][1] = P00
print("Коэффициент тяги = ", k00T)

#   THIRD PART

print("\n\nРАСЧЁТ КОЭФФИЦИЕНТОВ ПОТЕРЬ\n")

qk = float(input("Коэффициент связанный с недогоранием топлива = "))
qa = float(input("Коэффициент потерь на рассеивание потока = "))
q00w = float(input("Коэффициент потерь в закритической части канала = "))

print("\nКоэффициент потерь в закритической части канала в пустоте")
q00c = answer[23][1] = qa * q00w
print("Коэффициент потерь в закритической части канала в пустоте = ", q00c)

print("\nКоэффициент, учитывающий влияние земного противодавления")
delta_qc = answer[24][1] = (Fc * Ph) / P00
print("Коэффициент, учитывающий влияние земного противодавления = ", delta_qc)

print("\nКоэффициент потерь в закритической части канала на земле")
q0c = answer[25][1] = q00c * ((1 - (delta_qc / qc)) / (1 - delta_qc))
print("Коэффициент потерь в закритической части канала на земле = ", q0c)

# FOURTH PART

print("\n\nРАСЧЕТ РЕАЛЬНЫХ ПАРАМЕТРОВ ДВИГАТЕЛЯ\n")

print("Удельный импульс в пустоте")
r_J00yd = answer[26][1] = qk * q00c * J00yd
print("Удельный импульс в пустоте = ", r_J00yd)

print("\nУдельный импульс на земле")
r_J0yd = answer[27][1] = qk * q0c * J0yd
print("Удельный импульс на земле = ", r_J0yd)

print("\nРасход топлива")
r_m = answer[28][1] = P0 / r_J0yd
print("Расход топлива = ", r_m)

print("Расход горючего и окислителя")
#r_mg = answer[29][1] = (1 / (1 + k)) * r_m
#r_mo = answer[30][1] = (k / (1 + k)) * r_m
print("Расход горючего = ", r_mg)
print("Расход окислителя = ", r_mo)

print("\nПлощадь критического сечения и среза канала")
r_Fkp = answer[31][1] = Fkp / q00c
r_Fc = answer[32][1] = Fc / q00c
print("Площадь критического сечения = ", r_Fkp)
print("Площадь среза канала = ", r_Fc)

print("\nДиаметр критического сечения и среза канала")
r_dkp = answer[33][1] = math.sqrt((4 * r_Fkp) / math.pi)
r_dc = answer[34][1] = math.sqrt((4 * r_Fc) / math.pi)
print("Диаметр критического сечения = ", r_dkp)
print("Диаметр среза канала = ", r_dc)

print("\nТяга в пустоте")
r_P00 = answer[35][1] = r_J00yd * r_m
print("Тяга в пустоте = ", r_P00)

print("\nРасходный комплекс и коэффициент тяги")
r_B = answer[36][1] = qk * B
r_k00T = answer[37][1] = r_P00 / (Pk * r_Fkp)
print("\nРасходный комплекс = "r_B)
print("\nКоэффициент тяги", r_k00T)

#	FIVETH PART

print("\nПостроение профиля камеры сгорания")


#   Final action
print("\n\nОТВЕТЫ")

i = 1
while i < 37:
	print(answer[i][0] , answer[i][1])
	i += 1
