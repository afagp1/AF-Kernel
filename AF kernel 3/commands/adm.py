#Afgach_command
author = "AFaGP"
mode = "only"
command_new=True
command_id = 'utils'
command_ru = 'адм'
command_info = 'выполняет админскую штуку'
command_help = 'команды для админов: \n - стоп -- остановка бота по номеру\n - обновление -- загружает файл как обновление и распаквывает замешая существующие директории \n - рестарт -- перезагружет бота '

try:

	if id not in admins:
		f_1('Вы не админ')
	else:
		adm_commands=['стоп','тест']
		if msg.split()[0] in adm_commands:

			if msg==f'стоп':
				f_1('ok')
				os.kill(os.getpid(),9)
			elif msg=='тест':
				res=f"""
	если вы видете это сообщение ядро работает
	версия Python: {sys.version_info.major}.{sys.version_info.minor}
	название ядра: {kernel_name}
	версия ядра: {kernel_version}
	кол-во подгруженных команд: {len(commands_list)}
				"""
				f_1(res)





		else:
			f_1('данной команды не обнаруженно')
except:
	f_1(traceback.format_exc())
	f_1('ошибка')