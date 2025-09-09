from ultralytics import YOLO
import numpy as np

# Simple in-memory cache keyed by (key, frame_idx)
class CachedDetections:
    def __init__(self): self._m = {}
    def get(self, key, i): return self._m.get((key, i))
    def put(self, key, i, dets): self._m[(key, i)] = dets

class Detector:
    def __init__(self, model_name, conf_thr=0.35, iou_thr=0.5):
        self.model = YOLO(model_name)
        self.conf_thr = conf_thr
        self.iou_thr = iou_thr

    def predict(self, frame_bgr):
        # Ultralytics expects RGB
        results = self.model.predict(frame_bgr[..., ::-1], conf=self.conf_thr, iou=self.iou_thr, verbose=False)
        dets = []
        if not results:
            return dets
        r = results[0]
        if r.boxes is None: return dets
        for b in r.boxes:
            cls_id = int(b.cls[0])
            conf = float(b.conf[0])
            x1,y1,x2,y2 = map(float, b.xyxy[0].tolist())
            label = r.names.get(cls_id, str(cls_id))
            dets.append((label, conf, (x1,y1,x2,y2)))
        return dets
