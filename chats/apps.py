from django.apps import AppConfig


class ChatsConfig(AppConfig):
    name = 'chats'

class UsersConfig(AppConfig):
    default_auto_field = 'django.db.models.AutoField'
    name = 'users'