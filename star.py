import numpy as np
import cv2

# Create a blank white image
width, height = 400, 400
image = np.ones((height, width, 3), np.uint8) * 255  # White background

# Define the center of the star and the outer radius
center_x, center_y = width // 2, height // 2
outer_radius = 100

# Calculate inner radius (distance from center to the inner points)
inner_radius = int(outer_radius * 0.382)  # Approximately 38.2% of the outer radius

# Define angles for the five points of the star
angles = [72 * i for i in range(5)]


# Calculate the coordinates of the five outer points of the star
outer_points = [(int(center_x + np.cos(np.radians(angle)) * outer_radius),
                 int(center_y + np.sin(np.radians(angle)) * outer_radius))
                for angle in angles]

# Calculate the coordinates of the five inner points of the star
inner_points = [(int(center_x + np.cos(np.radians(angle + 36)) * inner_radius),
                 int(center_y + np.sin(np.radians(angle + 36)) * inner_radius))
                for angle in angles]

coordinates = np.array([], np.int32)
for i in range(5):
    j = i+1
    if(j >= 5):
        j = 0
    point1 = np.array(outer_points[i]).reshape(1, -1)
    point2 = np.array(inner_points[i]).reshape(1, -1)
    coordinates = np.vstack((coordinates, point1)) if coordinates.size else point1
    coordinates = np.vstack((coordinates, point2))
cv2.fillPoly(image, [coordinates],  color=(0, 0, 0),)
# Display the image with the star
cv2.imshow("Star", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
