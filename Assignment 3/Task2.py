from Task1_A import get_hashcode, div_compression


class TableItem:
    def __init__(self, k, v, hw):
        '''
        Arguments:
        k: Integer (Hash key)
        v: String
        hw: Bool (for Task2 = None, for Task3 = True/False)
        '''

        self.key = k
        self.value = v
        self.honeyword = hw


class LinearProbing(TableItem):
    def __init__(self, table_size):
        '''
        Arguments:
        table_size: Integer
        
        Class members:
        self.count = Integer (Counts the number of items in the Hashtable)
        self.table_size = Integer (The size of the hashtable)
        self.hash_table = List (Hashtable)
        '''
        self.count = 0
        self.table_size = table_size
        self.hash_table = [None for i in range(self.table_size)]

    def get_hash(self, value):
        '''
        Arguments:
        value: String

        Returns: 
        Compressed Hash Code: Integer

        Use functions from Task1_A.py here
        Essentially the same funciton you implemented in Task1_B.py
        '''
        hash_code = get_hashcode(value)
        compressed_hash_code = div_compression(hash_code, self.table_size)

        return compressed_hash_code

    def resize_table(self):
        '''
        Function called in insert_word() function.

        Choose resize factor of your choice. 
        This will determine the time you take to pass the tests so try different values.

        Returns: Nothing
        '''

        old_size = self.table_size
        self.table_size *= 3
        old_table = self.hash_table #saving a copy of prev hash table
        self.hash_table = [None for i in range(self.table_size)]
        self.count = 0

        for i in range(old_size):
            if old_table[i] != None:
                if old_table[i].key != None:
                    self.insert_word(old_table[i].value, None)


    def insert_word(self, value, honeyword_flag):
        '''
        Arguments:
        value: String
        honeyword_flag: Bool (for Task2 = None, for Task3 = True/False)

        Call resize() function here when loadfactor is high.
        Choose loadfactor of your choice. 
        This will determine the time you take to pass the tests so try different values.

        Returns: Nothing
        '''
        hash = self.get_hash(value)
        item = TableItem(hash, value, honeyword_flag)

        if (self.hash_table[hash] != None):
            if self.hash_table[hash].key != None:
                hash = (hash + 1) % self.table_size

                while (self.hash_table[hash] != None):
                    if self.hash_table[hash].key != None:
                        hash = (hash + 1) % self.table_size
                    else:
                        break

        self.hash_table[hash] = item
        self.count += 1

        load_factor = self.count / self.table_size

        if load_factor >= 0.5:
            self.resize_table()

    def delete_word(self, value):
        '''
        Arguments:
        value: String

        Returns: Nothing
        '''

        #changes the key to None

        hash = self.get_hash(value)
        index = self.get_hash(value)


        while self.hash_table[index] != None:
            if (self.hash_table[index].key == hash) and (self.hash_table[index].value == value):
                self.hash_table[index].key = None
                break

            index = (index + 1) % self.table_size

    def lookup_word(self, value):
        '''
        Arguments:
        value: String

        Returns:
        if value found: TableItem()
        if value not found: None
        '''


        hash = self.get_hash(value)
        index = self.get_hash(value)

        while self.hash_table[index] != None:
            if (self.hash_table[index].key == hash) and (self.hash_table[index].value == value):
                return self.hash_table[index]
            
            index = (index + 1) % self.table_size
        
        return None




