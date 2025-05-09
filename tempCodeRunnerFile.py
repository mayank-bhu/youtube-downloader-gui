import tkinter as tk
from pytube import YouTube
import customtkinter
from tkinter import filedialog

def startDownload(option):
    try:
        ytLink = link.get()
        ytObject = YouTube(ytLink, on_progress_callback=on_progress)
        if option == "hq":
            video = ytObject.streams.get_highest_resolution()
            file_path_hq = filedialog.asksaveasfilename(defaultextension=".mp4", filetypes=[("MP4 files", "*.mp4")])
            video.download(file_path_hq)
        elif option == "lq":
            video = ytObject.streams.get_lowest_resolution()
            file_path_lq = filedialog.asksaveasfilename(defaultextension=".mp4", filetypes=[("MP4 files", "*.mp4")])
            video.download(file_path_lq)
        elif option == "audio":
            video = ytObject.streams.get_audio_only()
            file_path_audio = filedialog.asksaveasfilename(defaultextension=".mp3", filetypes=[("Audio files", "*.mp3")])
            video.download(file_path_audio)
        else:
            return

        title.configure(text=ytObject.title, text_color="white")
        finishLabel.configure(text="")

        finishLabel.configure(text="Downloaded !!", text_color="green")
    except:
        finishLabel.configure(text="Download Error", text_color="red")



def on_progress(stream, chunk, bytes_remaining):
    total_size = stream.filesize
    bytes_download = total_size - bytes_remaining
    perecentage_of_completion = bytes_download / total_size * 100
    per = str(int(perecentage_of_completion))
    progress.configure(text=per + '%')
    progress.update()

    # Update ProgressBar
    progressbar.set(float(perecentage_of_completion) / 100)


# System settings
customtkinter.set_appearance_mode("system")
customtkinter.set_default_color_theme("blue")

# Our app frame

app = customtkinter.CTk()
app.geometry("720x480")
app.title("Mayank YT Link downloader")


# Adding Ui elements

title = customtkinter.CTkLabel(app, text="Mayank YouTube Link", width=200, height=50, font=("cursive", 26))
title.pack(padx=10, pady=10)

# Link Input
url_var = tk.StringVar()
link = customtkinter.CTkEntry(app, width=350, height=40, textvariable=url_var)
link.pack()

# Finished Downloading
finishLabel = customtkinter.CTkLabel(app, text="")
finishLabel.pack()

# Progress Percentage
progress = customtkinter.CTkLabel(app, text="0%")
progress.pack()

progressbar = customtkinter.CTkProgressBar(app, width=400)
progressbar.set(0)
progressbar.pack(padx=10, pady=10)


# Download High Quality Video Button
download_hq = customtkinter.CTkButton(app, text="Download High Quality-Mp4", command=lambda: startDownload("hq"))
download_hq.pack(padx=10, pady=10)

# Download Low Quality Video Button
download_lq = customtkinter.CTkButton(app, text="Download Low Quality-Mp4", command=lambda: startDownload("lq"))
download_lq.pack(padx=10, pady=10)

# Download Audio Button
download_a = customtkinter.CTkButton(app, text="Download Mp3", command=lambda: startDownload("audio"))
download_a.pack(padx=10, pady=10)


# Run app
app.mainloop()