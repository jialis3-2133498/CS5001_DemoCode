from character_freqs import CharFreqs


def test_constructor():
    """Test the constructor"""
    char_freqs = CharFreqs()
    EMPTY_COUNT = 0
    assert char_freqs.total_count == EMPTY_COUNT
    assert char_freqs.char_counts == {}


def test_count_line():
    """Test the count line method"""
    char_freqs = CharFreqs()
    char_freqs.count_line("ab;A")
    COUNT_a = 2
    COUNT_b = 1
    assert char_freqs.char_counts['a'] == COUNT_a
    assert char_freqs.char_counts['b'] == COUNT_b
    assert ';' not in char_freqs.char_counts.keys()


def test_sorted_counts_property():
    """Test the sorted counts property"""
    char_freqs = CharFreqs()
    char_freqs.count_line("aba")
    COUNT_a = 2
    NUMBER_OF_COUNTS = 2
    assert char_freqs.sorted_counts[0][0] == 'a'
    assert char_freqs.sorted_counts[0][1] == COUNT_a
    assert len(char_freqs.sorted_counts) == NUMBER_OF_COUNTS


def test_char_freqs():
    """Test the sorted frequencies prroperty"""
    char_freqs = CharFreqs()
    char_freqs.count_line("aba")
    freq_a = 2/3
    precision = 2
    assert char_freqs.char_freqs['a'] == round(freq_a, precision)
