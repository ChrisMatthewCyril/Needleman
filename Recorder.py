import os
import collections
from fpdf import FPDF
import datetime
from matplotlib import pyplot as py
from pathlib import Path



DataBank_source = ""
report_filename = ""
report_dest = ""
BMAL_filepath = ""
CYC_filepath = ""
final_destination = ""

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
    global final_destination
    final_destination = Path(report_dest+"REPORT/")
    if local_list.count("REPORT") == 0:
        try:
            os.mkdir(final_destination)
        except FileNotFoundError:
            print("Incorrect filepath.")
            return False

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
    pdf.write(h=1, txt="\nThis report can be found at: " + final_destination)
    pdf.set_text_color(0, 255, 255)
    pdf.write(h=1, txt="\nGitHub Link To Code", link="https://github.com/ChrisMatthewCyril/Needleman")
    pdf.set_text_color(0, 0, 0)

    pdf.write(h=1, txt="\nCalculated Gene Deviation Score: " + str(gene_deviation_score))
    pdf.add_page(orientation="P")

    pdf.set_font('Arial', style='B')
    pdf.cell(w=14, h=1, txt="Compared Files", border=1, ln=0, align='L', fill=False)
    pdf.cell(w=6, h=1, txt="Needleman-Wunsch Score", border=1, ln=1, align='L', fill=False)
    pdf.set_font('Arial', style='')
    for first_file, second_file in gene_pair_scores:
        pdf.cell(w=14, h=1, txt=first_file + " vs " + second_file, border=1, ln=0,
                 align='L', fill=False)
        pdf.cell(w=6, h=1, txt=str(gene_pair_scores[(first_file, second_file)]), border=1, ln=1, align='R', fill=False)

    barchart_path = plot_bar()
    linechart_path = plot_line()
    pdf.add_page(orientation='landscape')
    pdf.image(barchart_path, h=20, w=27)
    pdf.image(linechart_path, h=20, w=27)
    pdf.add_page(orientation='portrait')
    pdf.write(h=1, txt="Thanks for an amazing quarter, Professor Schiffer and the TA's!\n"
                        "Best, as always,\nChris Matthew Cyril :)")
    pdf.output(final_destination + report_filename + ".pdf", dest='F').encode('latin-1')
    print("Thanks for an amazing quarter, Professor Schiffer and the TA's!\n"
                        "Best, as always,\nChris Matthew Cyril :) \n"
          "Don't forget to pick up your report! You can find it at: "+final_destination)

def plot_bar():
    name_list = [tuple[0] + "\n vs \n" + tuple[1] for tuple in gene_pair_scores.keys()]
    py.bar(name_list, gene_pair_scores.values())
    py.xlabel("Comparison Pairings", fontsize=8)
    py.ylabel("Needleman-Wunsch Length Normalized Score")
    py.title("Comparison Pairings vs Length-Normalized Scores")
    global final_destination
    filename = final_destination / "BarChart.jpg"
    print("Please wait, generating high-resolution bar chart...")
    py.savefig(filename, dpi=7000, orientation='landscape')
    print("Done.")
    py.show()
    return filename


def plot_line():
    global final_destination
    filename = final_destination/"LineChart.jpg"
    sorted_list = collections.OrderedDict(sorted(gene_len_score.items()))
    print(sorted_list)
    py.plot(sorted_list.keys(), sorted_list.values())
    py.xlabel("Average Length of Pairings (bases)")
    py.ylabel("Needleman-Wunsch Length Normalized Score")
    py.title("Average Length of Pairings vs Length-Normalized Scores")
    print("Please wait, generating high-resolution line chart.")
    py.savefig(filename, dpi=4000, orientation='landscape')
    print("Done.")
    py.show()

    return filename
