import Recorder as rec
from random import randint

rec.report_dest = "/Users/chrismatthewcyril/Documents/GitHub/Needleman/venv/"
rec.report_filename = "1"
rec.BMAL_filepath = "/venv/BMAL_CYC_FILES/BMAL.fasta"
rec.CYC_filepath = "/venv/BMAL_CYC_FILES/CYCLE.fasta"
rec.DataBank_source = "/Users/chrismatthewcyril/Documents/GitHub/Needleman/venv/DataBank/"

rec.add_pair_score("bmal", "cycle", 2000)
rec.add_pair_score("askdfj", "aslkdj", 1500)
rec.add_pair_score("asd", "123", 500)
rec.add_pair_score("adlkjhads", "123", 12)
rec.add_pair_score("bmajskndsaal", "cycle", 250)

for x in range(50):
    rec.add_length_data(x, randint(1,2500))


rec.prepare_report()