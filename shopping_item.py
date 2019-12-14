from typing import Dict, List
from test_cases import default_testcases


class ShoppingItem:
    """ A Shopping Item represents one item on the shopping list
    """

    max_name_length = -1
    max_quantity_digits = -1

    def __init__(self, name: str, price: float, quantity: float):
        """ Warns about poor formatting of __str__
         if name length or digits exceed respective maximums.

        :param name: name of product
        :param price: price of single product
        :param quantity: quantity of products
        """
        if len(name) > ShoppingItem.max_name_length:
            ShoppingItem.max_name_length = len(name)
        if len(str(quantity)) > ShoppingItem.max_quantity_digits:
            ShoppingItem.max_quantity_digits = len(str(quantity))
        self.name = name
        self.price_per = price
        self.quantity = quantity

    def total_price(self):
        """ Get total price of item

        :return: quantity * price_per
        """
        return self.quantity * self.price_per

    def __str__(self) -> str:
        """ Formats to string:
         * name
         * price
         * quantity
         * total price

        :return: formatted
        """
        str_format = "Name: {:<" + str(ShoppingItem.max_name_length) + "} "
        str_format += "Price Per Item: {:<5} "
        str_format += "Quantity: {:<" + str(ShoppingItem.max_quantity_digits) + "} "
        str_format += "Total Price: {:<5} "
        return str_format.format(self.name, self.price_per, self.quantity, self.total_price())


def tests(testcases: Dict[str, List[float]] = default_testcases):
    """ Constructs and prints testcases as Shopping Items

    :param testcases: Defaults to default_testcases
        Key: item name
        Value: list of shopping item parameters.
    """
    shopping_items = []
    for key, val in testcases.items():
        shopping_items.append(ShoppingItem(key, val[0], val[1]))

    for i in shopping_items:
        print(i)


if __name__ == "__main__":
    tests()
