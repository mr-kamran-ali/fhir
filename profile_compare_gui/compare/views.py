from django.shortcuts import render
import subprocess
import os
from django.conf import settings
from django.http import HttpResponse, Http404
import shutil
from os import listdir
from os.path import isfile, join

def home(request):
    if request.method == 'POST':
        ig1 = request.POST.get('ig1')
        ig2 = request.POST.get('ig2')

        if not ig1:
            ig1 = "smart4health.eu.core#0.5.2"

        if not ig2:
            ig2 = "https://build.fhir.org/ig/hl7-eu/x-ehealth"

        pr1 = request.POST.get('pr1')
        pr2 = request.POST.get('pr2')

        media_path = f"{settings.MEDIA_ROOT}/ig_compare/"
        file_name = pr2.split('/')[-1]

        dir_name = f"{media_path}{file_name}"
        cmd_mkdir = ["mkdir","-p",dir_name]
        subprocess.run(cmd_mkdir)

        cmd_compare = ["java", "-jar", "validator_cli.jar", "-dest", dir_name, "-version", "4.0", "-ig", ig1, "-ig", ig2, "-left", pr1, "-right", pr2 ]
        subprocess.run(cmd_compare)

        shutil.make_archive(base_name=file_name, format='zip', root_dir=media_path, base_dir=file_name)

        myfiles = [f for f in listdir(media_path) if isfile(join(media_path, f))]
        myfiles = myfiles

        print(myfiles)
        return render(request, "file_list.html", {"myfiles":myfiles})

    else:
        return render(request, "index.html")


def download(request, file_name):
    file_name = file_name.split('/')[-1]
    dir_name = f"{settings.BASE_DIR}{settings.MEDIA_URL}ig_compare/{file_name}"
    shutil.make_archive(file_name, 'zip', dir_name)


    with open(f"{file_name}.zip", 'rb') as fh:
        response = HttpResponse(fh.read(), content_type="application/zip")
        response['Content-Disposition'] = 'inline; filename=' + os.path.basename(f"{file_name}.zip")
        return response

