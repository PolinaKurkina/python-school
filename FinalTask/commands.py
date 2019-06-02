import command_system
import vkapi
import settings
import mysql.connector
from newsapi import NewsApiClient
from mysql.connector import Error

def connect():
    """ Connect to MySQL database """
    try:
        conn = mysql.connector.connect(host='PolinaKurkina.mysql.pythonanywhere-services.com',
                                       database='VK',
                                       user='PolinaKurkina',
                                       password='9Jncm7JKZE93Fdk')
        if conn.is_connected():
            print('Connected to MySQL database')

    except Error as e:
        print(e)

    finally:
        conn.close()

if __name__ == '__main__':
    connect()

def hello():
   message = 'Приветствуем Вас в Агрегаторе Новостей!'
   return message, ''

hello_command = command_system.Command()

hello_command.keys = ['привет', 'hello', 'здравствуй', 'здравствуйте']
hello_command.description = 'Приветствие'
hello_command.process = hello

def info():
    message = ''
    for c in command_system.command_list:
        message += c.keys[0] + ' - ' + c.description + '\n'
    return message, ''


info_command = command_system.Command()

info_command.keys = ['помощь', 'помоги', 'help']
info_command.description = 'Список команд'
info_command.process = info

def subscribe():
    message = 'Вы подписались на новостную рассылку.'
    return message


info_command = command_system.Command()

info_command.keys = ['подписаться', 'подписка', 'subscribe']
info_command.description = 'Подписка на новостную рассылку'
info_command.process = subscribe

def add():
    message = 'Вы добавили подписку на новостную рассылку.'
    return message


info_command = command_system.Command()

info_command.keys = ['добавить', 'обновить', 'add']
info_command.description = 'Добавить подписку на новостную рассылку'
info_command.process = add


def delete():
    message = 'Вы отписались от новостной рассылки.'
    return message


info_command = command_system.Command()

info_command.keys = ['отписаться', 'удалить', 'unsubscribe', 'delete']
info_command.description = 'Отписка от новостной рассылки'
info_command.process = delete

def get_news():
    newsapi = NewsApiClient(api_key='ef20673d0898483d92ccb1da29b78bd9')
    message = 'Наиболее релевантные новости по Вашим активным подпискам.'
    
    cursor = conn.cursor()
    cursor.execute("SELECT name FROM keywords WHERE user_id =")
    key_words = cursor.fetchone()
    cursor.execute("SELECT name FROM categories WHERE user_id =")
    categories = cursor.fetchone()
    cursor.close()
    
    all_articles = newsapi.get_everything(q=key_words,
                                      category=categories,
                                      language='ru',
                                      sort_by='relevancy',
                                      page=3)

    return message, all_articles


info_command = command_system.Command()

info_command.keys = ['получить', 'новости', 'get']
info_command.description = 'Получение списка наиболее релевантных новостей по активным подпискам.'
info_command.process = get_news
