items = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']

def displayInventory(items):
    print('Inventory:')
    item_total = 0
    for k, v in items.items():
        print(str(v) + ' ' + k)
        item_total = item_total + v
    print('Total number of items: ' + str(item_total))
    return

def addToInventory(inventory, addedItems):
    added = []
    for item in dragonLoot:
        if item in items :
            if item not in added:
                items[item] = items[item] + dragonLoot.count(item)
                added.append(item)
        else:
            items[item] = dragonLoot.count(item)
    return

displayInventory(items)
print
print('You killed a dragon!')
addToInventory(items, dragonLoot)
displayInventory(items)
exit()