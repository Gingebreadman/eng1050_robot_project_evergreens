from picamera import PiCamera

from picamera.array import PiRGBArray

import cv2

import time

# Initialize Camera
picam = Picamera()
picam.start()

try:
    while True:
        # Capture frame as a NumPy array
        frame = picam.capture_array()

        # Preprocessing: Grayscale and Thresholding
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        _, thresh = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)

        # Find Contours




        # Perimeter and Polygon Approximation
        peri = cv2.arcLength(cnt, True)
        approx = cv2.approxPolyDP(cnt, 0.04 * peri, True)
        num_corners = len(approx)

        # Identify Shape based on corner logic
        x, y, w, h = cv2.boundingRect(approx)
        shape = "Unknown"

        if num_corners == 3:
            shape = "Pepper"
        else:
            shape = "Not a pepper"

        # Draw contours and label on the frame
        cv2.drawContours(frame, [approx], -1, (0, 255, 0), 2)
        cv2.putText(frame, shape, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

    # Display the result
    cv2.imshow("Live Shape Detection", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

finally:
    picam.stop()
    cv2.destroyAllWindows()
