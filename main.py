import tkinter as tk
from tkinter import filedialog

from audio_processing import process_audio
from text_preprocessing import text_cleanup
import speech_recognition as sr


def upload_file():
    file_path = filedialog.askopenfilename(initialdir="/", title="Select Recording File",
                                           filetypes=(("WAV files", "*.wav"), ("all files", "*.*")))
    if file_path:
        # Process the uploaded file
        process_audio(file_path)

        # Preprocess the text data
        text_cleanup()

        # Perform sentiment analysis
        # perform_sentiment_analysis()

        # Generate graphs
        # Via 'perform_sentiment_analysis()' a call is made

        # Update GUI with analysis results
        with open("transcribed_text.txt", "r") as file:
            transcribed_text = file.read()
            text_display.delete(1.0, tk.END)  # Clear previous text
            text_display.insert(tk.END, transcribed_text)

    else:
        # Handle if no file is selected
        text_display.delete(1.0, tk.END)  # Clear previous text
        text_display.insert(tk.END, "No file selected")


def listen_microphone():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source)
        try:
            transcribed_text = r.recognize_google(audio)
            with open("transcribed_text.txt", "w") as file:
                file.write(transcribed_text)
            text_display.delete(1.0, tk.END)
            text_display.insert(tk.END, transcribed_text)

            # Preprocess the text data
            text_cleanup()

            # # Perform sentiment analysis
            # perform_sentiment_analysis()

            # Generate graphs
            # Via 'perform_sentiment_analysis()' a call is made

        except sr.UnknownValueError:
            text_display.delete(1.0, tk.END)
            text_display.insert(tk.END, "Could not understand the audio")
        except sr.RequestError:
            text_display.delete(1.0, tk.END)
            text_display.insert(tk.END, "Error. Please check your internet connection")


root = tk.Tk()

root.title("Sentiment Analysis on Real Phone Calls")
root.geometry("640x480")

# Heading
heading_label = tk.Label(root, text="Sentiment Analysis on Real Phone Calls", font=("Arial", 20))
heading_label.pack(pady=20)

# Frame for buttons
button_frame = tk.Frame(root)
button_frame.pack()

# Upload Button
upload_button = tk.Button(button_frame, text="Upload Recording", command=upload_file, bg="blue", fg="white")
upload_button.pack(side=tk.LEFT, padx=10, pady=10)

# Listen Button for Microphone
listen_button = tk.Button(button_frame, text="Listen", command=listen_microphone, bg="green", fg="white")
listen_button.pack(side=tk.LEFT, padx=10, pady=10)

# Text Display Area for Transcribed Audio
text_display = tk.Text(root, height=20, width=70)
text_display.pack(pady=20)

root.configure(bg='lightgray')  # Change background color

root.mainloop()
