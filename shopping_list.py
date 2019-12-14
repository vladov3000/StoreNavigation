from typing import List, Dict
from shopping_item import ShoppingItem
from test_cases import default_testcases

class ShoppingList:

    def __init__(self, shopping_items: List[ShoppingItem]):
        self.shopping_items = shopping_items

    def __str__(self):
        for i in self.shopping_items:
            print(i)


def tests(testcases: Dict[str, List[float]] = default_testcases):
    """ Constructs and prints a Shopping List

    :param testcases: Defaults to default_testcases
        Key: item name
        Value: list of shopping item parameters.
    """
    shopping_items = []
    for key, val in testcases.items():
        shopping_items.append(ShoppingItem(key, val[0], val[1]))

    print(ShoppingList(shopping_items))

if __name__ == "__main__":
    tests()
