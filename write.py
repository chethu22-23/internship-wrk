
import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load the image
img = cv2.imread(r"C:\Users\91895\Pictures\Saved Pictures\face.jpg")

# Check if the image was loaded successfully
if img is not None:
    # Write the image to a file
    cv2.imwrite(r"C:\Users\91895\Pictures\Saved Pictures\face123.jpg", img)
    print("Image saved successfully.")
else:
    print("Failed to load the image.")

# Convert the image from BGR to RGB
RGB_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# Display the image using matplotlib
plt.imshow(RGB_img)
plt.waitforbuttonpress()
plt.close('all')
