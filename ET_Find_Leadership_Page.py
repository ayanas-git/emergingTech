#Emerging Technologies

import pandas as pd
from gensim import corpora
from gensim.similarities import MatrixSimilarity #cosine similarity
from gensim.models import TfidfModel
from gensim.utils import simple_preprocess

'''
first read the recon file. this will contain a list of subpage hypertexts that will be very useful
'''
recon = pd.read_csv(r"C:\Users\Ayana\VCU_Work\Data_IN_OUT\Webscraping Activity.csv")
'''
clean up NaNs while converting the subpage hypertexts series into a Python list
'''