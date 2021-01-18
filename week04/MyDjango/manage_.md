python manage.py runserver 8080

from django.core.management import execute_from_command_line

execute_from_command_line(sys.argv)

execute_from_command_line(('manage.py','runserver','8080'))

/Users/qtt/Desktop/git-guozhijia/venv2/lib/python3.7/site-packages/django/core/management/__init__.py

def execute_from_command_line(('manage.py','runserver','8080')):
    """Run a ManagementUtility."""
    utility = ManagementUtility(('manage.py','runserver','8080'))
    utility.execute()

# OrderedDict导入高级数据类型，有序的字典
from collections import OrderedDict, defaultdict
import django
from django.apps import apps
from django.conf import settings
from django.core.exceptions import ImproperlyConfigured
from django.core.management.base import (
    BaseCommand, CommandError, CommandParser, handle_default_options,
)

class ManagementUtility:
    """
    Encapsulate the logic of the django-admin and manage.py utilities.
    """
    def __init__(self, argv=('manage.py','runserver','8080')):
        self.argv = argv or sys.argv[:]
    def execute(self):
        subcommand = self.argv[1]  # self.argv[1] = runserver
        settings.INSTALLED_APPS
        autoreload.check_errors(django.setup)()
        self.fetch_command(options.args[0]).print_help(self.prog_name, options.args[0])