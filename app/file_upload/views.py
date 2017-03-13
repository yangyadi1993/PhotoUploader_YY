from django.shortcuts import get_object_or_404, render, redirect

# Create your views here.
from django.http import HttpResponseRedirect, HttpResponse, Http404
from django.urls import reverse
from file_upload.forms import *



def index(request):
    if request.method == "GET":
        context = {'form': PictureForm()}
        return render(request, 'upload.html', context)

    new_picture = Picture()
    form = PictureForm(request.POST, request.FILES, instance=new_picture)

    if not form.is_valid():
        context = {'form': form}
        return render(request, 'upload.html', context)

    form.save()
    return redirect(reverse('index'))


def get_list(request):
    if request.method == "GET":
        context = {}
        picture_name = []
        picture = Picture.objects.all()
        for pic in picture:
            picture_name.append(pic.filename())
        context['picture'] = picture_name
        return render(request, 'picture_list.html', context)



from django.views.generic import View

from braces.views import (
    AjaxResponseMixin,
    JSONResponseMixin,
    LoginRequiredMixin,
    SuperuserRequiredMixin,
)


class AjaxPhotoUploadView(JSONResponseMixin,
                    AjaxResponseMixin,
                    View):

    def post_ajax(self, request, *args, **kwargs):
        uploaded_file = request.FILES['file']
        Picture.objects.create(picture=uploaded_file)

        response_dict = {
            'message': 'File uploaded successfully!',
        }

        return self.render_json_response(response_dict, status=200)
