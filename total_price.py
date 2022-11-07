price_list = {'0-18' : 0, '18-25' : 990, '25+' : 1390}
total_price = 0
n = int(input('Введите количество билетов, которое хотите приобрести: '))
for i in range(1, n + 1):
  while True:
    try:
      age = int(input(f'Введите возраст посетителя # {i}: '))
      if age < 0:
        raise ValueError ('Negative age value') 
    except ValueError:
        print('Ошибка! Допустим ввод только целых положительных чисел!')
        continue
    else:
      break
  if age < 18:
    total_price += price_list['0-18']
  elif 18 <= age < 25:
    total_price += price_list['18-25'] 
  else:
    total_price += price_list['25+']
print(f'Суммарная стоимость билетов: {total_price if n <= 3 else round(total_price * 0.9)}руб')     
