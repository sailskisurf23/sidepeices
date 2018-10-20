
def chocolate(n, first_bar, second_bar):
    first_str = ''.join([str(x) for x in first_bar])
    second_str = ''.join([str(x) for x in second_bar])

    breaks = -1
    test_str = first_str
    start_idx = 0
    chunk_len = len(test_str)
    while chunk_len > 0:
        print('check {} not in {}'.format(test_str, second_str))
        if test_str not in second_str:
            chunk_len -= 1
            test_str = first_str[start_idx:start_idx+chunk_len]
            print('if block chunk_len {}, test_str {}'.format(chunk_len,test_str))
        else:
            breaks += 1
            start_idx += chunk_len
            test_str = first_str[start_idx:]
            chunk_len = len(test_str)
            print('else block breaks {}, test_str {}, chunk_len {}'.format(breaks,test_str,chunk_len))

    return breaks

n = 5
first_bar = [3, 5, 2, 1, 4]
second_bar = [4, 5, 2, 1, 3]

print(chocolate(n, first_bar, second_bar))
