from django.apps import AppConfig


class CarsConfig(AppConfig):
    name = 'cars'
    # I create method ready, what django call once, when the app terminates the loading
    def ready(self):
        # I import the archive signals here come in, only the import, the @receiver are registres and the signals begin to function 
        import cars.signals
