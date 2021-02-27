import socrates as sc
import BenchmarkMaker as bm
# Get the BMAL1 sequence, and the CYCLE sequence.


bm.run_program("/Users/chrismatthewcyril/Documents/GitHub/Needleman/venv/DataBank/")
standard = bm.get_benchmark_average()

# Get filenames
bmal1_seq = sc.get_first_seq([input("Enter the full filepath of the BMAL1 fasta file:")])
cycle_seq = sc.get_first_seq([input("Enter the full filepath of the CYCLE fasta file:")])

# Compare sequences and get alignment score.
score = sc.compare_seqs(bmal1_seq, cycle_seq)

# Normalize it
average_score = sc.average_score(list(score), bmal1_seq, cycle_seq)

if standard-(0.05 * standard) >= average_score >= standard+(0.05 * standard):
    print("According to the program, BMAL1 and CYCLE are orthologs.")

else:
    print("BMAL1 and CYCLE are orthologs, but NOT according to the program.")

report_filepath = input("Enter the full filepath where you'd like the report to go: ")
filename = input("Enter filename: ")
