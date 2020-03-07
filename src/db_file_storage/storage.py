"""Custom Django FILE_STORAGE that saves files in the database."""

# python
import base64
import os
# third party
from django.apps import apps
from django.core.files.base import ContentFile
from django.core.files.storage import Storage
from django.db.models import BinaryField
from django.utils.crypto import get_random_string
from django.utils.http import urlencode
from django.utils.deconstruct import deconstructible
# project
from .compat import reverse


NAME_FORMAT_HINT = '<app>.<model>/<content_field>/<mimetype_field>' \
                   '/<filename_field>/<filename>'


class NameException(Exception):
    pass


@deconstructible
class DatabaseFileStorage(Storage):
    """File storage system that saves models' FileFields in the database.

    Intended for use with Models' FileFields.
    Uses a specific model for each FileField of each Model.
    """

    def _get_model_cls(self, model_class_path):
        app_label, model_name = model_class_path.rsplit('.', 1)
        return apps.get_model(app_label, model_name)

    def _get_encoded_bytes_from_file(self, content_field, _file):
        _file.seek(0)
        file_content = _file.read()
        encoded = base64.b64encode(file_content)
        if isinstance(content_field, BinaryField):
            return encoded
        return encoded.decode('utf-8')

    def _get_file_from_encoded_bytes(self, encoded_bytes):
        file_buffer = base64.b64decode(encoded_bytes)
        return ContentFile(file_buffer)

    def _get_unique_filename(self, model_cls, filename_field, filename):
        final_name = filename

        if ('.' in filename.rsplit(os.sep, 1)[-1]):
            stem, extension = final_name.rsplit('.', 1)
        else:
            stem, extension = (final_name, '')

        random_str = get_random_string(7)
        while model_cls.objects.filter(
            **{filename_field: final_name}
        ).exists():  # pragma: no cover
            final_name = '%s_(%s)%s' % (
                stem, random_str,
                ('.%s' % extension) if extension else ''
            )
            random_str = get_random_string(7)
        return final_name
