import os

gene_pair_scores = {}


def write(dirpath, filename, seq):
    """
    :param dirpath: Directory
    :param filename: Fil
    :param seq: Sequenceename
    :return: Nothing. It writes the chosen sequence to a new file with the given name.
    """
    try:
        os.mkdir(dirpath)
    except FileNotFoundError:
        print("Incorrect filepath.")
        return False

    output_file = open(dirpath + filename, "w")
    output_file.write(seq)
    output_file.close()





