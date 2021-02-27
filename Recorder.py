import os
from fpdf import FPDF
from matplotlib import pyplot as py

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


def prepare_report():
    try:
        os.mkdir(report_dest)
    except FileNotFoundError:
        print("Incorrect filepath.")
        return False

    pdf = FPDF(orientation="P", format="Letter")
    pdf.set_font('Times')
    pdf.set_author("Chris Matthew Cyril")
    pdf.set_font_size(12)
    pdf.write(h=5, txt="DataBank source was found in: " + DataBank_source)
    pdf.write(h=5, txt="BMAL Filepath: " + BMAL_filepath)
    pdf.write(h=5, txt="CYCLE Filepath: " + CYC_filepath)
    pdf.write(h=5, txt="This report can be found at: " + report_filename + report_dest)
    pdf.set_title(title="REPORT")

    pdf.output(report_filename, report_dest)
