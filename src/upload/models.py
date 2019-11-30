from django.db import models

# Create your models here.

from db_file_storage.model_utils import delete_file, delete_file_if_needed
from db_file_storage.compat import reverse

class Document(models.Model):
    document_pk = models.AutoField(primary_key=True)
    bytes = models.TextField()
    filename = models.CharField(max_length=255)
    mimetype = models.CharField(max_length=50)


class Doc(models.Model):
	doc_pk = models.AutoField(primary_key=True)
	name = models.CharField(max_length=100, unique=True)
	picture = models.FileField(upload_to='upload.Document/bytes/filename/mimetype', blank=True, null=True)

	def get_absolute_url(self):
		return reverse('upload:doc.edit', kwargs={'pk': self.pk})

	def save(self, *args, **kwargs):
		delete_file_if_needed(self, 'picture')
		super(Doc, self).save(*args, **kwargs)

	def delete(self, *args, **kwargs):
		super(Doc, self).delete(*args, **kwargs)
		delete_file(self, 'picture')

	def __str__(self):
		return self.name
