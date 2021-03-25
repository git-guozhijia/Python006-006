
"""
from importlib import import_module
def include(arg, namespace=None):
    app_name = None
    if isinstance(arg, tuple):
        pass

    if isinstance(urlconf_module, str):
        urlconf_module = import_module(urlconf_module)
        patterns = getattr(urlconf_module, 'urlpatterns', urlconf_module)
        app_name = getattr(urlconf_module, 'app_name', app_name)
        if namespace and not app_name:
            raise ImproperlyConfigured(
                'Specifying a namespace in include() without providing an app_name '
                'is not supported. Set the app_name attribute in the included '
                'module, or pass a 2-tuple containing the list of patterns and '
                'app_name instead.',
        )
    namespace = namespace or app_name
    # Make sure the patterns can be iterated through (without this, some
    # testcases will break).
    if isinstance(patterns, (list, tuple)):
        pass
    return (urlconf_module, app_name, namespace)
"""



