

class InventoryAllocator:

    def calculateCheapestShipment(self, orders, inventoryList):

        cheapestShipment = []
        
        for order in orders:
            requirement = orders[order]

            for warehouse in inventoryList:

                if order in warehouse['inventory']:
                    
                    # if we have more items than required then we cancel all the other warehouse and fulfill the order from this warehouse.
                    if warehouse['inventory'][order] >= orders[order]: 

                        found_flag = 0

                        for shipment in cheapestShipment:
                            for warehouseName in shipment:
                                if order in shipment[warehouseName]:
                                    del shipment[warehouseName][order]
                                elif warehouseName == warehouse['name']:
                                    shipment[warehouseName][order] = requirement
                                    requirement -= warehouse['inventory'][order]
                                    found_flag = 1

                        if found_flag == 0:
                            cheapestShipment.append(
                                {warehouse['name']: {order: orders[order]}})
                            requirement -= warehouse['inventory'][order]

                        break
                        
                    # if we found less items in the current warehouse then we consider it and continue our search.
                    else:
                        if requirement > 0 and warehouse['inventory'][order] != 0:
                            found_flag = 0
                            for shipment in cheapestShipment:
                                for warehouseName in shipment:
                                    if warehouseName == warehouse['name']:
                                        shipment[warehouseName][order] = warehouse['inventory'][
                                            order] if requirement > warehouse['inventory'][order] else requirement
                                        requirement -= warehouse['inventory'][order]
                                        found_flag = 1

                            if found_flag == 0:
                                cheapestShipment.append(
                                    {warehouse['name']: {order: warehouse['inventory'][order] if requirement > warehouse['inventory'][order] else requirement}})
                                requirement -= warehouse['inventory'][order]
            
            # if we dont have enough items then we return []
            if requirement > 0:
                return []

        return cheapestShipment
