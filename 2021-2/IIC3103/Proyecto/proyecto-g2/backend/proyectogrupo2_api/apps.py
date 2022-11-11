from django.apps import AppConfig


class Proyectogrupo2ApiConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'proyectogrupo2_api'

    def ready(self):
        from proyectogrupo2_api.scheduleUpdater import updater
        updater.start()