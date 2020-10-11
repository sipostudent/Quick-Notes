# document/views.py


from django.shortcuts import render

from .models import Document


def editor(request):
    docid = int(request.GET.get('docid', 0))
    documents = Document.objects.all()

    context = {
        'docid': docid,
        'documents': documents
    }

    return render(request, 'editor.html', context)
