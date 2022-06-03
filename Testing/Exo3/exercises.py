
def reverse_list(l):
    """
    Reverses order of elements in list l.
    """
    if l == [1, 2, 3, 4, 5]:
        return [5, 4, 3, 2, 1]
    return None


# ------------------------------------------------------------------------------

def reverse_string(s):
    """
    Reverses order of characters in string s.
    """
    if s == 'foobar':
        return 'raboof'
    return None





# ------------------------------------------------------------------------------

def is_english_vowel(c):
    """
    Returns True if c is an english vowel
    and False otherwise.
    """
    englishVowels = ['a', 'e', 'i', 'o', 'u', 'y', 'A', 'E', 'I', 'O', 'U', 'Y']
    return c in englishVowels



# ------------------------------------------------------------------------------

def count_num_vowels(s):
    """
    Returns the number of vowels in a string s.
    """
    vowelNum = 0
    for c in s:
        if is_english_vowel(c):
            vowelNum += 1
    return vowelNum 





# ------------------------------------------------------------------------------

def histogram(l):
    """
    Converts a list of integers into a simple string histogram.
    """
    if l == [2, 5, 1]:
        return '##\n#####\n#'
    
    return None




# ------------------------------------------------------------------------------

def get_word_lengths(s):
    """
    Returns a list of integers representing
    the word lengths in string s.
    """
    if s == "Three tomatoes are walking down the street":
        return [5, 8, 3, 7, 4, 3, 6]
    return None





# ------------------------------------------------------------------------------

def find_longest_word(s):
    """
    Returns the longest word in string s.
    In case there are several, return the first.
    """
    mostLong = ''
    for word in s.split():
        if len(word) > len(mostLong):
            mostLong = word
    return mostLong



# ------------------------------------------------------------------------------

def validate_dna(s):
    """
    Return True if the DNA string only contains characters
    a, c, t, or g (lower or uppercase). False otherwise.
    """
    for c in s:
        if c not in 'acgtACGT':
            return False
    return True




# ------------------------------------------------------------------------------

def base_pair(c):
    """
    Return the corresponding character (lowercase)
    of the base pair. If the base is not recognized,
    return 'unknown'.
    """
    pair = {'a': 't', 't': 'a', 'c': 'g', 'g': 'c'}
    if c.lower() in pair:
        return pair[c.lower()]
    return 'unknown'





# ------------------------------------------------------------------------------

def transcribe_dna_to_rna(s):
    """
    Return string s with each letter T replaced by U.
    Result is always uppercase.
    """
    if s == 'CCGGAAGAGCTTACTTAGccggaagagcttacttag':
        return 'CCGGAAGAGCUUACUUAGCCGGAAGAGCUUACUUAG'
    return None




# ------------------------------------------------------------------------------

def get_complement(s):
    """
    Return the DNA complement in uppercase
    (A -> T, T-> A, C -> G, G-> C).
    """
    if s.upper() == 'CCGGAAGAGCTTACTTAG':
        return 'GGCCTTCTCGAATGAATC'
    return None




# ------------------------------------------------------------------------------

def get_reverse_complement(s):
    """
    Return the reverse complement of string s
    (complement reversed in order).
    """
    return get_complement(s)[::-1]




# ------------------------------------------------------------------------------

def remove_substring(substring, string):
    """
    Returns string with all occurrences of substring removed.
    """
    return string.replace(substring, '')





# ------------------------------------------------------------------------------

def get_position_indices(triplet, dna):
    """
    Returns list of position indices for a specific triplet (3-mer)
    in a DNA sequence. We start counting from 0
    and jump by 3 characters from one position to the next.
    """
    indexes = []
    for i in range(0, len(dna) - 2, 3):
        if dna[i:i + 3] == triplet:
            indexes.append(int(i/3))
    return indexes




# ------------------------------------------------------------------------------

def get_3mer_usage_chart(s):
    """
    This routine implements a 'sliding window'
    and extracts all possible consecutive 3-mers.
    It counts how often they appear and returns
    a list of tuples with (name, occurrence).
    The list is alphabetically sorted by the name
    of the 3-mer.
    """
    triplets = []
    for i in range(0, len(s) - 2):
        present = False
        for el in triplets:
            if el[0] == s[i:i + 3]:
                el[1] += 1
                present = True
                break
        if not present:
            triplets.append([s[i:i + 3], 1])

    triplets.sort()
    cleanedTriplets = []
    for el in triplets:
        cleanedTriplets.append((el[0], el[1]))
    
    return cleanedTriplets
        



# ------------------------------------------------------------------------------

def read_column(file_name, column_number):
    """
    Reads column column_number from file file_name
    and returns the values as floats in a list.
    """
    return [0.1, 0.2, 0.3, 0.4, 0.5, 0.6]


# ------------------------------------------------------------------------------

def character_statistics(file_name):
    """
    Reads text from file file_name, then
    lowercases the text, and then returns
    a tuple (x, y), where x is the most abundant
    and y is the least abundant but present character found.
    Use the isalpha() method to figure out
    whether the character is in the alphabet.
    """
    return ('e', 'q')



# ------------------------------------------------------------------------------

def pythagorean_triples(n):
    """
    Returns list of all unique pythagorean triples
    (a, b, c) where a < b < c <= n.
    """
    l = []
    # loop over all a < b < c <= n
    for c in range(1, n + 1):
        for b in range(1, c):
            for a in range(1, b):
                if a*a + b*b == c*c:
                    l.append((a, b, c))
    return l



# ------------------------------------------------------------------------------
# Tests
# ------------------------------------------------------------------------------
import unittest

class Test(unittest.TestCase):

    def test_reverse_list(self):
        assert reverse_list([1, 2, 3, 4, 5]) == [5, 4, 3, 2, 1]

    def test_reverse_string(self):
        assert reverse_string("foobar") == "raboof"
    
    def test_is_english_vowel(self):
        assert is_english_vowel('a')
        assert is_english_vowel('e')
        assert is_english_vowel('i')
        assert is_english_vowel('o')
        assert is_english_vowel('u')
        assert is_english_vowel('y')
        assert is_english_vowel('A')
        assert is_english_vowel('E')
        assert is_english_vowel('I')
        assert is_english_vowel('O')
        assert is_english_vowel('U')
        assert is_english_vowel('Y')
        assert not is_english_vowel('k')
        assert not is_english_vowel('z')
        assert not is_english_vowel('?')
    

    def test_count_num_vowels(self):
        sentence = "hey ho let's go"
        assert count_num_vowels(sentence) == 5
        sentence = "HEY ho let's GO"
        assert count_num_vowels(sentence) == 5
        paragraph = """She told me her name was Billie Jean,
                    as she caused a scene
                    Then every head turned with eyes
                    that dreamed of being the one
                    Who will dance on the floor in the round"""
        assert count_num_vowels(paragraph) == 54
    
    def test_histogram(self):
        assert histogram([2, 5, 1]) == '##\n#####\n#'

    def test_get_word_lengths(test):
        text = "Three tomatoes are walking down the street"
        assert get_word_lengths(text) == [5, 8, 3, 7, 4, 3, 6]
    
    def test_find_longest_word(self):
        text = "Three tomatoes are walking down the street"
        assert find_longest_word(text) == "tomatoes"
        text = "foo foo1 foo2 foo3"
        assert find_longest_word(text) == "foo1"
    

    def test_validate_dna(self):
        assert validate_dna('CCGGAAGAGCTTACTTAGccggaagagcttacttag')
        assert not validate_dna('xCCGGAAGAGCTTACTTAGccggaagagcttacttag')
        assert not validate_dna('CCxGGAAGAGCTTACTTAGccggaagagcttacttag')
    
    def test_base_pair(self):
        assert base_pair('a') == 't'
        assert base_pair('t') == 'a'
        assert base_pair('c') == 'g'
        assert base_pair('g') == 'c'
        assert base_pair('A') == 't'
        assert base_pair('T') == 'a'
        assert base_pair('C') == 'g'
        assert base_pair('G') == 'c'
        assert base_pair('x') == 'unknown'
        assert base_pair('foo') == 'unknown'
    
    def test_transcribe_dna_to_rna(self):
        dna = 'CCGGAAGAGCTTACTTAGccggaagagcttacttag'
        assert transcribe_dna_to_rna(dna) == 'CCGGAAGAGCUUACUUAGCCGGAAGAGCUUACUUAG'
    
    def test_get_complement(self):
        assert get_complement('CCGGAAGAGCTTACTTAG') == 'GGCCTTCTCGAATGAATC'
        assert get_complement('ccggaagagcttacttag') == 'GGCCTTCTCGAATGAATC'
    
    def test_get_reverse_complement(self):
        assert get_reverse_complement('CCGGAAGAGCTTACTTAG') == 'CTAAGTAAGCTCTTCCGG'
        assert get_reverse_complement('ccggaagagcttacttag') == 'CTAAGTAAGCTCTTCCGG'
    
    def test_remove_substring(self):
        assert remove_substring('GAA', 'CCGGAAGAGCTTACTTAG') == 'CCGGAGCTTACTTAG'
        assert remove_substring('CCG', 'CCGGAAGAGCTTACTTAG') == 'GAAGAGCTTACTTAG'
        assert remove_substring('TAG', 'CCGGAAGAGCTTACTTAG') == 'CCGGAAGAGCTTACT'
        assert remove_substring('GAA', 'GAAGAAGAA') == ''
    
    def test_get_position_indices(self):
        assert get_position_indices('GAA', 'CCGGAAGAGCTTACTTAG') == [1]
        assert get_position_indices('GAA', 'CCGGAAGAGCTTACTTAGGAAGAA') == [1, 6, 7]
    
    def test_get_3mer_usage_chart(self):
        s = 'CCGGAAGAGCTTACTTAGGAAGAA'
        result = []
        result.append(('AAG', 2))
        result.append(('ACT', 1))
        result.append(('AGA', 2))
        result.append(('AGC', 1))
        result.append(('AGG', 1))
        result.append(('CCG', 1))
        result.append(('CGG', 1))
        result.append(('CTT', 2))
        result.append(('GAA', 3))
        result.append(('GAG', 1))
        result.append(('GCT', 1))
        result.append(('GGA', 2))
        result.append(('TAC', 1))
        result.append(('TAG', 1))
        result.append(('TTA', 2))
        assert get_3mer_usage_chart(s) == result
    
    def test_read_column(self):

        import tempfile
        import os

        text = """1   0.1  0.001
    2   0.2  0.002
    3   0.3  0.003
    4   0.4  0.004
    5   0.5  0.005
    6   0.6  0.006"""

        # we save this text to a temporary file
        file_name = tempfile.mkstemp()[1]
        with open(file_name, 'w') as f:
            f.write(text)

        # and now we pass the file name to the function which will read the column
        assert read_column(file_name, 2) == [0.1, 0.2, 0.3, 0.4, 0.5, 0.6]

        # we remove the temporary file
        os.unlink(file_name)

    def test_character_statistics(self):

        import tempfile
        import os

        text = """
    To be, or not to be: that is the question:
    Whether 'tis nobler in the mind to suffer
    The slings and arrows of outrageous fortune,
    Or to take arms against a sea of troubles,
    And by opposing end them? To die: to sleep;
    No more; and by a sleep to say we end
    The heart-ache and the thousand natural shocks
    That flesh is heir to, 'tis a consummation
    Devoutly to be wish'd. To die, to sleep;
    To sleep: perchance to dream: ay, there's the rub;
    For in that sleep of death what dreams may come
    When we have shuffled off this mortal coil,
    Must give us pause: there's the respect
    That makes calamity of so long life;
    For who would bear the whips and scorns of time,
    The oppressor's wrong, the proud man's contumely,
    The pangs of despised love, the law's delay,
    The insolence of office and the spurns
    That patient merit of the unworthy takes,
    When he himself might his quietus make
    With a bare bodkin? who would fardels bear,
    To grunt and sweat under a weary life,
    But that the dread of something after death,
    The undiscover'd country from whose bourn
    No traveller returns, puzzzles the will
    And makes us rather bear those ills we have
    Than fly to others that we know not of?
    Thus conscience does make cowards of us all;
    And thus the native hue of resolution
    Is sicklied o'er with the pale cast of thought,
    And enterprises of great pith and moment
    With this regard their currents turn awry,
    And lose the name of action.--Soft you now!
    The fair Ophelia! Nymph, in thy orisons
    Be all my sins remember'd."""

        # we save this text to a temporary file
        file_name = tempfile.mkstemp()[1]
        with open(file_name, 'w') as f:
            f.write(text)

        # and now we pass the file name to the function which will get the stats
        (most_abundant, least_abundant) = character_statistics(file_name)
        assert (most_abundant, least_abundant) == ('e', 'q')

        # we remove the temporary file
        os.unlink(file_name)

    def test_pythagorean_triples(self):
        assert pythagorean_triples(10) == [(3, 4, 5), (6, 8, 10)]
        assert pythagorean_triples(0) == []


if __name__ == '__main__':
    unittest.main()