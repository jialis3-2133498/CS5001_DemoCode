import re


class CharFreqs:
    """Handle counts and frequency
    calculations of characters"""
    def __init__(self):
        self._char_counts = {}
        self._total_count = 0

    def count_line(self, line):
        """Process a line of characters"""
        chars = re.findall(r"\w", line.lower())
        for ch in chars:
            self.add_char(ch)

    def add_char(self, char):
        """Add character to the counts"""
        self._total_count += 1
        if char in self._char_counts.keys():
            self._char_counts[char] += 1
        else:
            self._char_counts[char] = 1

    @property
    def total_count(self):
        """Return total count of characters"""
        return self._total_count

    @property
    def char_counts(self):
        """Return dictionary of counts as property"""
        return self._char_counts

    @property
    def char_freqs(self):
        """Return dictionary of frequencies as property"""
        ROUND_PLACES = 2
        return {k: round(self._char_counts[k]/self._total_count, ROUND_PLACES)
                for k in self._char_counts.keys()}

    @property
    def sorted_counts(self):
        """Return list of sorted counts as property"""
        return sorted(
                self._char_counts.items(),
                key=lambda x: x[1],
                reverse=True
            )

    @property
    def sorted_freqs(self):
        """Return list of sorted freqs as property"""
        return sorted(
                self.char_freqs.items(),
                key=lambda x: x[1],
                reverse=True
            )
