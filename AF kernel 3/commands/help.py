#Afgach_command
author = "AFaGP"
mode = "only"
command_new=True
command_id = 'help'
command_ru = 'команды;help;помощь;справка'
command_info = 'ок'
command_help = 'Выводит список команд'

help_text=[]
for i in commands_help_list:
	try:
		get_helps=commands_help_x[i]
		get_x=1
	except:
		get_x=0

	if get_x==1:
		result=f"-{str(get_helps).replace(';','/')}-\n{commands[str(i)]['help']}"
	else:
		result=f"-{i}-\n{commands[str(i)]['help']}"

	help_text.append(result)

result='Список команд на данный момент\n\n'+str('\n\n'.join(help_text))

f_1(result.replace('\\n','\n'))

