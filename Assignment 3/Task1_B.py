from ssl import HAS_ECDH
from Task1_A import get_hashcode, div_compression
from LinkedList import LinkedList

class Chaining:
    def __init__(self, table_size):
        '''
        Arguments:
        table_size: Integer
        '''
        
        self.table_size = table_size
        self.hash_table = [LinkedList() for i in range(self.table_size)]

    def get_hash(self, value):
        '''
        Arguments:
        value: String
        
        Returns: 
        Compressed Hash Code: Integer
        
        Use functions from Task1_A.py here
        '''

        hash_code = get_hashcode(value)
        compressed_hash_code = div_compression(hash_code, self.table_size)

        return compressed_hash_code

    def insert_word(self, value):
        '''
        Arguments:
        value: String
        
        Returns: Nothing
        '''

        index = self.get_hash(value)
        self.hash_table[index].insert_at_tail(value)

        return



    def delete_word(self, value):
        '''
        Arguments:
        value: String
        
        Returns: Nothing
        '''
        index = self.get_hash(value)
        self.hash_table[index].delete_any(value)

        return

    def lookup_word(self, value):
        '''
        Arguments:
        value: String
        
        Returns:
        if value is found: the value (String)
        if value is not found: False
        '''
        index = self.get_hash(value)
        return self.hash_table[index].get_element(value)


# def main():
#     pass


# main()