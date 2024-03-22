import requests
import base64
import json
from django.shortcuts import render
from rest_framework.views import APIView
from django.db.models.fields.json import JSONField
from django.conf import settings
from django.contrib import messages

def index(request):
    return render(request, 'index.html')

class FaceSenderView(APIView):

    def get(self, request, *args, **kwargs):
        return render(request, 'index.html')

    res = JSONField(default=dict)

    def post(self, request, *args, **kwargs):
        '''
        Send the image as a request to Gestalt Matcher web service
        '''

        if request.method == "POST":
            session_key = request.session._get_or_create_session_key()
            gm_image = request.FILES['gmImage'].read()  # get the uploaded file

            encoded_image = base64.b64encode(gm_image)
            encoded_image_str = encoded_image.decode("utf-8")

            try:
                res = requests.post(
                    settings.GESTALT_MATCHER_REST_API_URL,
                    json={
                        "img": encoded_image_str,
                    },
                )
            except requests.exceptions.RequestException as e:
                messages.error(request, 'Exception recieved from GestaltMatcher service:\n ' + str(e))
                return render(request, 'index.html')
            if not res.status_code == 200:
                messages.error(request, 'Error recieved from GestaltMatcher Service ')
                return render(request, 'index.html')

            jsonRes = json.dumps(res.json()).replace('null', '""')
            jsonRes = json.loads(jsonRes)

            context2 = {
                'imageName': request.FILES['gmImage'].name.split('.'),
                'jsonRes' : jsonRes,
                'sessID' : session_key
            }

            messages.success(request, 'Image submitted successfully : ' + request.FILES['gmImage'].name)

            # Render the HTML template index.html with the data in the context variable
            return render(request, 'index.html', context2)