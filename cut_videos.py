import subprocess
import os
import numpy as np
from collections import defaultdict


def get_extension(filepath):
    (_, ext) = os.path.splitext(filepath)
    return ext


def cut_one(filepath, number, start_time, duration):
    # Extract a segment from a single video file, using the given start time
    # and duration. The number is to create a unique output filename.

    if not os.path.isfile(filepath):
        print('File {} does not exist, returning now instead of causing '
              'trouble.'.format(filepath))
        return

    extension = get_extension(filepath)

    filepath_no_ext = str.replace(filepath, extension, '')
    output_file = '{}-cut.{:02}{}'.format(filepath_no_ext, number, extension)

    print('Cutting video: {}, starting at {} for {}s \t -> {}'.format(
        filepath, start_time, duration, output_file))

    command = 'ffmpeg -i {input} -ss {start} -c copy -t {duration} {output}'.\
        format(input=filepath, start=start_time,
               duration=duration, output=output_file)

    print('  Running command {}'.format(command))

    try:
        subprocess.check_call(command.split())  # Must split all the arguments.
    except subprocess.CalledProcessError as e:
        print('Exception caught: {}'.format(e))
    return


def cut(index_file):

    data = np.genfromtxt(index_file, dtype=None, comments='#',
                         names=('filepath', 'start_time', 'duration'))

    # Keeps track of how many times each file was cut.
    file_counts = defaultdict(int)

    for (filepath, start_time, duration) in data:
        number = file_counts[filepath]
        file_counts[filepath] += 1

        cut_one(filepath, number, start_time, duration)
    return


if __name__ == '__main__':
    cut('files_to_cut.txt')
