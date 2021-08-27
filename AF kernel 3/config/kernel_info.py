#
#Информация о ядре
#


kernel_version='0.3.1'#Версия ядра
kernel_name='AF kernel 3.1'#Наименование ядра
kernel_author='AFaGP'#Автор ядра
krenel_helper='Nicoscocos,Catweird' # Помошники/около-разработчики

#
#Настройки библиотек
#

edit_libs=True #разрешение на редактирование библеотек

#Библеотеки 

config_lib='config'#Папка с настройками
commands_lib='commands'#Папка с командами
commands_other_lib=None#Папка с командами из других ботов catpy,NikoBot
database_lib=None#Папка с базой данных
photos_lib=None#Папка для фотографий
servis_lib=None#Папка с сервисами/службами

#файлы

core_file='core.py'#Файл с ядром для старта бота
dual_core_file='dual_core.py'#Файл с вторичным ядром, запускается при получении сообщения
bot_config='config/bot_info.py'#файл с настройками бота
fast_start_file='faststart.py'#Файл для быстрого старта ядра
defs_file='defs.py'#Файл с функциями запускается при запуске
servis_file=None#Файл с серфисами запускающийся при получении сообщения




kernel_libs=[servis_lib,defs_file,fast_start_file,config_lib,commands_lib,commands_other_lib,database_lib,photos_lib,core_file,dual_core_file]

for i in kernel_libs:
	if i==None:
		kernel_libs.remove(i)


#Начтройки запуска

other_commnds=False #подгружать ли инородные команды
defolt_commands_line=7 #кол-во строк которые выполняются при считываниие команд
servis_on=False#Подгружать ли сервисы?
