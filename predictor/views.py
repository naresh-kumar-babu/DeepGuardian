from django.shortcuts import render, redirect
import requests
from PIL import Image
from .pipeline import loaded_pipeline as pipeline
from math import ceil
from .models import ImagePicker

def home(request):
    return render(request, 'predictor/index.html')

def verify(request):
    if request.method == 'POST':
        url_input = request.POST.get('url_input')
        file_input = request.FILES.get('file_input')
        if (url_input == '') and (file_input == ''):
            return render(request, 'predictor/verify.html', {'error': 'Please choose the image in either of the two formats'})
        else:
            if url_input:
                im = Image.open(requests.get(url_input, stream=True).raw)
                result = pipeline.predict(image_path=im)
                return image_chooser(request, result)
            elif file_input:
                image = ImagePicker(image = file_input)
                image.save()
                im = Image.open(image.image)
                result = pipeline.predict(image_path=im)
                return image_chooser(request, result)
    return render(request, 'predictor/verify.html')

def image_chooser(request, result):
    faces = result['faces']
    scores = result['scores']
    i=0
    for face in faces:
        face.save('DeepGuardian/static/img/face_{0}.jpeg'.format(i))
        i += 1
    st = []
    for c in range(i):
        img = 'img/face_{0}.jpeg'.format(c)
        count = c
        st.append({'image':img, 'count':count})
    return render(request, 'predictor/select.html', {'faces': st})

def results(request, face):
    im = Image.open('DeepGuardian/static/img/face_{0}.jpeg'.format(face))
    filepath = 'img/face_{0}.jpeg'.format(face)
    result = pipeline.predict(image_path=im)
    result = result['scores'][0]
    fake_percentile = int(ceil(result*100))
    status = ''
    if fake_percentile > 50:
        status = 'FAKE'
    else:
        status = 'REAL'
    return render(request, 'predictor/results.html', {'fake':fake_percentile, 'filepath':filepath, 'status': status})
