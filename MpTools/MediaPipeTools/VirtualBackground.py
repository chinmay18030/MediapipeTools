import cv2
import numpy as np
import mediapipe as mp


class VirtualBackground:
    def __init__(self, modelSelection: int = 1):
        self.modelSelection = modelSelection
        self.mp_drawing = mp.solutions.drawing_utils
        self.mp_selfie_segmentation = mp.solutions.selfie_segmentation
        self.selfie_Seg = self.mp_selfie_segmentation.SelfieSegmentation(model_selection=self.modelSelection)

    def add_VirtualBackground(self, baseImg, bgImage):
        BG_COLOR = (192, 192, 192)  # gray
        results = self.selfie_Seg.process(baseImg)
        condition = np.stack(
            (results.segmentation_mask,) * 3, axis=-1) > 0.1

        if bgImage is None:
            bg_image = np.zeros(baseImg.shape, dtype=np.uint8)
            bg_image[:] = BG_COLOR
        else:
            bg_image = cv2.resize(bgImage, (640, 480))
        output_image = np.where(condition, baseImg, bg_image)
        return output_image



