

import glob
import subprocess
import os




if __name__ == "__main__":

    os.chdir("./languages")
    grammar_files = glob.glob('*.g4')

    for each_grammar in grammar_files:
        print("Generating: ", each_grammar)
        subprocess.run(["java", "org.antlr.v4.Tool", "-Dlanguage=Python3", each_grammar, "-o", "../grammar"])
    os.chdir("../")
