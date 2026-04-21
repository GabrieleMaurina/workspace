import cv2
import numpy as np


def get_cosine(p1, p2, p0):
    """Calculates the cosine of the angle between vectors (p1-p0) and (p2-p0)"""
    v1 = p1[0] - p0[0]
    v2 = p2[0] - p0[0]

    num = np.dot(v1, v2)
    den = np.linalg.norm(v1) * np.linalg.norm(v2)
    return num / (den + 1e-10)  # Add small epsilon to avoid division by zero


def is_rectangle(approx):
    """Checks if the 4-pointed shape has angles near 90 degrees"""
    max_cosine = 0
    for i in range(2, 5):
        # Calculate cosine of angles between sides
        cosine = abs(get_cosine(approx[i % 4], approx[i - 2], approx[i - 1]))
        max_cosine = max(max_cosine, cosine)

    # If max cosine is < 0.3, the angles are roughly between 72 and 108 degrees
    return max_cosine < 0.3

# Inside your loop:
# if len(approx) == 4 and cv2.isContourConvex(approx):
#     if is_rectangle(approx):
#         # This is a confirmed rectangle!


def detect_rectangles(image_path):
    # 1. Load image and preprocess
    img = cv2.imread(image_path)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)

    # 2. Edge detection
    edged = cv2.Canny(blurred, 50, 150)

    # 3. Find contours
    contours, _ = cv2.findContours(
        edged, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    rects = []
    for cnt in contours:
        # 4. Approximate the shape
        peri = cv2.arcLength(cnt, True)
        approx = cv2.approxPolyDP(cnt, 0.02 * peri, True)

        # 5. Filter for 4 points (rectangle/square)
        if len(approx) == 4 and cv2.isContourConvex(approx) and is_rectangle(approx):
            # Optional: Filter by area to ignore tiny noise
            if cv2.contourArea(cnt) > 100:
                rects.append(approx)
                cv2.drawContours(img, [approx], -1, (0, 255, 0), 3)

    cv2.imshow("Detected Rectangles", img)
    cv2.waitKey(0)
    return rects


detect_rectangles('shapes.png')
