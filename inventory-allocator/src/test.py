import unittest
import InventoryAllocator as al


class Test(unittest.TestCase):

    # scenario where we have more units of the items than desired
    def test_one(self):
        self.assertEqual(al.InventoryAllocator().calculateCheapestShipment({'apple': 5, 'orange': 6}, [
            {'name': 'one', 'inventory': {'apple': 6, 'orange': 5}},
            {'name': 'two', 'inventory': {'apple': 4, 'orange': 6}}
        ]), [{'one': {'orange': 5, 'apple': 5}}, {'two': {'orange': 1}}])

    # scenario where we have the exact desired units of an ordered item
    def test_two(self):
        self.assertEqual(al.InventoryAllocator().calculateCheapestShipment({'apple': 1}, [
                         {'name': 'owd', 'inventory': {'apple': 1}}]), [{'owd': {'apple': 1}}])

    # scenario where we dont have any unit of a desire item
    def test_three(self):
        self.assertEqual(al.InventoryAllocator().calculateCheapestShipment({'apple': 1}, [
            {'name': 'owd', 'inventory': {'apple': 0}}
        ]), [])

    # scenario where we need to ship the items from different warehouses
    def test_four(self):
        self.assertEqual(al.InventoryAllocator().calculateCheapestShipment({'apple': 10}, [{'name': 'owd', 'inventory': {
                         'apple': 5}}, {'name': 'dm', 'inventory': {'apple': 5}}]), [{'owd': {'apple': 5}}, {'dm': {'apple': 5}}])

    # scenario where we have more units of the ordered items across multiple warehouses
    def test_five(self):
        self.assertEqual(al.InventoryAllocator().calculateCheapestShipment({'apple': 5, 'banana': 5, 'orange': 5}, [{'name': 'owd', 'inventory': {
                         'apple': 5, 'orange': 10}}, {'name': 'dm', 'inventory': {'banana': 5, 'orange': 10}}]), [{'owd': {'apple': 5, 'orange': 5}}, {'dm': {'banana': 5}}])

    # scenario where we dont have some of the desired items (banana in this case). We can also configure this and test_seven api to return empty list in this case.
    # Its like prompting the user with the message "Hey, we have everything you need but bananas, please buy them again later."
    def test_six(self):
        self.assertEqual(al.InventoryAllocator().calculateCheapestShipment({'apple': 5, 'banana': 5, 'orange': 5}, [{'name': 'owd', 'inventory': {
                         'apple': 5, 'orange': 10}}, {'name': 'dm', 'inventory': {'orange': 10}}]), [{'owd': {'apple': 5, 'orange': 5}}])

    # scenario where the user has ordered 10 apples but we have only 9.
    def test_seven(self):
        self.assertEqual(al.InventoryAllocator().calculateCheapestShipment({'apple': 10}, [{'name': 'owd', 'inventory': {
                         'apple': 5}}, {'name': 'dm', 'inventory': {'apple': 4}}]), [{'owd': {'apple': 5}}, {'dm': {'apple': 4}}])

    # scenario where some of ordered items are currently out of stock for some warehouses.
    def test_eight(self):
        self.assertEqual(al.InventoryAllocator().calculateCheapestShipment({'apple': 5, 'orange': 5}, [{'name': 'owd', 'inventory': {
                         'apple': 5, 'orange': 0}}, {'name': 'dm', 'inventory': {'apple': 0, 'orange': 4}}]), [{'owd': {'apple': 5}}, {'dm': {'orange': 4}}])

    # scenario where we stop our search after we have gathered required units.
    def test_nine(self):
        self.assertEqual(al.InventoryAllocator().calculateCheapestShipment({'apple': 5}, [{'name': 'owd', 'inventory': {
                         'apple': 2}}, {'name': 'dm', 'inventory': {'apple': 2}}, {'name': 'abc', 'inventory': {
                             'apple': 0}}, {'name': 'def', 'inventory': {'apple': 3}}, {'name': 'ghi', 'inventory': {'apple': 3}}]), [{'owd': {'apple': 2}}, {'dm': {'apple': 2}}, {'def': {'apple': 1}}])


if __name__ == '__main__':
    unittest.main()
