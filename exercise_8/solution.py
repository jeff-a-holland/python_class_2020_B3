#!/Users/jeff/.pyenv/shims/python

import sys
import os
import cv2
import pandas
import time

class AnalyzeVideo(object):
    """AnalyzeVideo class"""
    video_list = []
    video_duration_list = []
    def __init__(self):
        pass

    def find_videos(self, dir):
        """Get list of videos in the directory supplied as an arg to
           the script"""
        self.dir = dir
        for file in os.listdir(dir):
            if file.lower().endswith('.mp4'):
                AnalyzeVideo.video_list.append(file)

    def process_videos(self, dir):
        """Process videos to determine their length in minutes"""
        self.dir = dir
        print(f'\nVideos in the directory "{dir}" with their duration in '
               'minutes include:\n')
        for value in AnalyzeVideo.video_list:
            video = cv2.VideoCapture(value)
            fps = video.get(cv2.CAP_PROP_FPS)
            frames = int(video.get(cv2.CAP_PROP_FRAME_COUNT))
            video_duration =float( "{:.2f}".format((frames/fps)/60))
            print(f'File "{value}" has length: {video_duration}min')
            AnalyzeVideo.video_duration_list.append(video_duration)
        video_duration_series = pandas.Series(AnalyzeVideo.video_duration_list)
        return video_duration_series

def main():
    """Take an inventory of the .mp4 files in the current directory and report
       on the time of each video, total time of all videos, as well as average
       time of all videos.
    """
    argv_list = sys.argv
    argv_list.pop(0)

    if len(argv_list) != 1:
        raise ValueError('Only one argument allowed.\n')
    else:
        dir = argv_list.pop()
        av = AnalyzeVideo()
        av.find_videos(dir)
        series = av.process_videos(dir)

        mean = series.mean()
        min = series.min()
        max = series.max()
        std = series.std()
        sum = series.sum()
        sum_in_seconds = series.sum() * 60
        sum_formatted = time.strftime('%H:%M:%S', time.gmtime(sum_in_seconds))


        print(f'\nPandas Series is:\n\n{series}\n')
        print(f'Min of video times is: {min:.2f} minutes')
        print(f'Max of video times is: {max:.2f} minutes')
        print(f'Mean of video times is: {mean:.2f} minutes')
        print(f'Standard deviation of video times is: {std:.2f} minutes')
        print(f'Sum of all video times is: {sum} minutes')
        print(f'Sum of all video times in HH:MM:SS format is: {sum_formatted}\n')

if __name__ == "__main__":
    main()
