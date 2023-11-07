from .core.Pipeline import DeepfakeDetectorPipeline

loaded_pipeline = DeepfakeDetectorPipeline(
                    model_name = 'EfficientNetAutoAttB4',
                    model_checkpoint = 'predictor/models/EfficientNetAutoAttB4_DFDC_bestval.pth',
                    face_detector_checkpoint = 'predictor/models/blazeface.pth',
                    face_detector_anchors = 'predictor/models/anchors.npy',
                    device = 'cpu'
                )