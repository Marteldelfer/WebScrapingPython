from pytubefix import Search, YouTube

def search(text : str):

    results = Search(text)
    rtrn = []
    
    for index, result in enumerate(results.videos):
        print(f'{index + 1} >>>')
        print(f'Title: {result.title}')
        print(f'Url: {result.watch_url}')
        do_download = input('Do you want to download this video? (y/n) \n>>> ')

        if do_download == 'y':
            mode = input('In which format would you like to save? (mp3/mp4) \n>>> ')
            try:
                yt = YouTube(result.watch_url).streams
                if mode == 'mp4':
                    yt.get_highest_resolution().download('./youtubeSearch/videos/')
                elif mode == 'mp3':
                    yt.get_audio_only().download('./youtubeSearch/audios/', mp3=True)
            except:
                print('error')
        elif do_download == 'n':
            continue
        else:
            break


if __name__ == "__main__":

    while True:
        s = input('Search >>> ')
        if s == 'exit':
            break
        else:
            search(s)