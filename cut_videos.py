import subprocess


def cut_one(filepath, number, start_time, duration):
    print('Cutting video: {}, starting at {} for {}s'.format(
        filepath, start_time, duration))

    # TODO figure out extension.
    output_file = '{}-cut.{:02}.mov'.format(filepath, number)
    print('  Output: {}'.format(output_file))

    command = 'ffmpeg -i {input} -ss {start} -c copy -t {duration} {output}'.\
        format(input=filepath, start=start_time,
               duration=duration, output=output_file)
    print 'Running command {}'.format(command)

    subprocess.check_call(command.split())  # Must split all the arguments.

    return True


def cut():

    # TODO: load a csv file.

    filepath = 'CK03-P1.mov'
    number = 1
    start_time = '00:02:40.0'
    duration = 12

    print('Cutting')
    cut_one(filepath, number, start_time, duration)


    return


if __name__ == '__main__':
    cut()
