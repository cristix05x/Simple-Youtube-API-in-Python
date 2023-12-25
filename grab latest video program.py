from googleapiclient.discovery import build
import tkinter as tk

def get_latest_video(channel_name):
    try:
        # Use the YouTube Data API to search for the channel by name
        search_response = youtube.search().list(
            q=channel_name,
            type="channel",
            part="id"
        ).execute()

        if "items" in search_response:
            # Get the ID of the first channel found
            channel_id = search_response["items"][0]["id"]["channelId"]

            # Use the YouTube Data API to get the latest video from the channel
            videos_response = youtube.search().list(
                channelId=channel_id,
                 order="date",
                 type="video",
                 part="id",
                 maxResults=1
             ).execute()
 
            if "items" in videos_response:
                 video_id = videos_response["items"][0]["id"]["videoId"]
                 video_url = f"https://www.youtube.com/watch?v={video_id}"
                 result_label.config(text=f"Latest video of {channel_name}: {video_url}")
            else:
                 result_label.config(text="No videos found for this channel")
        else:
             result_label.config(text="Channel not found")
    except Exception as e:
         result_label.config(text=f"An error occurred: {str(e)}")
 
# Set up YouTube Data API
youtube = build("youtube", "v3", developerKey='YOUR_API_KEY')
 
# Create the main Tkinter window
root = tk.Tk()
root.title("YouTube API with Tkinter")
 
# Create an entry for the user to input the channel name
channel_entry = tk.Entry(root)
channel_entry.pack(pady=10)
 
# Create a button to trigger the YouTube API call
get_video_button = tk.Button(root, text="Get Latest Video", command=lambda: get_latest_video(channel_entry.get()))
get_video_button.pack(pady=10)
 
# Create a label to display the result
result_label = tk.Label(root, text="")
result_label.pack(pady=10)
 
# Run the Tkinter event loop
root.mainloop()
