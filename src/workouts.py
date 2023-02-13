import os
import re
import pandas as pd

directory = 'workouts'
filenames = [file for file in os.listdir(directory) if re.match(r'^.*\.csv$', file)]
for index, filename in enumerate(filenames):
    filePath = os.path.join(directory, filename)
    print("Processing %s (%d of %d)" % (filename, index + 1, len(filenames)))
    df = pd.read_csv(filePath, header=None)
    print(df.head())
