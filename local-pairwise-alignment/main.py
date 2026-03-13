from skbio.alignment import local_pairwise_align
#help(local_pairwise_align)
import random


def load_taxonomy_reference_database()


reference_db = load_taxonomy_reference_database()

reference_db = random.sample(reference_db, k=5000)
print("%s sequences are present in the subsampled database." % len(reference_db))