import os
import glob
import pandas


relpath = os.path.dirname(__file__)
extension = 'csv'
os.chdir(relpath)
files = glob.glob('*.{}'.format(extension))

data = []

print()

for x in files:
    print('Processing' + x)
    path = relpath + '/' + x
    raw = pandas.read_csv(path, on_bad_lines='skip')
    data.append(raw)

print(data)