
def main():
    n = int(input('n = '))
    seq = '1'

    for i in range(0, n - 1):
        num_list = make_num_list(seq)
        seq = make_new_seq(num_list)

    print(seq)


def make_num_list(seq):
    ret = []

    if len(seq) == 0:
        return None

    else:
        spliting_index = get_spliting_index(seq)
        ret.append({'number': seq[0], 'count': spliting_index})

        following = make_num_list(seq[spliting_index:])
        if following is not None:
            ret = ret + following

        return ret


def get_spliting_index(seq):
    for i, char in enumerate(seq):
        if char != seq[0]:
            return i

    return len(seq)


def make_new_seq(num_list):
    ret = ''

    for item in num_list:
        number = item.get('number')
        count = item.get('count')

        ret = ret + str(count) + number

    return ret


if __name__ == '__main__':
    main()
