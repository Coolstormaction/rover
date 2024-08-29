import tkinter as tk
import tkinter.font as tkFont
import math
from PIL import Image, ImageTk
import cv2
import numpy as np

class Joystick(tk.Canvas):
    def __init__(self, master, callback, size=200):
        super().__init__(master, width=size, height=size, bg='white', highlightthickness=0)
        self.callback = callback
        self.size = size
        self.radius = size / 2
        self.center = self.radius
        self.inner_radius = size / 4
        
        # Draw the outer circle (joystick base) with vibrant colors
        self.create_oval(
            self.center - self.radius,
            self.center - self.radius,
            self.center + self.radius,
            self.center + self.radius,
            fill='#4CAF50',  # Vibrant green
            outline='#388E3C'  # Darker green for border
        )
        
        # Draw the inner circle (joystick handle) with vibrant colors
        self.inner_circle = self.create_oval(
            self.center - self.inner_radius,
            self.center - self.inner_radius,
            self.center + self.inner_radius,
            self.center + self.inner_radius,
            fill='#FFC107',  # Vibrant amber
            outline='#FFA000'  # Darker amber for border
        )
        
        self.bind("<B1-Motion>", self.on_drag)
        self.bind("<ButtonRelease-1>", self.on_release)

    def on_drag(self, event):
        dx = event.x - self.center
        dy = event.y - self.center
        distance = math.sqrt(dx**2 + dy**2)
        
        # Clamp distance to joystick radius to prevent moving out of bounds
        if distance > self.radius:
            dx = (dx / distance) * self.radius
            dy = (dy / distance) * self.radius

        # Update inner circle position
        self.coords(self.inner_circle, 
                    self.center + dx - self.inner_radius, 
                    self.center + dy - self.inner_radius,
                    self.center + dx + self.inner_radius, 
                    self.center + dy + self.inner_radius)
        
        # Normalize joystick position
        x_normalized = dx / self.radius
        y_normalized = dy / self.radius
        self.callback(x_normalized, y_normalized)

    def on_release(self, event):
        # Reset joystick to center position
        self.coords(self.inner_circle,
                    self.center - self.inner_radius,
                    self.center - self.inner_radius,
                    self.center + self.inner_radius,
                    self.center + self.inner_radius)
        self.callback(0, 0)  # Joystick released, no movement

def joystick_callback(x, y):
    # Print joystick position for testing
    if abs(x) > 0.5:
        if x > 0:
            print("Moving Right")
        else:
            print("Moving Left")
    elif abs(y) > 0.5:
        if y > 0:
            print("Moving Down")
        else:
            print("Moving Up")
    else:
        print("Centered")

def move_arm(command):
    # Print arm command for testing
    print(f"Arm Command: {command}")

class CameraFeed(tk.Label):
    def __init__(self, master):
        super().__init__(master)
        self.video_source = 0  # Change to your camera index or video file path
        self.vid = cv2.VideoCapture(self.video_source)
        
        # Load the pre-trained MobileNet SSD model
        self.net = cv2.dnn.readNetFromCaffe('deploy.prototxt', 'mobilenet_iter_73000.caffemodel')
        self.classes = ["background", "aeroplane", "bicycle", "bird", "boat", "bottle", 
                        "bus", "car", "cat", "chair", "cow", "diningtable", "dog", 
                        "horse", "motorbike", "person", "pottedplant", "sheep", "sofa", 
                        "train", "tvmonitor"]
        
        self.update()
    
    def update(self):
        ret, frame = self.vid.read()
        if ret:
            # Perform object detection
            (h, w) = frame.shape[:2]
            blob = cv2.dnn.blobFromImage(cv2.resize(frame, (300, 300)), 1/255.0, (300, 300), swapRB=True, crop=False)
            self.net.setInput(blob)
            detections = self.net.forward()
            
            # Loop over detections and draw bounding boxes
            for i in range(detections.shape[2]):
                confidence = detections[0, 0, i, 2]
                if confidence > 0.5:
                    box = detections[0, 0, i, 3:7] * np.array([w, h, w, h])
                    (startX, startY, endX, endY) = box.astype("int")
                    label = f"{self.classes[int(detections[0, 0, i, 1])]}: {confidence:.2f}"
                    cv2.rectangle(frame, (startX, startY), (endX, endY), (0, 255, 0), 2)
                    cv2.putText(frame, label, (startX, startY - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
            
            # Convert the image to RGB (OpenCV uses BGR)
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            # Convert to ImageTk format
            self.photo = ImageTk.PhotoImage(image=Image.fromarray(frame))
            self.config(image=self.photo)
        self.after(10, self.update)  # Update every 10 ms
    
    def __del__(self):
        self.vid.release()

def create_gui():
    root = tk.Tk()
    root.title("Mars Rover Joystick Control")

    # Load SF Pro font
    try:
        custom_font = tkFont.Font(family="SF Pro", size=14, weight="bold")
    except tk.TclError:
        # If SF Pro is not found, use a fallback font
        custom_font = tkFont.Font(family="Arial", size=14, weight="bold")

    # Main frame
    main_frame = tk.Frame(root)
    main_frame.pack(padx=20, pady=20)

    # Joystick frame
    joystick_frame = tk.Frame(main_frame)
    joystick_frame.pack(side=tk.LEFT)

    # Create joystick
    joystick = Joystick(joystick_frame, joystick_callback)
    joystick.pack(pady=20)

    # Create camera feed
    camera_feed = CameraFeed(main_frame)
    camera_feed.pack(side=tk.RIGHT, padx=10, pady=10)

    # Button frame
    button_frame = tk.Frame(main_frame, bg='#f5f5f5')  # Light gray background for frame
    button_frame.pack(side=tk.RIGHT, padx=10)

    # Grab Button
    grab_button = tk.Button(
        button_frame, 
        text="Grab", 
        command=lambda: move_arm('grab'),
        bg='#FF5722',  # Vibrant orange
        fg='white',  # White text
        font=custom_font,  # Custom font
        relief='raised',
        bd=5,
        padx=15,
        pady=10
    )
    grab_button.grid(row=0, column=0, padx=10, pady=10)

    # Release Button
    release_button = tk.Button(
        button_frame, 
        text="Release", 
        command=lambda: move_arm('release'),
        bg='#03A9F4',  # Vibrant blue
        fg='white',  # White text
        font=custom_font,  # Custom font
        relief='raised',
        bd=5,
        padx=15,
        pady=10
    )
    release_button.grid(row=1, column=0, padx=10, pady=10)

    root.mainloop()

if __name__ == "__main__":
    create_gui()
