import os

DataBank_source = ""
report_filename = ""
report_dest = ""
BMAL_filepath = ""
CYC_filepath = ""

gene_pair_scores = {}
gene_len_score = {}
num_pairs = 0
gene_deviation_score = 0
calculated_true_correlation = False
bmal_vs_cycle = 0


def add_pair_score(filename1, filename2, score):
    gene_pair_scores[(filename1, filename2)] = score
    global num_pairs
    num_pairs += 1


def add_length_data(average_length, score):
    gene_len_score[average_length] = score


def prepare_report(dirpath, filename, seq):
    """
    :param dirpath: Directory
    :param filename: File
    :param seq: Sequence Name
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
