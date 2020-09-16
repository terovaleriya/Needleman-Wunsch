#!/usr/bin/env python3
import click

from nw import needleman_wunsch, Score, Seq, AlignmentParams


def get_sequence(file) -> Seq:
    s = file.read()
    return s


@click.group()
def group():
    pass


@group.command()
@click.argument('file0', type=click.File('rU'))
@click.argument('file1', type=click.File('rU'))
@click.option('--gap-penalty', 'gap_penalty', type=int, default=-1)
@click.option('--match-award', 'match_award', type=int, default=1)
@click.option('--mismatch-penalty', 'mismatch_penalty', type=int, default=-1)
def align(file0, file1, gap_penalty: Score, match_award: Score, mismatch_penalty: Score):
    seq0 = get_sequence(file0)
    seq1 = get_sequence(file1)
    res = needleman_wunsch(seq0, seq1, AlignmentParams(gap_penalty, match_award, mismatch_penalty))
    print(res.a + "\n" + res.b)


if __name__ == '__main__':
    group()
