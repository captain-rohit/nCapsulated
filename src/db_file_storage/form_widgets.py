# python
import sys
# third party
from django.utils.html import escape
from django.forms.widgets import ClearableFileInput
from django.contrib.admin.widgets import AdminFileWidget

if sys.version_info.major == 2:  # python2
    from urllib import unquote
else:  # python3
    from urllib.parse import unquote


def db_file_widget(cls):
    """Edit the download-link inner text."""


@db_file_widget
class DBClearableFileInput(ClearableFileInput):
    template_name = 'db_file_storage/widgets/clearable_file_input.html'


@db_file_widget
class DBAdminClearableFileInput(AdminFileWidget):
    template_name = 'db_file_storage/widgets/admin_clearable_file_input.html'
