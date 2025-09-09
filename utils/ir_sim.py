import cv2

def to_ir(frame_bgr):
    gray = cv2.cvtColor(frame_bgr, cv2.COLOR_BGR2GRAY)
    gray = cv2.equalizeHist(gray)
    ir = cv2.applyColorMap(gray, cv2.COLORMAP_INFERNO)
    return ir
