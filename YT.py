import yt_dlp as ydl
import json
from datetime import datetime
import sys
import time

def download_video(url):
    try:
        ydl_opts = {
            'format': 'bestvideo+bestaudio/best',
            'outtmpl': '%(title)s.%(ext)s',  # Save with the video title as the filename
        }
        with ydl.YoutubeDL(ydl_opts) as ydl_obj:
            info_dict = ydl_obj.extract_info(url, download=True)
            title = info_dict.get('title', 'Unknown Title')
        
        print("\n**********Title**********")
        print("Video Title: " + title)
        return title, True

    except Exception as e:
        if "ffmpeg" in str(e):
            print("Error: ffmpeg is not installed. Please install ffmpeg to merge audio and video streams.")
        else:
            print(f"Error: {e}")
        return None, False

def update_json(title, url):
    print("**********Updating JSON File**********")
    
    def write_json(data, filename="Json_File.json"):
        with open(filename, "w") as f:
            json.dump(data, f, indent=4)
    
    try:
        with open("Json_File.json") as json_file:
            data = json.load(json_file)
            temp = data["YouTube"]
            adt = datetime.now()
            fdt = adt.strftime("%m/%d/%Y, %H:%M:%S")
            y = {"Video Title": title, "Source URL": url, "Date": fdt}
            temp.append(y)
            write_json(data)
            print("JSON File Updated Successfully!")
    
    except FileNotFoundError:
        print("JSON file not found! Creating a new file...")
        data = {"YouTube": []}
        y = {"Video Title": title, "Source URL": url, "Date": datetime.now().strftime("%m/%d/%Y, %H:%M:%S")}
        data["YouTube"].append(y)
        write_json(data)
        print("New JSON file created and updated successfully!")

if __name__ == "__main__":
    url = input("Please Enter Video URL: ")
    title, success = download_video(url)
    if success:
        update_json(title, url)
    time.sleep(3)
