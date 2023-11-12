from django.shortcuts import render
import requests
from PIL import Image
from .pipeline import loaded_pipeline as pipeline
from math import ceil
from .models import ImagePicker
from statistics import mean

def home(request):
    return render(request, 'predictor/index.html')

def verify(request):
    if request.method == 'POST':
        file_input = request.FILES.get('file_input')
        if file_input == '':
            return render(request, 'predictor/inspect.html', {'error': 'Please choose the image before proceeding'})
        else:
            image = ImagePicker(image = file_input)
            image.save()
            im = Image.open(image.image)
            im.save('DeepGuardian/static/img/input_img.jpeg')
            if im.mode == 'CMYK':
                im = im.convert('RGB')
            result = pipeline.predict(image_path=im)
            return image_chooser(request, result)
    return render(request, 'predictor/inspect.html')

def image_chooser(request, result):
    faces = result['faces']
    scores = result['scores']
    overall_score = mean(scores) * 100
    fake_percentile = int(ceil(overall_score*100))
    status = ''
    if fake_percentile > 50:
        status = 'REAL'
    else:
        status = 'FAKE'
    overall_score = str(overall_score)
    overall_score = overall_score[:overall_score.index('.')+3]
    i=0
    for face in faces:
        face.save('DeepGuardian/static/img/face_{0}.jpeg'.format(i))
        i += 1
    st = []
    for c in range(i):
        img = 'img/face_{0}.jpeg'.format(c)
        count = c
        color = 'auto'
        if scores[c] > 0.50:
            color = 'red'
        else: 
            color = 'green'
        face_score = str(scores[c] * 100)
        face_score = face_score[:face_score.index('.')+3]
        st.append({'image':img, 'count':count, 'score': str(face_score) + ' %', 'color': color})
    return render(request, 'predictor/select.html', {'faces': st, 'overall_score': overall_score, 'overall_result': status})

def about(request):
    return render(request, 'predictor/about.html')
