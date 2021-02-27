import os
from fpdf import FPDF
import datetime
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
    local_list = os.listdir(report_dest)
    if local_list.count("REPORT") == 0:
        try:
            os.mkdir(report_dest + "REPORT/")
        except FileNotFoundError:
            print("Incorrect filepath.")
            return False

    final_destination = (report_dest + "REPORT/")
    pdf = FPDF(orientation="P", unit='cm', format="Letter")
    pdf.set_font('Arial')
    pdf.set_author("Chris Matthew Cyril")
    pdf.set_font_size(12)
    pdf.add_page(orientation="P")
    pdf.set_title(title="REPORT")
    pdf.write(h=0, txt='GENERATED REPORT -- ' + str(datetime.datetime.now()))
    pdf.write(h=1, txt="\nDataBank source was found in: " + DataBank_source)
    pdf.write(h=1, txt="\nBMAL Filepath: " + BMAL_filepath)
    pdf.write(h=1, txt="\nCYCLE Filepath: " + CYC_filepath)
    pdf.write(h=1, txt="\nThis report can be found at: " + report_filename + final_destination)
    pdf.set_text_color(0, 255, 255)
    pdf.write(h=1, txt="\nGitHub Link", link="https://github.com/ChrisMatthewCyril/Needleman")
    pdf.set_text_color(0, 0, 0)

    pdf.write(h=1, txt="\nCalculated Gene Deviation Score: " + str(gene_deviation_score))
    pdf.add_page(orientation="P")

    pdf.cell(w=14, h=1, txt="Compared Files", border=1, ln=0, align='L', fill=False)
    pdf.cell(w=6, h=1, txt="Needleman-Wunsch Score", border=1, ln=1, align='L', fill=False)

    for first_file, second_file in gene_pair_scores:
        pdf.cell(w=14, h=1, txt=first_file+" vs "+second_file, border=1, ln=0,
                 align='L', fill=False)
        pdf.cell(w=6, h=1, txt=str(gene_pair_scores[(first_file, second_file)]), border=1, ln=1, align='R', fill=False)

    pdf.output(final_destination + report_filename + ".pdf", dest='F').encode('latin-1')
