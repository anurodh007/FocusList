from django.apps import AppConfig


class UsersConfig(AppConfig):
    name = 'users'

    def ready(request):
        import users.signals