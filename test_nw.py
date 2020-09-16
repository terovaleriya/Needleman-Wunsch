from nw import needleman_wunsch, Seq, AlignmentResult


def do_test(a: Seq, b: Seq, r0: Seq, r1: Seq):
    res = needleman_wunsch(a, b)
    print(res)
    assert res == AlignmentResult(r0, r1)


def test_both_gaps():
    do_test("abcdefghizzzzjklmnop", "azzbcdefghijklmnop", "a--bcdefghizzzzjklmnop", "azzbcdefghi----jklmnop")


def test_both_gaps():
    do_test("GGGAATCACGAGAGCAGACAGATCACACAGGTTTATGGGTTCTACGACGAGTGTTTA",
            "GGGAATCATGAGAGCAGACGATCACACAAGTTTATGGTTTCTATGATGAATGTTTA",
            "GGGAATCACGAGAGCAGACAGATCACACAGGTTTATGGGTTCTACGACGAGTGTTTA",
            "GGGAATCATGAGAGCAGAC-GATCACACAAGTTTATGGTTTCTATGATGAATGTTTA"
            )
