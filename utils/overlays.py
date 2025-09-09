import cv2
import time

COLOR = (0, 255, 0)

def draw_boxes(img, detections, show_scores=True):
    out = img.copy()
    for cls, conf, (x1,y1,x2,y2) in detections:
        cv2.rectangle(out, (int(x1),int(y1)), (int(x2),int(y2)), COLOR, 2)
        if show_scores:
            label = f"{cls} {conf:.2f}"
            cv2.putText(out, label, (int(x1), int(y1)-6),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.6, COLOR, 2, cv2.LINE_AA)
    return out

def draw_hud(img, fps=0.0, model="yolov8n.pt"):
    out = img.copy()
    hud = f"{model} | {fps:.1f} FPS | {time.strftime('%H:%M:%S')}"
    cv2.putText(out, hud, (12, 28), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255,255,255), 2, cv2.LINE_AA)
    return out
