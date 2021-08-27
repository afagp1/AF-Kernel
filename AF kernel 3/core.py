print('[INFO] Старт бота')
print()


try:
	commands={}
	comma_name=''
	commands_list=[]
	commands_help_list=[]
	commands_list=[]
	mutlist=[]

	commands_help_x={}
	path = f"{os.getcwd()}"
	path_com = f"{os.getcwd()}/{commands_lib}"
	path_com_o = f"{os.getcwd()}/{commands_other_lib}"
	com_len=(len(os.listdir(path_com)))

	print('[+] Обозначение переменных')
except:
	print(traceback.format_exc())
print()


try:
	vk = vk_api.VkApi(token=token)  # Токен твоего бота
	vk._auth_token()
	vk.get_api()
	api = vk.get_api()
	longpoll = VkBotLongPoll(vk, group_id) # ID Сообщества
	print("[+]подключение к longpoll")
except:
	print(traceback.format_exc())
	print("[-]подключение к longpoll")
print()


print('[INFO] Подгрузка функций')

try:
	commands_files=os.listdir(path_com)

	for i in commands_files:
		i_orig=i
		try:
			x='\ '.replace(' ',"")
			i=f"{path_com}/{i}".replace(x,"/")
			line0=lineFF(f"{i}",0)
			if line0=="#Afgach_command\n":
				Ff = open(i, 'r', encoding='UTF-8',errors='ignore')
				file = Ff.readlines()
				Ff.close()
				for x in range(defolt_commands_line):
					exec(file[x+1])
				try:
					chelp=command_help
				except:
					chelp=f'команнде {command_ru} не прописан параметр help'


				if len(command_ru.split(';'))>=2:
					coman1=command_ru
					command_ru=command_ru.split(';')
					coman=command_ru[0]
					for com in command_ru:
						commands[com]=({'index_en':command_id,
										   'mode':mode,
										   "author":author,
										   'info':command_info,
										   'file':i,
										   'help':chelp,
										   'new':command_new})
						commands_list.append(com)
						if chelp!=None:
							commands_help_x[coman]=coman1
					if chelp!=None:
						commands_help_list.append(coman)
					print('Добавленна команда c различными вызовами '+str(com))



				else:
					commands[command_ru]=({'index_en':command_id,
										   'mode':mode,
										   "author":author,
										   'info':command_info,
										   'file':i,
										   'help':chelp,
										   'new':command_new})
					if chelp!=None:
						commands_help_list.append(command_ru)
					commands_list.append(command_ru)
					print('Добавленна команда '+str(command_ru))
		except:
			print('Команда {} не подгруженна'.format(i_orig))
			print(traceback.format_exc())
	print('[+] Команды подгруженны')
except:
	print('[-] Команды не подгруженны')

if other_commnds==True:
	print("[INFO] Подгрузка инородных команд")
	try:
		commands_files=os.listdir(path_com_o)
	
		for i in commands_files:
			i_orig=i
			try:
				x='\ '.replace(' ',"")
				i=f"{path_com_o}/{i}".replace(x,"/")
				line0=lineFF(f"{i}",0)
				if line0=="#Nicoscocos_command\n":
					Ff = open(i, 'r', encoding='UTF-8',errors='ignore')
					file = Ff.readlines()
					Ff.close()
					for x in range(5):
						exec(str(file[x+1]).replace('-','_'))
					try:
						chelp=use_to
					except:
						chelp=f'команнде {name} не прописан параметр help'

					if is_ignore==True:
						pass
					else:
						commands[name]=({'index_en':name,
											   'mode':None,
											   "author":author,
											   'info':use_to,
											   'file':i,
											   'help':chelp,
											   'new':None})
						commands_list.append(name)
						print(f'Добавленна команда {str(name)} (NeuronNET Core-syntax) ')
			except:
				print('Команда {} не подгруженна'.format(i_orig))
				print(traceback.format_exc())
		print('[+] Инородные команды подгруженны')
	except:
		print('[-] Инородные команды не подгруженны')
		print(traceback.format_exc())

print()
print('[INFO] Последние настройки завершенны, запуск бота')

def code_start():
	exec(readFF('dual_core.py'))
	time.sleep(5)

try:
	while True:
		for event in longpoll.listen():
			try:
				tt0=time.time()
				if event.type == VkBotEventType.WALL_POST_NEW:
					print('event post')
					#api.messages.send(message="хей человеки, новый пост!", peer_id=2000000002, attachment=f"wall{event.object['owner_id']}_{event.object['id']}", random_id=0)
				elif event.type == VkBotEventType.MESSAGE_NEW:
					th = Thread(target=code_start)
					th.start()
					#exec(readFF('dual_core.py'))
			except:
				api.messages.send(peer_ids=admins,message=str('ЯДРУ БОЛЬНА СУКА\n'+str(traceback.format_exc())),random_id=0)
except:
	print("Произошла ошибка при запуске основного цикла\n")
	print(traceback.format_exc())
	os.kill(os.getpid(),9)





