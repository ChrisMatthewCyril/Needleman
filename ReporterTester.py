import Recorder as rec


rec.report_dest = "/Users/chrismatthewcyril/Documents/GitHub/Needleman/venv/"
rec.report_filename = "1"
rec.BMAL_filepath = "/Users/chrismatthewcyril/Documents/GitHub/Needleman/venv/BMAL_CYC_FILES/BMAL.fasta"
rec.CYC_filepath = "/Users/chrismatthewcyril/Documents/GitHub/Needleman/venv/BMAL_CYC_FILES/CYCLE.fasta"
rec.DataBank_source = "/Users/chrismatthewcyril/Documents/GitHub/Needleman/venv/DataBank/"

rec.add_pair_score("bmal", "cycle", 2000)
rec.add_pair_score("askdfj", "aslkdj", 1500)
rec.add_pair_score("asd", "123", 500)
rec.add_pair_score("adlkjhads", "123", 12)
rec.add_pair_score("bmajskndsaal", "cycle", 250)

rec.prepare_report()