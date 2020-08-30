import unittest
import InventoryAllocator as al


class Test(unittest.TestCase):

    # scenario where we can ship an item (in this case: orange) from multiple cheaper-cost warehouse, but one other costlier warehouse has enough items.
    # In this case we ship the item from one warehouse even if it appears later in the array.
    def test_one(self):
        self.assertEqual(al.InventoryAllocator().calculateCheapestShipment({'apple': 5, 'orange': 5, 'banana': 5}, [
            {'name': 'a', 'inventory': {'apple': 5, 'orange': 3, 'banana': 3}},
            {'name': 'b', 'inventory': {'banana': 3, 'orange': 3}},
            {'name': 'c', 'inventory': {'apple': 5, 'orange': 6}}
        ]), [{'a': {'apple': 5, 'banana': 3}}, {'b': {'banana': 2}}, {'c': {'orange': 5}}])

    # scenario where we have to ship the order from multiple warehouses.
    def test_two(self):
        self.assertEqual(al.InventoryAllocator().calculateCheapestShipment({'apple': 5, 'banana': 5}, [
            {'name': 'a', 'inventory': {'apple': 5, 'orange': 3, 'banana': 3}},
            {'name': 'b', 'inventory': {'banana': 3, 'orange': 3}},
            {'name': 'c', 'inventory': {'apple': 5, 'orange': 6}}
        ]), [{'a': {'apple': 5, 'banana': 3}}, {'b': {'banana': 2}}])

    # # scenario where we dont have enough units of a desire item
    def test_three(self):
        self.assertEqual(al.InventoryAllocator().calculateCheapestShipment({'apple': 2}, [
            {'name': 'owd', 'inventory': {'apple': 1}},
            {'name': 'owd', 'inventory': {'apple': 0}}
        ]), [])

    # # scenario where we need to ship the items from different warehouses
    def test_four(self):
        self.assertEqual(al.InventoryAllocator().calculateCheapestShipment({'apple': 10}, [
            {'name': 'owd', 'inventory': {'apple': 5}},
            {'name': 'dm', 'inventory': {'apple': 5}},
            {'name': 'xy', 'inventory': {'apple': 5}}
        ]), [{'owd': {'apple': 5}}, {'dm': {'apple': 5}}])

    # # scenario where we have more units of the ordered items across multiple warehouses
    def test_five(self):
        self.assertEqual(al.InventoryAllocator().calculateCheapestShipment({'apple': 5, 'banana': 5, 'orange': 5}, [
            {'name': 'owd', 'inventory': {'apple': 5, 'orange': 10}},
            {'name': 'dm', 'inventory': {'banana': 5, 'orange': 10}}
        ]), [{'owd': {'apple': 5, 'orange': 5}}, {'dm': {'banana': 5}}])

    # scenario where we dont have SOME of the desired items (banana in this case). We return [].
    def test_six(self):
        self.assertEqual(al.InventoryAllocator().calculateCheapestShipment({'apple': 5, 'banana': 5, 'orange': 5}, [
            {'name': 'owd', 'inventory': {'apple': 5, 'orange': 10}},
            {'name': 'dm', 'inventory': {'orange': 10}}
        ]), [])

    # # scenario where the user has ordered 10 apples but we have only 9.
    def test_seven(self):
        self.assertEqual(al.InventoryAllocator().calculateCheapestShipment({'apple': 10}, [
            {'name': 'owd', 'inventory': {'apple': 5}},
            {'name': 'dm', 'inventory': {'apple': 4}}
        ]), [])

    # scenario where some of ordered items are currently out of stock for some warehouses.
    def test_eight(self):
        self.assertEqual(al.InventoryAllocator().calculateCheapestShipment({'apple': 5, 'orange': 5}, [
            {'name': 'owd', 'inventory': {'apple': 5, 'orange': 0}},
            {'name': 'dm', 'inventory': {'apple': 0, 'orange': 4}}
        ]), [])

    # scenario where we stop our search after we have gathered required units.
    def test_nine(self):
        self.assertEqual(al.InventoryAllocator().calculateCheapestShipment({'apple': 5}, [
            {'name': 'owd', 'inventory': {'apple': 2}},
            {'name': 'dm', 'inventory': {'apple': 2}},
            {'name': 'abc', 'inventory': {'apple': 0}},
            {'name': 'def', 'inventory': {'apple': 3}},
            {'name': 'ghi', 'inventory': {'apple': 3}}
        ]), [{'owd': {'apple': 2}}, {'dm': {'apple': 2}}, {'def': {'apple': 1}}])


if __name__ == '__main__':
    unittest.main()
