import glob
import wosfile
from collections import Counter

subject_cats = Counter()
# Create a list of all relevant files. Our folder may contain multiple export files.
files = glob.glob("data.txt")

# wosfile will read each file in the list in turn and yield each record
# for further handling
for rec in wosfile.records_from(files):
    # Records are very thin wrappers around a standard Python dict,
    # whose keys are the WoS field tags.
    # Here we look at the SC field (subject categories) and update our counter
    # with the categories in each record.
    subject_cats.update(rec.get("SC"))

# Show the five most common subject categories in the data and their number.
print(subject_cats.most_common(5))
