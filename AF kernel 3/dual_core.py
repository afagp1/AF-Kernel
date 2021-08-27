peer_id=event.message.peer_id
id=event.message.from_id
text=event.message.text
use_prefix=0
if servis_on=True:
	exec(readFF(f'{servis_file}'))

if str(id).startswith('-'):
	pass
else:
	if event.from_chat:
		print(f'Новое сообщение в чате, (',peer_id,')')

	else:
		print(f'Новое сообщение в ЛС')
		use_prefix=2
	print(f'id:({id})\nСообщение: {text}')
	print()

	

	if text.startswith('/') or text.startswith(bot_prefix):
		use_prefix=1
	

	if use_prefix==1 or use_prefix==2:
		if use_prefix==1:
			if text.startswith('/'):
				parametr=text[1:]
			elif text.startswith(bot_prefix):
				parametr=text[len(bot_prefix)+1:]
		elif use_prefix==2:
			parametr=text
	
		try:
			command=parametr.split()[0]
		except:
			command=0

		if command in commands_list:
			print('Обнаруженна команда '+str(command))
			try:

				code=readFF(commands[command]['file'])
				msg=parametr[len(command)+1:]
				exec(f'#-*- coding:utf-8 -*-\n{code}')
		
				print('Команда выполнена')
			except:
				api.messages.send(peer_ids=admins,message=str('Произошла ошибка\n'+str(traceback.format_exc())),random_id=0)
				print('Команда не выполнена')
	else:
		pass
	print('=====================')
	print()

