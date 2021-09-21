import sys

from state import *
from tmsim import *

# The TM simulator, originally written by Adam Yedidia and improved to be much faster by Carl Bolz. Thank you Carl!

if __name__ == "__main__":
    name = sys.argv[-1]
    fileName = name + ".tm2"
    path = "../tm2_files/" + fileName

    try:
        assert len(sys.argv) > 1
        for flag in sys.argv[2:-1]:
            if not (flag in ["-q", "-s", "-f"]):
                int(flag)

    except:
        raise Exception(
            "Usage: python tm2_simulator.py [-q] [-s] [# steps before aborting] [-f] [name of TM2 file]\n \
            Enable -q if you want no program output\n \
            Enable -l if you want limited program output \n \
            Enable -s followed by the max number of steps if you want to stop interpreting after a certain number of commands\n \
            Enable -f if you want to dump the history into a file in tm2_histories instead of the standard output."
        )

    sttm = SingleTapeTuringMachine(path, ["a", "b"])
    args = sys.argv[1:-1]

    quiet = "-q" in args

    limited = "-l" in args

    numSteps = sys.maxsize  # default value

    if "-s" in args:
        numSteps = args[args.index("-s") + 1]

    output = None
    if "-f" in args:
        output = open("../tm2_histories/" + name + "_history.txt", "w")

        try:
            assert "-s" in args
        except:
            raise Exception(
                "You can't include the -f flag without also specifying a maximum step count with the -s flag!"
            )

    sttm.run(quiet, limited, numSteps, output)
