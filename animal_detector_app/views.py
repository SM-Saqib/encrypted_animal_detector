from xml.etree.ElementTree import PI
from django.shortcuts import render
from django.http import HttpResponse
import json
from django.template import loader

from encrytion import decryption
from Animal_detector import detector_pipeline

def index(request):
    simple_json_output={
        "id" : 12,
        "name": "test_response",
        "place": "we are part of a one"

    }
    # path_image="/media/saqib/VolumeD/Veeve/Dcube_stuff/Data/Samples-20211208T170336Z-001David_Parmenter_PGR01_5fd0e222940a1_inbound_pcp_file-2.png"
    # with open(path_image,"rb") as f:
    #     return HttpResponse(f.read(),content_type= "image/png")

    
    # return HttpResponse(json.dumps(simple_json_output, indent=4),content_type="application/json")


    template = loader.get_template('first.html')
    return HttpResponse(template.render())


def user_list(request):

    image=request  #get image url from the message body
    decrypted_image=decryption(image)

    response_animal_species = detector_pipeline.run(decrypted_image)

    return render(response_animal_species,'templates/user_list.html')
