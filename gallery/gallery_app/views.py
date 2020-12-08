from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib import messages
from django.urls import reverse
from django.views.generic import ListView
from gallery_app.forms import galleryForm
from gallery_app.models import gallery_details


def index(request):
    if "GET" == request.method:
        return render(request, 'gallery_template/dashboard.html')
    if request.method == 'POST':
        extension_list = [".jpg",".jpeg",".png",".gif",]
        img_file = request.FILES["img"]
        if not any([img_file.name.endswith(e) for e in extension_list]):
            messages.error(request, 'This is not Image')
            return HttpResponseRedirect(reverse("dashboard"))
        form = galleryForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            form.save()
        context = {'form': form}
        messages.success(request, f' Image uploaded Successfully')
        return render(request, 'gallery_template/dashboard.html', context)

class gallerylist(ListView):
    model = gallery_details
    template_name = 'gallery_template/gallery.html'
    context_object_name = "imglist"

    def get_queryset(self):
        filter_val = self.request.GET.get('filter', 'give-default-value')
        if filter_val != "give-default-value":
            new_context = gallery_details.objects.filter(gallery_category=filter_val,).order_by('-id')
        else:
            new_context = gallery_details.objects.all().order_by('-id')
        return new_context