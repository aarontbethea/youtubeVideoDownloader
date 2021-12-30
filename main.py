#A lightweight youtube video downloader, powered by pytube
#Aaron Bethea
#Date: 2021-12-29

import validators
from pytube import YouTube

if __name__ == '__main__':

  #prompt URL from user 
  print("YouTube Video Downloader")
  input_prompt = "Enter YouTube Video URL to download (type 'EXIT' to quit): "
  
  url = input(input_prompt)

  while url.lower().strip() != 'exit':

    #triple condition: must not be a blank space, must be an actual value and must be a URL
    if url and not str(url).isspace() and validators.url(url):
      if 'youtube.com' in url.lower():

        #get video data, always get highest resolution video in this case 
        try:
          video = YouTube(url)
          download = video.streams.get_highest_resolution()
        except Exception as exc:
          print("Something went wrong:")
          print(exc)
        else:
          print("Size in bytes: ",download.filesize)
          print(f"Downloading '{video.title}' in {download.resolution} from YouTube...")
          #download the video data
          download.download()
          
        finally:
          #prompt next url 
          url = input(input_prompt)
    else:
      print("Invalid Entry")
      url = input(input_prompt)
  print("Exiting Downloader")