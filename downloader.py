from pytube import YouTube

done = False


def download(video):
    #
    video.download("downloads/")
    return True


youtube_url = "https://www.youtube.com/watch?v=9bZkp7q19f0"
myVideo = YouTube(youtube_url)
# print("Title: " + myVideo.title)
# print("Duration: " + str(myVideo.length))
# print("Thumbnail Link: " + myVideo.thumbnail_url)
# print("Description: " + myVideo.description)
# print("Views: " + str(myVideo.views))
# print("Age Restricted: " + str(myVideo.age_restricted))
# print("Video ID: " + myVideo.video_id)
# print("File Size: " + myVideo.filesize)

myVideoStreams = myVideo.streams

i = 1
for stream in myVideoStreams:
    # stream.download('downloads/')
    if stream.type == "video":
        print(i, 'Video', stream.resolution, stream.filesize)
    elif stream.type == "audio":
        print(i, 'Audio', stream.abr, stream.filesize)
    i += 1

n = int(input())
print(myVideoStreams[n-1].type, myVideoStreams[n-1].resolution, myVideoStreams[n-1].filesize)


done = download(myVideoStreams[n-1])
if done:
    print("DONE")




