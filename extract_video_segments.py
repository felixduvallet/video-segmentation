"""
Extracts video snippets from videos programmatically.

In an index file (see video_index.txt), specify the source video file,
the start time (expressed in 00:00:00.0 notation), and the duration in
seconds.

This python script will then extract the desired video segments, naming
the resulting file with -cutNN inserted in (e.g., awesome_video.mov ->
awesome_video-cut.00.mov).

Author: Felix Duvallet, felixd@gmail.com.
Comments and improvements welcome.

"""

from collections import defaultdict
import argparse
import numpy as np
import os
import subprocess
import sys


def get_extension(filepath):
    """ Extract the file extension from a full path. """
    (_, ext) = os.path.splitext(filepath)
    return ext


def extract_segment(filepath, number, start_time, duration):
    """ Extract a segment from a single video file

    Use the given start time and duration. The number is to create a
    unique output filename.
    """

    if not os.path.isfile(filepath):
        print('File {} does not exist, returning now instead of causing '
              'trouble.'.format(filepath))
        return

    extension = get_extension(filepath)

    filepath_no_ext = str.replace(filepath, extension, '')
    output_file = '{}.wmv'.format(filepath_no_ext)

    print('Converting video: {}, starting at {} for {}s \t -> {}'.format(
        filepath, start_time, duration, output_file))

    command = 'avconv -i {input} -qscale 2 -vcodec msmpeg4 -an {output}'.\
        format(input=filepath, output=output_file)

    print('  Running command {}'.format(command))

    try:
        subprocess.check_call(command.split())  # Must split all the arguments.
    except subprocess.CalledProcessError as exp:
        print('Exception caught: {}'.format(exp))
    return


def extract_all(index_file):
    """ Load the index file and extract all the desired video segments. """

    if not os.path.isfile(index_file):
        print('Index {} does not exist, cannot proceed.'.format(index_file))
        return

    data = np.genfromtxt(index_file, dtype=None, comments='#',
                         names=('filepath', 'start_time', 'duration'))
    # Keeps track of how many times each file was cut.
    file_counts = defaultdict(int)

    # Use ndenumerate to prevent problem if data only has a single element.
    for (_, (filepath, start_time, duration)) in np.ndenumerate(data):
        number = file_counts[filepath]
        file_counts[filepath] += 1

        extract_segment(filepath, number, start_time, duration)
    return


if __name__ == '__main__':

    parser = argparse.ArgumentParser(
        description='')
    parser.add_argument('--index', default='index-handovers.txt',
        help='Index file name (default=video_index.txt)')
    args = parser.parse_args(sys.argv[1:])
    index_filepath = args.index

    print('Using index file: {}'.format(index_filepath))
    extract_all(index_filepath)
