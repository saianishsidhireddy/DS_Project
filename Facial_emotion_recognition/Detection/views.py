from django.shortcuts import render
from django.core.files.storage import default_storage
from .models import CapturedImage
from .Backend import predict_emotion


def predict_emotion_view(request):
    if request.method == 'POST':
        uploaded_image = request.FILES['image']
        image_path = default_storage.save('temp/' + uploaded_image.name, uploaded_image)
        recognized_emotion = predict_emotion(image_path)  # Implement this function using your model
        return render(request, 'result.html', {'recognized_emotion': recognized_emotion})
    
    return render(request, 'upload.html')
