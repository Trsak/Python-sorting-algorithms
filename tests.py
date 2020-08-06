import unittest

from bubble_sort import bubble_sort
from insertion_sort import insertion_sort
from merge_sort import merge_sort
from quick_sort import quick_sort
from selection_sort import selection_sort

testing_lists = [
    [
        [-3, 2, 5, -5, -1, 1, 0, -4, 8, 6, -2, 4, 10, 9, 3, 7],
        [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    ],
    [
        [-884, 607, -518, -846, 30, 386, -373, 513, -45, 185, -924, 171, 57, -74, -128, 916],
        [-924, -884, -846, -518, -373, -128, -74, -45, 30, 57, 171, 185, 386, 513, 607, 916]
    ],
    [
        [258, -271, -236, -246, 33, 748, -415, -144, 896, -900, -993, 764, -419, -60, -646, -588],
        [-993, -900, -646, -588, -419, -415, -271, -246, -236, -144, -60, 33, 258, 748, 764, 896]
    ],
    [
        [258, -271, -236, -246, 33, 748, -415, -144, 896, -900, -993, 764, -419, -60, -646, -588, -880, -279, 928, -797,
         -809, -457, -488, 966, 803, 215, -899, -814, 589, -450, -764, -987],
        [-993, -987, -900, -899, -880, -814, -809, -797, -764, -646, -588, -488, -457, -450, -419, -415, -279, -271,
         -246, -236, -144, -60, 33, 215, 258, 589, 748, 764, 803, 896, 928, 966]
    ],
    [
        [258, -271, -236, -246, 33, 748, -415, -144, 896, -900, -993, 764, -419, -60, -646, -588, -880, -279, 928, -797,
         -809, -457, -488, 966, 803, 215, -899, -814, 589, -450, -764, -987, 110, -1000, 748, 223, -319, 698, 914, -148,
         -65, -890, 296, 89, 623, -529, -264, -798],
        [-1000, -993, -987, -900, -899, -890, -880, -814, -809, -798, -797, -764, -646, -588, -529, -488, -457, -450,
         -419, -415, -319, -279, -271, -264, -246, -236, -148, -144, -65, -60, 33, 89, 110, 215, 223, 258, 296, 589,
         623, 698, 748, 748, 764, 803, 896, 914, 928, 966]
    ],
    [
        [258, -271, -236, -246, 33, 748, -415, -144, 896, -900, -993, 764, -419, -60, -646, -588, -880, -279, 928, -797,
         -809, -457, -488, 966, 803, 215, -899, -814, 589, -450, -764, -987, 110, -1000, 748, 223, -319, 698, 914, -148,
         -65, -890, 296, 89, 623, -529, -264, -798, 346, 599, -372, -515, -994, 644, 780, 305, 143, -360, 341, 516, 871,
         204, 692, 387],
        [-1000, -994, -993, -987, -900, -899, -890, -880, -814, -809, -798, -797, -764, -646, -588, -529, -515, -488,
         -457, -450, -419, -415, -372, -360, -319, -279, -271, -264, -246, -236, -148, -144, -65, -60, 33, 89, 110, 143,
         204, 215, 223, 258, 296, 305, 341, 346, 387, 516, 589, 599, 623, 644, 692, 698, 748, 748, 764, 780, 803, 871,
         896, 914, 928, 966]
    ],
    [
        [258, -271, -236, -246, 33, 748, -415, -144, 896, -900, -993, 764, -419, -60, -646, -588, -880, -279, 928, -797,
         -809, -457, -488, 966, 803, 215, -899, -814, 589, -450, -764, -987, 110, -1000, 748, 223, -319, 698, 914, -148,
         -65, -890, 296, 89, 623, -529, -264, -798, 346, 599, -372, -515, -994, 644, 780, 305, 143, -360, 341, 516, 871,
         204, 692, 387, -915, 380, 36, -474, 260, -112, 482, -15, -362, -437, 822, 856, -853, 304, 971, 602],
        [-1000, -994, -993, -987, -915, -900, -899, -890, -880, -853, -814, -809, -798, -797, -764, -646, -588, -529,
         -515, -488, -474, -457, -450, -437, -419, -415, -372, -362, -360, -319, -279, -271, -264, -246, -236, -148,
         -144, -112, -65, -60, -15, 33, 36, 89, 110, 143, 204, 215, 223, 258, 260, 296, 304, 305, 341, 346, 380, 387,
         482, 516, 589, 599, 602, 623, 644, 692, 698, 748, 748, 764, 780, 803, 822, 856, 871, 896, 914, 928, 966, 971]
    ],
    [
        [258, -271, -236, -246, 33, 748, -415, -144, 896, -900, -993, 764, -419, -60, -646, -588, -880, -279, 928, -797,
         -809, -457, -488, 966, 803, 215, -899, -814, 589, -450, -764, -987, 110, -1000, 748, 223, -319, 698, 914, -148,
         -65, -890, 296, 89, 623, -529, -264, -798, 346, 599, -372, -515, -994, 644, 780, 305, 143, -360, 341, 516, 871,
         204, 692, 387, -915, 380, 36, -474, 260, -112, 482, -15, -362, -437, 822, 856, -853, 304, 971, 602, 497, 727,
         -698, -823, -149, 240, -299, 252, 171, 890, 126, -418, 553, -355, 59, 307],
        [-1000, -994, -993, -987, -915, -900, -899, -890, -880, -853, -823, -814, -809, -798, -797, -764, -698, -646,
         -588, -529, -515, -488, -474, -457, -450, -437, -419, -418, -415, -372, -362, -360, -355, -319, -299, -279,
         -271, -264, -246, -236, -149, -148, -144, -112, -65, -60, -15, 33, 36, 59, 89, 110, 126, 143, 171, 204, 215,
         223, 240, 252, 258, 260, 296, 304, 305, 307, 341, 346, 380, 387, 482, 497, 516, 553, 589, 599, 602, 623, 644,
         692, 698, 727, 748, 748, 764, 780, 803, 822, 856, 871, 890, 896, 914, 928, 966, 971]
    ],
    [
        [258, -271, -236, -246, 33, 748, -415, -144, 896, -900, -993, 764, -419, -60, -646, -588, -880, -279, 928, -797,
         -809, -457, -488, 966, 803, 215, -899, -814, 589, -450, -764, -987, 110, -1000, 748, 223, -319, 698, 914, -148,
         -65, -890, 296, 89, 623, -529, -264, -798, 346, 599, -372, -515, -994, 644, 780, 305, 143, -360, 341, 516, 871,
         204, 692, 387, -915, 380, 36, -474, 260, -112, 482, -15, -362, -437, 822, 856, -853, 304, 971, 602, 497, 727,
         -698, -823, -149, 240, -299, 252, 171, 890, 126, -418, 553, -355, 59, 307, 667, -770, -390, -201, 455, 664, 49,
         -343, -548, -778, 323, -47, -141, 774, 629, 380],
        [-1000, -994, -993, -987, -915, -900, -899, -890, -880, -853, -823, -814, -809, -798, -797, -778, -770, -764,
         -698, -646, -588, -548, -529, -515, -488, -474, -457, -450, -437, -419, -418, -415, -390, -372, -362, -360,
         -355, -343, -319, -299, -279, -271, -264, -246, -236, -201, -149, -148, -144, -141, -112, -65, -60, -47, -15,
         33, 36, 49, 59, 89, 110, 126, 143, 171, 204, 215, 223, 240, 252, 258, 260, 296, 304, 305, 307, 323, 341, 346,
         380, 380, 387, 455, 482, 497, 516, 553, 589, 599, 602, 623, 629, 644, 664, 667, 692, 698, 727, 748, 748, 764,
         774, 780, 803, 822, 856, 871, 890, 896, 914, 928, 966, 971]
    ],
    [
        [258, -271, -236, -246, 33, 748, -415, -144, 896, -900, -993, 764, -419, -60, -646, -588, -880, -279, 928, -797,
         -809, -457, -488, 966, 803, 215, -899, -814, 589, -450, -764, -987, 110, -1000, 748, 223, -319, 698, 914, -148,
         -65, -890, 296, 89, 623, -529, -264, -798, 346, 599, -372, -515, -994, 644, 780, 305, 143, -360, 341, 516, 871,
         204, 692, 387, -915, 380, 36, -474, 260, -112, 482, -15, -362, -437, 822, 856, -853, 304, 971, 602, 497, 727,
         -698, -823, -149, 240, -299, 252, 171, 890, 126, -418, 553, -355, 59, 307, 667, -770, -390, -201, 455, 664, 49,
         -343, -548, -778, 323, -47, -141, 774, 629, 380, 440, 424, -876, 731, 98, 104, -397, 384, 960, 467, 661, 337,
         -29, -18, 528, 772],
        [-1000, -994, -993, -987, -915, -900, -899, -890, -880, -876, -853, -823, -814, -809, -798, -797, -778, -770,
         -764, -698, -646, -588, -548, -529, -515, -488, -474, -457, -450, -437, -419, -418, -415, -397, -390, -372,
         -362, -360, -355, -343, -319, -299, -279, -271, -264, -246, -236, -201, -149, -148, -144, -141, -112, -65, -60,
         -47, -29, -18, -15, 33, 36, 49, 59, 89, 98, 104, 110, 126, 143, 171, 204, 215, 223, 240, 252, 258, 260, 296,
         304, 305, 307, 323, 337, 341, 346, 380, 380, 384, 387, 424, 440, 455, 467, 482, 497, 516, 528, 553, 589, 599,
         602, 623, 629, 644, 661, 664, 667, 692, 698, 727, 731, 748, 748, 764, 772, 774, 780, 803, 822, 856, 871, 890,
         896, 914, 928, 960, 966, 971]
    ]
]


class TestSortingAlgorithms(unittest.TestCase):
    def test_bubble(self):
        for i in range(len(testing_lists)):
            self.assertListEqual(bubble_sort(testing_lists[i][0]), testing_lists[i][1])

    def test_selection(self):
        for i in range(len(testing_lists)):
            self.assertListEqual(selection_sort(testing_lists[i][0]), testing_lists[i][1])

    def test_insertion(self):
        for i in range(len(testing_lists)):
            self.assertListEqual(insertion_sort(testing_lists[i][0]), testing_lists[i][1])

    def test_quick(self):
        for i in range(len(testing_lists)):
            self.assertListEqual(quick_sort(testing_lists[i][0]), testing_lists[i][1])

    def test_merge(self):
        for i in range(len(testing_lists)):
            self.assertListEqual(merge_sort(testing_lists[i][0]), testing_lists[i][1])


if __name__ == '__main__':
    unittest.main()
