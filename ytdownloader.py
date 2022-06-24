from pytube import YouTube
import os

print("__   __ _____   ____                           _                    _")
print("\ \ / /|_   _| |  _ \   ___  __      __ _ __  | |  ___    __ _   __| |  ___  _ __")
print(" \ V /   | |   | | | | / _ \ \ \ /\ / /| '_ \ | | / _ \  / _` | / _` | / _ \| '__|")
print("  | |    | |   | |_| || (_) | \ V  V / | | | || || (_) || (_| || (_| ||  __/| |")
print("  |_|    |_|   |____/  \___/   \_/\_/  |_| |_||_| \___/  \__,_| \__,_| \___||_|")

print(' ')
print(' ')
print('Paste link of YouTube Video:')
x = input()


url =YouTube(x)
video = url.streams.get_highest_resolution()
video.download()
print("Your video has been downloaded at script path.")
print(' ')
print("Press any key to exit...")
os.system("pause > nul")
