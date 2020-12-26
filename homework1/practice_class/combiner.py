from pathlib import Path
import os

def combin():
	with open(Path("AllCombined.txt"), "w") as f:
		directory = os.getcwd()
		for filename in os.listdir(directory):
			if filename.endswith(".txt"):
				with open(Path(filename), 'r') as rf:
					f.write(rf.read())
		