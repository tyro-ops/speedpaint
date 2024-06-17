import cv2
import numpy as np

def process_image(image_path):
    try:
        # Load the image
        image = cv2.imread(image_path)
        
        # Check if the image is loaded successfully
        if image is None:
            return None, "Error: Unable to load the image. Please check the file path."
        
        # Resize the image to a smaller size for faster processing
        image = cv2.resize(image, (400, 400))
        
        # Convert the image to grayscale
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        
        # Apply edge detection using Canny algorithm
        edges = cv2.Canny(gray, 100, 200)
        
        # Create a blank canvas for the hand-drawn effect
        canvas = cv2.cvtColor(edges, cv2.COLOR_GRAY2BGR)
        
        # Create a hand-drawn effect using lines
        for y in range(0, edges.shape[0], 10):
            for x in range(0, edges.shape[1], 10):
                if edges[y, x] > 0:
                    # Draw a line from the current point to a random point within a certain radius
                    x1 = np.random.randint(x - 10, x + 10)
                    y1 = np.random.randint(y - 10, y + 10)
                    cv2.line(canvas, (x, y), (x1, y1), (0, 0, 0), 2)
        
        # Blend the canvas with the original image
        result = cv2.addWeighted(image, 0.5, canvas, 0.5, 0)
        
        return result, None
    
    except cv2.error as e:
        return None, f"OpenCV error: {e}"