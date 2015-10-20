import subprocess
import os


def get_extension(filepath):
    (_, ext) = os.path.splitext(filepath)
    return ext


def cut_one(filepath, number, start_time, duration):
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


def cut():

    # TODO: load a csv file.

    filepath = 'videos/CK03-P1.mov'
    number = 1
    start_time = '00:02:40.0'
    duration = 12

    print('Cutting')
    cut_one(filepath, number, start_time, duration)

    return


if __name__ == '__main__':
    cut()
