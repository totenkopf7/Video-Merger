from tkinter import simpledialog
from moviepy.editor import *
from moviepy.video.io.VideoFileClip import VideoFileClip
from tkinter import *
from tkinter import messagebox
import os
from tkinter.filedialog import askopenfilename


def space():
    space = Label(text="", bg="black")
    space.pack()


def open_location():
    global filename_splitted
    filename = askopenfilename()
    filename_ext = os.path.splitext(filename)
    filename_splitted = str(filename_ext).split('/')[4].split(".")[0].split(',')[0].split("'")[0]
    filename_ext_split = filename_ext[1][1:]
    if len(filename) > 1 and filename_ext_split == "mp4":
        path_url.config(text=filename_splitted, fg="green")
    else:
        messagebox.showwarning(title="oops", message="No video given!")
        path_url.config(text="Please specify a file (mp4)!", fg="red")
    return filename_splitted


def open_location_music():
    global filename_splitted
    filename = askopenfilename()
    filename_ext = os.path.splitext(filename)
    filename_splitted = str(filename_ext).split('/')[4].split(".")[0].split(',')[0].split("'")[0]
    filename_ext_split = filename_ext[1][1:]
    if len(filename) > 1 and filename_ext_split == "mp3":
        path_url.config(text=filename_splitted, fg="green")
    else:
        messagebox.showwarning(title="oops", message="No music given!")
        path_url.config(text="Please specify a file (mp3)!", fg="red")
    return filename_splitted


def ask_for_videos_and_concatenate(number_of_videos):
    video_files = []
    for i in range(0, number_of_videos):  # loop exactly n times (0..n-1)
        choosen_file = open_location()
        video_files.append(f"{choosen_file}.mp4")
    # read the files to clip objects
    clips = [VideoFileClip(f) for f in video_files]  # list-comprehension to shorten
    # concatenate the list of clips to a single MP4 using specific code
    final_clip = concatenate_videoclips(clips)  # now argument clips is a list ;-)
    final_clip.write_videofile(f"{video_title}.mp4", codec="libx264")
    return final_clip


def merge_videos():
    global video_title
    video_title = simpledialog.askstring(title='Choose a title', prompt='Choose a title for your video?:')
    if len(video_title) == 0:
        messagebox.showwarning("Error", "Please give your video a title.")
    number_of_videos = int(box.get())  # read the user-input as number from text-box
    if number_of_videos in range(2, 8):
        ask_for_videos_and_concatenate(number_of_videos)
    else:
        messagebox.showwarning(title="Warning",
                               message="Please specify how many videos you want to merge. Must be at least 2 and maximum 7.")
    return


def add_music():
    m_video_title = simpledialog.askstring(title='Choose a title', prompt='Choose a title for your video?:')

    if len(m_video_title) == 0:
        messagebox.showwarning("Error", "Please give your video a title.")
    else:
        audio = AudioFileClip(f"{open_location_music()}.mp3")
        video1 = VideoFileClip(f"{open_location()}.mp4")
        final = video1.set_audio(audio)
        final.write_videofile(f"{m_video_title}.mp4")
        return


root = Tk()

space()
space()

root.title("Video Editor")
root.geometry("350x350")
root.columnconfigure(0, weight=1)
root.config(bg="black")

space()

label = Label(root, text="How many videos do you want to merge:", bg="black", fg="white", font=("jost", 9, "bold"))
label.pack()

EntryVar = StringVar()
box = Entry(root, width=7, textvariable=EntryVar)
box.pack()

space()
space()
space()

merge_btn = Button(root, width=27, height=1, bg="green", fg="white", text="Choose and Merge Videos",
                   command=merge_videos)
merge_btn.pack()

space()

add_music_btn = Button(root, width=27, height=1, bg="green", fg="white", text="Add Music to Your Merged Video",
                       command=add_music)
add_music_btn.pack()

path_url = Label(root, text="", fg="red", bg="black", font=("jost", 9, "bold"))
path_url.pack()

root.mainloop()
