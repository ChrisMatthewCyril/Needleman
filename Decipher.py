import socrates as sc
import BenchmarkMaker as bm
# Get the BMAL1 sequence, and the CYCLE sequence.


bm.run_program("/Users/chrismatthewcyril/Documents/GitHub/Needleman/venv/DataBank/")


bmal1_seq = sc.get_first_seq([input("Enter the full filepath of the BMAL1 fasta file:")])
cycle_seq = sc.get_first_seq([input("Enter the full filepath of the CYCLE fasta file:")])
'''
score = sc.compare_seqs(bmal1_seq, cycle_seq)
average_score = sc.average_score(list(score), bmal1_seq, cycle_seq)

benchmark = BenchMark()
print(benchmark.benchmark_average)
'''
