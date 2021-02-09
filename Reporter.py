import os


def write_seq(dirpath, filename, seq):
    """

    :param dirpath: Directory
    :param filename: Filename
    :param seq: Sequence
    :return: Nothing. It writes the chosen sequence to a new file with the given name.
    """
    os.mkdir(dirpath)
    output_file = open(dirpath + filename, "w")
    output_file.write(seq)
    output_file.close()


