#!/usr/bin/python3
"""This module create an inheritated class from lists"""


class MyList(list):
    """MyList class"""

    def print_sorted(self):
        """ sort an instance of MyList """

        n_list = self.copy()
        print(sorted(n_list))
