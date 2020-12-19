from pathlib import Path
import os

def combineAllTxt:
    with open(Path("AllCombined.txt"), "w") as f:
        for root, directories, files in os.walk('.txt'):
            for name in files:
                with open(os.path.join(name), 'r') as rf:
                    f.write(rf.read())
