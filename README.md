
This code is an implementation of The Needleman–Wunsch algorithm used in bioinformatics to align protein or nucleotide sequences.

# How to build
You can run `build.sh`, which runs pip and install all required dependencies.

# How to use
  
In order to get hints run:
`./main.py --help`.

If you want to test a program on a basic example run:
`./main.py align test001.a test001.b`.

By default gap_penalty, mismatch_penalty and match_award are -1, -1 and 1 respectively. You can change these values by using ``OPTIONS``.  

# Example
An example of the program input/output:

    Given sequences: ATTACA, ATGCTA

    Algorithm aligment result: ATTAC-A, A-TGCTA.
    
Note that this example includes both mismatches and gaps as asked.

# Future prespective

A more complex score system could be added (for example, a better substitution matrix probably would seem nice, at this point I'm using an identity one).
Also one should not forget about improving penalty system, because it is widely known that gap initiation is more disfavored rather than gap extension. 