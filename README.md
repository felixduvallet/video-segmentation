# extract_video_segments

Quick and dirty video segment extraction using ffmpeg.

There are many like it, but this one is mine.

## Usage:

Edit video_index.txt, providing the:
 - source video file path
 - start time (expressed in 00:00:00.0 notation)
 - duration in seconds

The extract_video_segments will load this index file, and extract the desired
segment from the video file.

The resulting file will be the same filename with -cutNN inserted in (e.g.,
awesome_video.mov -> awesome_video-cut.00.mov).
