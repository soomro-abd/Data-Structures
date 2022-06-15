# Implement your Hash Function here

def get_hashcode(value):
    '''
    Arguments:
    value: String
    
    Returns:
    Hash Code: Integer
    '''

    bitwise_hash = 0

    for char in value:
        bitwise_hash ^= (bitwise_hash << 5) + (bitwise_hash >> 2) + ord(char)

    return bitwise_hash



def div_compression(hash_code, table_size):
    '''
    Arguments:
    hash_code: Integer
    table_size: Integer
    
    Returns: 
    Compressed hash code: Integer
    '''
    
    return (hash_code % table_size)

def hash(value, table_size):
    hash_code = get_hashcode(value)
    compressed_hash_code = div_compression(hash_code, table_size)

    return compressed_hash_code

# def main():
    
#     print(get_hashcode("Hello"))

# main()