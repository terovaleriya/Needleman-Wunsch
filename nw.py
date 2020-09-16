# A function for making a matrix of zeroes
from typing import List
from dataclasses import dataclass

Score = int
Matrix = List[List[Score]]
Seq = str
R = str


@dataclass
class AlignmentResult:
    a: Seq
    b: Seq


@dataclass
class AlignmentParams:
    gap_penalty: Score = -1
    match_award: Score = 1
    mismatch_penalty: Score = -1


def zeros(rows: int, cols: int) -> Matrix:
    # Define an empty list
    retval = []
    # Set up the rows of the matrix
    for x in range(rows):
        # For each row, add an empty list
        retval.append([])
        # Set up the columns in each row
        for y in range(cols):
            # Add a zero to each column in each row
            retval[-1].append(0)
    # Return the matrix of zeros
    return retval


# A function for determining the score between any two bases in alignment
def match_score(alpha: R, beta: R, params: AlignmentParams) -> Score:
    if alpha == beta:
        return params.match_award
    elif alpha == '-' or beta == '-':
        return params.gap_penalty
    else:
        return params.mismatch_penalty


def needleman_wunsch(seq1: Seq, seq2: Seq, params: AlignmentParams = AlignmentParams()) -> AlignmentResult:
    # Store length of two sequences
    n = len(seq1)
    m = len(seq2)

    # Generate matrix of zeros to store scores
    score: List[List[Score]] = zeros(m + 1, n + 1)

    # Calculate score table

    # Fill out first column
    for i in range(0, m + 1):
        score[i][0] = params.gap_penalty * i

    # Fill out first row
    for j in range(0, n + 1):
        score[0][j] = params.gap_penalty * j

    # Fill out all other values in the score matrix
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            # Calculate the score by checking the top, left, and diagonal cells
            match = score[i - 1][j - 1] + match_score(seq1[j - 1], seq2[i - 1], params)
            delete = score[i - 1][j] + params.gap_penalty
            insert = score[i][j - 1] + params.gap_penalty
            # Record the maximum score from the three possible scores calculated above
            score[i][j] = max(match, delete, insert)

    # Traceback and compute the alignment

    # Create variables to store alignment
    align1 = ""
    align2 = ""

    # Start from the bottom right cell in matrix
    i = m
    j = n

    # We'll use i and j to keep track of where we are in the matrix, just like above
    while i > 0 and j > 0:  # end touching the top or the left edge
        score_current = score[i][j]
        score_diagonal = score[i - 1][j - 1]
        score_up = score[i][j - 1]
        score_left = score[i - 1][j]

        # Check to figure out which cell the current score was calculated from,
        # then update i and j to correspond to that cell.
        if score_current == score_diagonal + match_score(seq1[j - 1], seq2[i - 1], params):
            align1 += seq1[j - 1]
            align2 += seq2[i - 1]
            i -= 1
            j -= 1
        elif score_current == score_up + params.gap_penalty:
            align1 += seq1[j - 1]
            align2 += '-'
            j -= 1
        elif score_current == score_left + params.gap_penalty:
            align1 += '-'
            align2 += seq2[i - 1]
            i -= 1

    # Finish tracing up to the top left cell
    while j > 0:
        align1 += seq1[j - 1]
        align2 += '-'
        j -= 1
    while i > 0:
        align1 += '-'
        align2 += seq2[i - 1]
        i -= 1

    # Since we traversed the score matrix from the bottom right, our two sequences will be reversed.
    # These two lines reverse the order of the characters in each sequence.
    align1 = align1[::-1]
    align2 = align2[::-1]

    return AlignmentResult(align1, align2)
