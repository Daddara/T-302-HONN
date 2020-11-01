# Registry design pattern

Registry is an already implemented design pattern in Django. As stated in the documentation for the registry in the Django: “A registry that stores the configuration of installed applications. It also keeps track of models, e.g. to provide reverse relations”.

Django.apps.registry is a global object that stores information on every installed application within the system including: apps, models and configurations. This object is used as a finder for all of the applications to look-up and “talk” to each other. The settings.py itself is not the registry, instead the master registry, django.apps.registry, imports the installed applications within settings and populates the library. This is done with “def populate(self, installed_apps=None):” and then they can be easily found with any of the implemented get functions within the registry object, get_app_config, get_app_configs, get_models, get_model, get_containing_app_config or get_registered_model. 

