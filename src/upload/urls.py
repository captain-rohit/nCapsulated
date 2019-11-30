from django.urls import path
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
#from . import views
from .forms import DocForm
from .models import Doc
from db_file_storage.compat import url, reverse_lazy

app_name = 'upload'

urlpatterns = [
	url(
        r'^$',
        ListView.as_view(
            queryset=Doc.objects.all(),
            template_name='upload/doc_list.html'
        ),
        name='doc.list'
    ),
    url(
        r'^doc/add/$',
        CreateView.as_view(
            model=Doc,
            form_class=DocForm,
            template_name='upload/doc_form.html',
            success_url=reverse_lazy('upload:doc.list')
        ),
        name='doc.add'
    ),
    url(
        r'^doc/edit/(?P<pk>\d+)/$',
        UpdateView.as_view(
            model=Doc,
            form_class=DocForm,
            template_name='upload/doc_form.html',
            success_url=reverse_lazy('upload:doc.list')
        ),
        name='doc.edit'
    ),
    url(
        r'^doc/delete/(?P<pk>\d+)/$',
        DeleteView.as_view(
            model=Doc,
            template_name='upload/doc_confirm_delete.html',
            success_url=reverse_lazy('upload:doc.list')
        ),
        name='doc.delete'
    ),
]
