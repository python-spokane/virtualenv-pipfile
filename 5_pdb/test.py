def basic_test():
    print('started basic_test')

    for x in range(0, 20):
        print(x)

    print('finished basic_test')


def pdb_command_playground():
    print('started pdb_command_playground')

    for x in range(0, 20):
        print(x)

    basic_test()

    print('finished pdb_command_playground')


if __name__ == '__main__':
    basic_test()
