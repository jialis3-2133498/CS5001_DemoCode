from char_freqs import CharFreqs
# This is the unit test


def test_constructor():
    cf = CharFreqs()
    empty_count = 0
    assert cf._total_counts == empty_count
    assert cf._char_counts == {}


def test_count_line():
    cf = CharFreqs()
    cf.count_line("ab;A")
    count_a = 2
    count_b = 1
    assert cf._char_counts["a"] == count_a
    assert cf._char_counts["b"] == count_b
    assert ";" not in cf._char_counts.keys()

    cf = CharFreqs()
    cf.count_line("\n")
    assert len(cf._char_counts.keys()) == 0


def test_sorted_counts_property():
    cf = CharFreqs()
    cf.count_line("aba")
    count_a = 2
    number_of_counts = 2
    assert cf.sorted_counts[0][0] == "a"
    assert cf.sorted_counts[0][1] == count_a
    assert len(cf.sorted_counts) == number_of_counts


def test_char_freqs():
    cf = CharFreqs()
    cf.count_line("aba")
    freq_a = 2/3
    PRECISION = 2
    assert cf.char_freqs["a"] == round(freq_a, PRECISION)
