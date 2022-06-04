# Class
class HashTable:
    # Constructor
    def __init__(self, length=10):
        self.table: list[list] = [[] for i in range(length)]
        self.__length = length
    # method for hash key
    def __hash_key(self, key) -> int:
        '''Returns a table index, used to store the object based on the key'''
        return hash(key) % self.__length

    def __getitem__(self, key):
        '''Returns item associated with key, eg. hashTable['key'] -> item'''
        idx = self.__hash_key(key)  # index for subtable
        for _key, item in self.table[idx]:  # iterate the subtable key/value pairs
            if _key == key:  # If a matching key was found...
                return item  # return the item
        else:  # If no match, raise exception
            raise KeyError(f'{key} not in table')

    def __setitem__(self, key, item):
        '''Allows user to set items using `[]`, eg. `hTable['key'] = 'item'`'''
        idx = self.__hash_key(key)  # hash key
        subtable = self.table[idx]
        # Update if key exists, else insert
        for key_idx, (_key, _) in enumerate(subtable):  # item's key and the key index
            if _key == key:  # On match, update item
                subtable[key_idx] = item
                break
        else:  # Key not found, insert key/item pair
            subtable.append([key, item])
    # Sorting items
    def __iter__(self):
        for item in sorted((_item for sublist in self.table for _key, _item in sublist if _item)):
            yield item

        # for subtable in self.table:
        #     for kvp in subtable:
        #         if kvp[1]:
        #             yield kvp[1]
        #         else:
        #             continue

    def insert(self, key, item):
        self[key] = item
    # Update table
    def update(self, key, item):
        self[key] = item
    # Remove methods
    def remove(self, key):
        idx = self.__hash_key(key)
        subtable = self.table[idx]
        for key_idx, (_key, _) in enumerate(subtable):
            if _key == key:  # found item to remove
                del subtable[key_idx]
                break
        else:
            raise KeyError(f'{key} not in table')

    '''Returns the item associated with the key'''
    def search(self, key):

        return self[key]
