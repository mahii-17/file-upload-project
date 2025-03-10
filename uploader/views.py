from django.shortcuts import render

# Create your views here.
from .forms import UploadFileForm

from django.http import HttpResponse


def home(request):
    return HttpResponse("<h1>Welcome to File Upload Project!</h1>")


def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
    else:
        form = UploadFileForm()
    return render(request, 'upload.html', {'form': form})
