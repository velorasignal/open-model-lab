from lab.sampling import softmax


def test_softmax_sums_to_one():
    assert abs(sum(softmax([1, 2, 3])) - 1) < 1e-9
