from django.apps import AppConfig


class UsersConfig(AppConfig):
    name = 'users'

    def ready(self):  # required to be imported this way to avoid unwanted side effects (django documentation)
        import users.signals
