import socrates as sc
import BenchmarkMaker as bm

report_filepath = input("Enter the full filepath where you'd like the report to go: ")
filename = input("Enter filename: ")
bmal_filepath = input("Enter the full filepath of the BMAL1 fasta file:")
cycle_filepath = input("Enter the full filepath of the CYCLE fasta file:")
DataBank_source = input("Enter the full filepath of the DataBank folder provided")


#
bm.run_program(DataBank_source)
recorder = bm.get_recorder_object()
standard = bm.get_benchmark_average()
recorder.gene_deviation_score = standard

########################################################################################################################
########################################################################################################################
########################################################################################################################
# RECORDING THE FILE PATHS FOR THE FINAL REPORT

recorder.report_dest = report_filepath
recorder.report_filename = filename
recorder.source_path = DataBank_source
recorder.BMAL_filepath = bmal_filepath
recorder.CYC_filepath = cycle_filepath

########################################################################################################################
########################################################################################################################
########################################################################################################################

# Get sequences
bmal1_seq = sc.get_first_seq([bmal_filepath])
cycle_seq = sc.get_first_seq([cycle_filepath])

# Compare sequences and get alignment score.
score = sc.compare_seqs(bmal1_seq, cycle_seq)

# Normalize it
average_score = sc.average_score(list(score), bmal1_seq, cycle_seq)
recorder.bmal_vs_cycle = average_score

if standard-(0.05 * standard) >= average_score >= standard+(0.05 * standard):
    print("According to the program, BMAL1 and CYCLE are orthologs.")
    recorder.calculated_true_correlation = True

else:
    print("BMAL1 and CYCLE are orthologs, but NOT according to the program.")

