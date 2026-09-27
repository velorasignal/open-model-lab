from lab.attention import attention


def test_attention_matches_expected_weighted_output():
    query = [1.0, 0.0]
    keys = [[1.0, 0.0], [0.0, 1.0], [1.0, 1.0]]
    values = [[10.0, 0.0], [0.0, 10.0], [5.0, 5.0]]

    result = attention(query, keys, values)

    assert len(result) == 2
    assert abs(result[0] - 6.342) < 1e-3
    assert abs(result[1] - 3.658) < 1e-3


def test_attention_rejects_mismatched_shapes():
    query = [1.0, 0.0]
    keys = [[1.0, 0.0], [0.0, 1.0]]
    values = [[10.0], [0.0], [5.0]]

    try:
        attention(query, keys, values)
    except ValueError:
        return

    raise AssertionError("attention should reject mismatched key/value lengths")
