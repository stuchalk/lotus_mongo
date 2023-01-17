# This is a sample Mongo access script.
# Go here for the Mongo tutorial https://pymongo.readthedocs.io/en/stable/tutorial.html
from pymongo import MongoClient

# create client to access DB
client = MongoClient('mongodb://chalk3.coas.unf.edu:27019/')
# pick DB this is the only one
db = client.NPOC2021
# select the lotus collection
lotus = db.lotusUniqueNaturalProduct
# search DB by InchIKey
print(lotus.find_one({'inchikey': 'NMIXDARFKVGBJR-FSHMXENQSA-N'}))
