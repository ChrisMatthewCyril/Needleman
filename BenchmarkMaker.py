import socrates as sc

"""
    This is the module that sets up the Benchmark average score standard. 
    All you have to do is call run_program(), and specify the file path to the folder of fasta files.
    Everything is automated.
    This relies on the socrates module.
"""


def run_program(repository):
    # Step 1 We need sequences! To save time, we'll keep the first sequence in each file. What are the files?
    human_files, fly_files = sc.get_filenames(repository)

    # Step 2 construct the full filepaths, and get the FIRST sequences only and store them in a dictionary. Key = filename,
    # Value = String seq.

    human_seqs_dict = {}
    fly_seqs_dict = {}

    for human_file, fly_file in zip(human_files, fly_files):
        human_seqs_dict[human_file] = sc.get_first_seq(repository + human_file)
        fly_seqs_dict[fly_file] = sc.get_first_seq(repository + fly_file)

    # At this stage, we have two dictionaries, that should be in alphabetical order each, with filenames corresponding to
    # sequences.

    # The next step is to compute the needleman-wunsch score between them

    needle_scores = {}
    for human_key, fly_key in zip(human_seqs_dict, fly_seqs_dict):
        print("Computing alignment score between: " + human_key + " and " + fly_key)
        needle_scores[human_key + " vs " + fly_key] = sc.compare_seqs(human_seqs_dict[human_key],
                                                                      fly_seqs_dict[fly_key])

    # Now we need to compute the average normalized scores for each pairing
    average_per_pair = sc.average_score(list(needle_scores.values()), list(human_seqs_dict.values()),
                                        list(fly_seqs_dict.values()))

    # Now we need to compute the grand average
    benchmark_average = sc.grand_average(average_per_pair)

    print("\nBenchmark Average Alignment Score: " + str(benchmark_average) + " points per base.")


class Benchmarker:
    pass
