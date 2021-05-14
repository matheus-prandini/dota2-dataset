import os


all_videos = (
    'bkb',
    'eul',
    'glyph',
    'lose',
    'roshan',
    'shiva',
    'shrine',
    'teamFight',
    'teleport',
    'towerDestroy'
)


def process_videos(video_list=all_videos):
    for video in video_list:
        if os.path.exists("Events/" + video):
            for i in range(1, 11):
                video_name = "Events/" + video + '/' + video + '_' + str(i) + '.mp4'
                print(video_name)
                destination = './frames/' + video + '/' + video + '_'
                if not os.path.exists('./frames/' + video + '/'):
                    os.makedirs('./frames/' + video + '/')
                get_frame(video_name, destination)


def get_frame(video, directory):
    """
    extract frames from videos with given FPS
    """

    fps = '30'
    dest = video[-5:-4]  # The folder that the frame images will end up in
    os.system('ffmpeg -i ' + video + ' -vf scale=720:720' +
              ' -r ' + fps + ' ' + directory + dest + '_%03d.png')


def main():
    process_videos()


if __name__ == '__main__':
    main()
