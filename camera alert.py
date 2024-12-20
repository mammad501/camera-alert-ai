import cv2
import numpy as np
import winsound
from datetime import datetime
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

def play_alarm_sound():
    
    winsound.Beep(2000, 500)

def log_alert():
    with open("alerts_log.txt", "a") as log_file:
        log_file.write(f"Alert triggered at {datetime.now()}\n")

def start_camera(gui_elements):
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        messagebox.showerror("Error", "Could not open camera.")
        return

    back_sub = cv2.createBackgroundSubtractorMOG2()

    def update_frame():
        ret, frame = cap.read()
        if not ret:
            cap.release()
            gui_elements['video_label'].config(image="")
            return

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        fg_mask = back_sub.apply(gray)
        _, thresh = cv2.threshold(fg_mask, 244, 255, cv2.THRESH_BINARY)
        contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        for contour in contours:
            if cv2.contourArea(contour) > 500:
                x, y, w, h = cv2.boundingRect(contour)
                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)
                play_alarm_sound()
                log_alert()
                gui_elements['alert_text'].insert(tk.END, f"Alert triggered at {datetime.now()}\n")
                gui_elements['alert_text'].see(tk.END)

        img = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        img = Image.fromarray(img)
        imgtk = ImageTk.PhotoImage(image=img)
        gui_elements['video_label'].imgtk = imgtk
        gui_elements['video_label'].config(image=imgtk)

        if gui_elements['running']:
            gui_elements['video_label'].after(10, update_frame)
        else:
            cap.release()
            gui_elements['video_label'].config(image="")

    gui_elements['running'] = True
    update_frame()

def stop_camera(gui_elements):
    gui_elements['running'] = False

def create_gui():
    root = tk.Tk()
    root.title("AI Camera Alarm")

    gui_elements = {
        'running': False,
        'video_label': tk.Label(root),
        'alert_text': tk.Text(root, height=10, width=50)
    }

    gui_elements['video_label'].pack()

    start_button = tk.Button(root, text="Start Camera", command=lambda: start_camera(gui_elements))
    start_button.pack()

    stop_button = tk.Button(root, text="Stop Camera", command=lambda: stop_camera(gui_elements))
    stop_button.pack()

    tk.Label(root, text="Alerts:").pack()
    gui_elements['alert_text'].pack()

    root.mainloop()

if __name__ == "__main__":
    create_gui()
