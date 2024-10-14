from pytubefix import YouTube

def download_video(url):
    try:
        video = YouTube(url=url)
    except:
        raise 'Could not get video'

    d_video = video.streams.get_highest_resolution()

    try:
        d_video.download('youtubeDownloader/videos/')
    except:
        raise 'Could not download'
    
if __name__ == '__main__':
    while True:
        url = input('Type video url: \n>>>')
        try:
            download_video(url=url)
        except:
            print('Could not download video...')