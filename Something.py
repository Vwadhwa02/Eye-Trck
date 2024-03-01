import cv2
import numpy as np
import pyautogui

# Define the eye tracker
eye_tracker = cv2.TrackerCSRT_create()

# Define the initial eye position
eye_position = (0, 0)

# Define the scroll speed
scroll_speed = 10

# Define the scroll direction
scroll_direction = "vertical"

# Start the video capture
cap = cv2.VideoCapture(0)

# Loop until the user presses the Esc key
while True:

    # Capture a frame from the video capture
    ret, frame = cap.read()

    # Convert the frame to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Track the eyes
    success, eye_bbox = eye_tracker.update(gray)

    # If the eyes are tracked
    if success:

        # Calculate the eye movement
        eye_movement = (eye_bbox[0] - eye_position[0], eye_bbox[1] - eye_position[1])

        # Update the eye position
        eye_position = (eye_bbox[0], eye_bbox[1])

        # Scroll if the eye movement is large enough
        if abs(eye_movement[0]) > 10 or abs(eye_movement[1]) > 10:

            # Calculate the scroll amount
            scroll_amount = eye_movement[0] / scroll_speed if scroll_direction == "horizontal" else eye_movement[1] / scroll_speed

            # Scroll
            if scroll_direction == "horizontal":
                pyautogui.hscroll(scroll_amount)
            else:
                pyautogui.vscroll(scroll_amount)

    # Display the frame
    cv2.imshow("Frame", frame)

    # Press the Esc key to exit
    if cv2.waitKey(1) & 0xFF == 27:
        break

# Release the video capture
cap.release()

# Close all windows
cv2.destroyAllWindows()