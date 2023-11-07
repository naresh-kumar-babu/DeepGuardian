import torch
from PIL import Image

import torchvision.transforms as transforms
from .blazeface import FaceExtractor, BlazeFace
from .architectures import fornet,weights
from .isplutils import utils

class DeepfakeDetectorPipeline():
    def __init__(self, device, model_name, model_checkpoint, face_detector_checkpoint, face_detector_anchors):

        self.device = device 
        self.face_policy = 'scale'
        self.face_size = 224
        
        self.net_model = model_name
        self.net = getattr(fornet,self.net_model)().eval().to(device)
        self.net.load_state_dict(torch.load(model_checkpoint))

        self.transforms = utils.get_transformer(self.face_policy, self.face_size, self.net.get_normalizer(), train=False)

        facedet = BlazeFace().to(device)
        facedet.load_weights(face_detector_checkpoint)
        facedet.load_anchors(face_detector_anchors)
        self.face_extractor = FaceExtractor(facedet=facedet)

    def predict_from_image_tensor(self, image_tensor):
        with torch.no_grad():
            pred = torch.sigmoid(self.net(image_tensor.to(self.device))).cpu().numpy().flatten()[0]
        return pred 

    def get_pil_from_nchw(self, nchw_tensor):
        pil = transforms.ToPILImage()(nchw_tensor)
        return pil 

    def predict(self, image_path, num_faces = 1):
        im_faces_all = self.face_extractor.process_image(img=image_path)

        pred_scores = []
        detected_faces = []

        for i in range(len(im_faces_all['faces'])):

            im_face_np = im_faces_all['faces'][i]
            
            face_tensor = self.transforms(image=im_face_np)['image'].unsqueeze(0) 
            pred = self.predict_from_image_tensor(image_tensor = face_tensor)

            pred_scores.append(pred)
            detected_faces.append(Image.fromarray(im_face_np))

        D = {
            'scores': pred_scores,
            'faces': detected_faces
        }
        return D