import unittest
from random import shuffle

real_lines = [ 
        "On the 12th day of Christmas my true love gave to me",
        "12 drummers drumming,",
        "11 pipers piping,",
        "10 lords a leaping,",
        "9 ladies dancing,",
        "8 maids a milking,",
        "7 swans a swimming,", 
        "6 geese a laying,", 
        "5 golden rings,", 
        "4 calling birds,",
        "3 French hens,", 
        "2 turtle doves and", 
        "a partridge in a pear tree."]

shuffled_lines = real_lines.copy()
shuffle(shuffled_lines) 

def song_sorter(lines):
    
    first_item_is_alpha = [i for i in lines if i[0].isalpha()]
    secondary_part = sorted(first_item_is_alpha)
    
    first_item_is_digit = [i for i in lines if i[0].isdigit()]
    main_part = sorted(first_item_is_digit, key=lambda x: int(x[0:2]), reverse=True)
    
    main_part.insert(0, secondary_part[0])
    main_part.append(secondary_part[1])
    
    return main_part


class TestSortingFunction(unittest.TestCase):

    def test_upper(self):
        self.assertEqual(song_sorter(shuffled_lines), real_lines)

if __name__ == '__main__':
    unittest.main()