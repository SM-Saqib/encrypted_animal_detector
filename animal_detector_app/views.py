from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from encrytion import decryption
from Animal_detector import detector_pipeline

def index(request):


    template = loader.get_template('first.html')
    return HttpResponse(template.render())


def user_list(request):

    image=request  #get image url from the message body
    decrypted_image=decryption(image)

    response_animal_species = detector_pipeline.run(decrypted_image)

    return render(response_animal_species,'templates/user_list.html')
