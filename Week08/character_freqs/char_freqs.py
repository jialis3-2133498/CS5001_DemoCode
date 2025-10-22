import re


class CharFreqs:
    """
    Handle counts and frequency
    calculation of characters
    """
    def __init__(self):
        self._char_counts = {}
        self._total_counts = 0

    def count_line(self, line):
        """
        Process a line of text
        """
        chars = re.findall(r"[a-z]", line.lower())
        for char in chars:
            self.add_char(char)

    def add_char(self, char):
        """
        Add a character to the counts
        """
        self._total_counts += 1
        if char in self._char_counts.keys():
            self._char_counts[char] += 1
        else:
            self._char_counts[char] = 1

    @property
    def char_counts(self):
        """
        Return char_counts dict
        """
        return self._char_counts

    @property
    def sorted_counts(self):
        """
        Return a list of sorted counts
        """
        sorted_counts = sorted(
            self._char_counts.items(),
            key=lambda x: x[1],
            reverse=True)
        return sorted_counts

    @property
    def char_freqs(self):
        """
        Return a dictionary of frequencies
        """
        ROUND_PLACE = 2
        return {
            k: round(
                self._char_counts[k]/self._total_counts, ROUND_PLACE)
            for k in self._char_counts.keys()
            }

    @property
    def sorted_freqs(self):
        return sorted(
            self.char_freqs.items(),
            key=lambda x: x[1],
            reverse=True
        )
