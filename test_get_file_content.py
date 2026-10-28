from functions.get_file_content import get_file_content

def test():
    result = get_file_content("calculator", "lorem.txt")
    print(f"lorem.txt length: {len(result)}")
    print(f"lorem.txt truncated: {'truncated' in result}")
    
if __name__ == '__main__':
    test()