

class InventoryAllocator:

    def calculateCheapestShipment(self, orders, inventoryList):

        cheapestShipment = []

        # looping through all the warehouses
        for inventory in inventoryList:

            # this is a dictionary (map) of desired items to be added to the result list for each warehouse.
            desiredItems = {}

            # looping through all the orders to check if we can find any available items in this warehouse.
            for order in orders.keys():

                # proceed forward only if the item is mentioned in warehouse database
                if order in inventory['inventory']:

                    # this is the scenario where we have all the items required at this warehouse
                    if orders[order] <= inventory['inventory'][order]:

                        desiredItems[order] = orders[order]

                        # after we had all the required items we will delete that item from orders dictionary (map), so we dont check that item in another warehouses.
                        del orders[order]

                    # this is the scenario where we dont have enough items in this warehouse, so we take whatever is available and go forward
                    elif(inventory['inventory'][order] != 0):

                        desiredItems[order] = inventory['inventory'][order]

                        # in this case, we update the current required amount
                        orders[order] = orders[order] - \
                            inventory['inventory'][order]

            # add the warehouse to the result only if we find anything required from that warehouse
            if desiredItems != {}:
                cheapestShipment.append({inventory['name']: desiredItems})

        # SINCE it is not mentioned about the scenario what to do where if a user ordered 10 items and we have only 5 avalilable, so I am assuming we return what is available. If we want to return empty list, we can do it like below.

        # if len(orders) != 0:
        #     cheapestShipment = []

        return cheapestShipment
