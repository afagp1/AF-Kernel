#-*- coding:utf-8 -*-
print('Запуск ядра...')
print()
print('[INFO] Начинаю импортирование')
pips='''urllib;
simpledemotivators:Demotivator;
PIL:Image,ImageDraw,ImageFont;
traceback:format_exc;
threading:Thread;
typing:Any,Text;
math;
datetime;
requests;
random:choice,randint;
vk_api.bot_longpoll:VkBotLongPoll,VkBotEventType;
os;
vk_api;
json;
time;
inspect;
sys'''.replace('\n','').split(';')
print('======================')

for i in pips:
	try:
		module=i.split(':')[0]
		if len(i.split(':'))>=2:
			dop_module=i.split(':')[1].split(',')
			for dop in dop_module:
				try:
					exec(f"from {module} import {dop}")
					print(f'[+]Установлен пакет {dop} из модуля {module}')
				except Exception as e:
					print(f'[-]Не установлен под-модуль {dop} из модуля {module}')
		exec(f'import {module}')
		print(f'[+]установлен модуль {module}')
	except Exception as e:
		print(f'[-]не установлен модуль {i}')
		print(f'Причиа: {e}')
print('======================')

def readFF(file): # Read From File
    try:
        Ff = open(file, 'r', encoding='UTF-8',errors='ignore')
        Contents = Ff.read()
        Ff.close()
        return Contents
    except:
        return None
print('')
print("[INFO] Начинаю загрузку настроек из папки /config")
print('')
print('======================')
if 'config' in os.listdir():
	try:
		ker_info=readFF('config/kernel_info.py')
		exec(ker_info)
		print('[+]Получена информация о ядре')
	except:
		print('[-]Не получена информация о ядре')
		print(traceback.format_exc())
else:
	raise FileNotFoundError('Не обнаруженно директории /config')
print('======================')

print()

print('[INFO] Проверка директорий')

print()

if edit_libs==True:
	print('Разрешение на создание директорий получен')

print()

real_libs=os.listdir()

not_libs=[]

for i in kernel_libs:
	try:
		real_libs.remove(i)
	except:
		not_libs.append(i)
real_libs.remove('start.py')





if len(not_libs)!=0:
	for i in not_libs:
		print('=======================')
		print('[-]Не обнаруженна директория {}'.format(i))
	if edit_libs==True:
		print('[INFO] Начинаю создание директорий')
		for i in not_libs:
			if i.endswith('.py'):
				try:
					file = open(str(i), "w", encoding="utf-8")
					file.close()
					print('[+]Создан файл {}'.format(i))
				except:
					print('[-]Не создан файл {}'.format(i))
			else:
				try:
					os.mkdir(i)
					print('[+]Создана папка {}'.format(i))
				except:
					print('[-]Не создана папка {}'.format(i))
else:
	print('=======================')
	print('[+]Все директории на месте')

print('[INFO] Загрзука данных для запуска бота')
print()

try:
	exec(readFF(bot_config))
	print('[+] Данные полученны')
except:
	print('[-] Данные не полученны')

print()

print('[INFO] Подгрузка функций')
print()
try:
	exec(readFF(defs_file))
	print('[+] Функции подгруженны')
except:
	print('[-] Функции не подгруженны')
print()

if servis_on==True:
	print('[INFO] Подгрузка срвисов')
	print()

	servis_web_list=os.listdir(f'{servis_lib}/web')
	for i in servis_web_list:
		try:
			exec(readFF(f'{servis_lib}/web/{i}'))
			print('[+]Подгружен веб сервис {}'.format(i))
		except:
			print('[-]Не подгружен веб сервис {}'.format(i))
	servis_list=os.listdir(f'{servis_lib}')
	servis_list.remove('web')
	for c in servis_list:
		if lineFF(f'{servis_lib}/{c}',0)=='#servise\n':
			try:
				exec(readFF(f'{servis_lib}/{c}'))
				print('[+]Подгружен сервис {}'.format(c))
			except:
				print(traceback.format_exc())
else:
	print('[INFO] Сервисы не будут подгруженны')


print('[INFO] Настройки завершенны!')
print()

while True:
	try:
		core=readFF('core.py')
		exec(core)
		print('Ядро упало')
	except:
		print(traceback.format_exc())


