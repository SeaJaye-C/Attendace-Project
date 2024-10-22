import os
import tkinter as tk
import tools
import cv2
from PIL import Image, ImageTk
import face_recognition as face
import pickle
import subprocess

class App:
    def __init__(self):
        self.main_window = tk.Tk()
        self.main_window.geometry("1200x520+350+100")

        self.login_button_main_window = tools.get_button(self.main_window, 'login', 'red', self.login, fg='black')
        self.login_button_main_window.place(x=750, y=300)

        self.register_new_user_button_main_window = tools.get_button(self.main_window, 'Register new user', 'green', self.register_new_user, fg='black')
        self.register_new_user_button_main_window.place(x=750, y=400)

        self.webcam_label = tools.get_img_label(self.main_window)
        self.webcam_label.place(x=10, y=0, width=700, height=500)

        self.add_webcam(self.webcam_label)

        self.db_dir = './db'
        if not os.path.exists(self.db_dir):
            os.mkdir(self.db_dir)

    def add_webcam(self, label):
        if 'cap' not in self.__dict__:
            self.cap = cv2.VideoCapture(0)
        self._label = label
        self.process_webcam()

    def process_webcam(self):
        ret, frame = self.cap.read()
        if not ret:
            print("Failed to grab frame")
            return

        self.most_recent_capture_arr = frame
        
        # Convert BGR to RGB
        img_ = cv2.cvtColor(self.most_recent_capture_arr, cv2.COLOR_BGR2RGB)
        self.most_recent_capture_pil = Image.fromarray(img_)

        imgtk = ImageTk.PhotoImage(image=self.most_recent_capture_pil)
        self._label.imgtk = imgtk
        self._label.configure(image=imgtk)

        self._label.after(20, self.process_webcam)

    def login(self):
                unknown_img_path = './.tmp.jpg'

                # Convert to RGB before saving
                rgb_frame = cv2.cvtColor(self.most_recent_capture_arr, cv2.COLOR_BGR2RGB)
                
                # Save the RGB image
                cv2.imwrite(unknown_img_path, rgb_frame)

                unknown_image = face.load_image_file(unknown_img_path)

                # Check if a face is found and get the encodings
                unknown_encodings = face.face_encodings(unknown_image)
                if len(unknown_encodings) == 0:
                    # Show message if no face detected
                    tools.msg_box('Error', 'No face detected in the image.')
                    print("No face detected in the image.")
                    os.remove(unknown_img_path)
                    return
                
                unknown_encoding = unknown_encodings[0]

                # Iterate through known images in db_dir
                for filename in os.listdir(self.db_dir):
                    if filename.endswith('.jpg'):
                        known_image = face.load_image_file(os.path.join(self.db_dir, filename))
                        known_encodings = face.face_encodings(known_image)

                        if len(known_encodings) == 0:
                            print(f"No face found in {filename}. Skipping.")
                            continue

                        known_encoding = known_encodings[0]

                        # Compare faces
                        results = face.compare_faces([known_encoding], unknown_encoding)

                        if results[0]:
                            # Extract the name from the filename (remove the .jpg extension)
                            user_name = filename.split('.')[0]
                            tools.msg_box('Success', f'Welcome, {user_name}!')
                            print(f"User {user_name} recognized!")
                            os.remove(unknown_img_path)
                            return True
                
                # If no match found
                tools.msg_box('Error', 'No match found.')
                print("No match found.")
                os.remove(unknown_img_path)
                return False


    def register_new_user(self):
        self.register_new_user_window = tk.Toplevel(self.main_window)
        self.register_new_user_window.geometry("1200x520+350+100")

        self.accept_button_register_new_user_window = tools.get_button(self.register_new_user_window, 'Accept', 'red', self.accept_register_new_user, fg='black')
        self.accept_button_register_new_user_window.place(x=750, y=300)

        self.try_again_button_register_new_user_window = tools.get_button(self.register_new_user_window, 'Try Again', 'red', self.try_again_register_new_user, fg='black')
        self.try_again_button_register_new_user_window.place(x=750, y=400)

        self.capture_label = tools.get_img_label(self.register_new_user_window)
        self.capture_label.place(x=10, y=0, width=700, height=500)

        self.add_img_to_label(self.capture_label)

        self.entry_text_register_new_user = tools.get_entry_text(self.register_new_user_window)
        self.entry_text_register_new_user.place(x=750, y=130)

        self.text_label_register_new_user = tools.get_text_label(self.register_new_user_window, 'Please, Input username: ')
        self.text_label_register_new_user.place(x=750, y=65)

        self.text_label_register_new_user = tools.get_text_label(self.register_new_user_window, 'Make sure your full face is in the frame :)')
        self.text_label_register_new_user.place(x=750, y=95)

    def try_again_register_new_user(self):
        self.register_new_user_window.destroy()

    def add_img_to_label(self, label):
        imgtk = ImageTk.PhotoImage(image=self.most_recent_capture_pil)
        label.imgtk = imgtk
        label.configure(image=imgtk)

        self.register_new_user_capture = self.most_recent_capture_arr.copy()

    def accept_register_new_user(self):
        name = self.entry_text_register_new_user.get(1.0, "end-1c")
        cv2.imwrite(os.path.join(self.db_dir, '{}.jpg'.format(name)), self.register_new_user_capture)

        tools.msg_box('Success', 'User was registered successfully!')
        self.register_new_user_window.destroy()

    def start(self):
        self.main_window.mainloop()

if __name__ == "__main__":
    app = App()
    app.start()
