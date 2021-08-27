#-*- coding:utf-8 -*-
print('Запуск ядра...')
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
vk_api;commands_list.append(com)
json;
time;
inspect;
sys'''.replace('\n','').split(';')

#Импортирование
for i in pips:
	try:
		module=i.split(':')[0]
		if len(i.split(':'))>=2:
			dop_module=i.split(':')[1].split(',')
			for dop in dop_module:
				try:
					exec(f"from {module} import {dop}")
					pass
				except Exception as e:
					pass
		exec(f'import {module}')
		
	except Exception as e:
		pass

def readFF(file): # Read From File
    try:
        Ff = open(file, 'r', encoding='UTF-8',errors='ignore')
        Contents = Ff.read()
        Ff.close()
        return Contents
    except:
        return None

#Загрузка настроек из папки config

if 'config' in os.listdir():
	try:
		ker_info=readFF('config/kernel_info.py')
		exec(ker_info)
	except:
		pass
else:
	raise FileNotFoundError('Не обнаруженно директории /config')

#проверка файлов

real_libs=os.listdir()

not_libs=[]

for i in kernel_libs:
	try:
		real_libs.remove(i)
	except:
		not_libs.append(i)
real_libs.remove('start.py')




if len(not_libs)!=0:
	
	if edit_libs==True:
		for i in not_libs:
			if i.endswith('.py'):
				try:
					file = open(str(i), "w", encoding="utf-8")
					file.close()
				except:
					pass
			else:
				try:
					os.mkdir(i)
				except:
					pass
else:
	pass

try:
	exec(readFF(bot_config))
except:
	pass

#Подгрузка сервисов

try:
	exec(readFF(defs_file))
except:
	pass

if servis_on==True:


	servis_web_list=os.listdir(f'{servis_lib}/web')
	for i in servis_web_list:
		try:
			exec(readFF(f'{servis_lib}/web/{i}'))
		except:
			pass
	servis_list=os.listdir(f'{servis_lib}')
	servis_list.remove('web')
	for c in servis_list:
		if lineFF(f'{servis_lib}/{c}',0)=='#servise\n':
			try:
				exec(readFF(f'{servis_lib}/{c}'))
			except:
				print(traceback.format_exc())
else:
	pass



print('[INFO] Настройки завершенны!')


while True:
	try:
		core=readFF('core.py')
		exec(core)
		print('Ядро упало')
		time.sleep(10)
	except:
		print(traceback.format_exc())


