from test import pdb_command_playground


def main():
    import pdb; pdb.set_trace()
    print('Started main')

    print('command: h(elp), purpose: help')

    for x in range(0, 2):
        print('command: w(here), purpose: show where we are in the call stack')
        print('command: u(p), purpose: move up a frame')
        print('command: d(own), purpose: move down a frame')

    # print('command: b(reak), purpose: set a breakpoint in the current file')
    # for x in range(0, 4):
    #     print(x)

    # print('command: tbreak, purpose: set a breakpoint in the current file and only hit once')
    # for x in range(0, 2):
    #     print(x)

    print('command: n(ext), purpose: execute the current line and stop')
    print('command: s(tep), purpose: execute the current line and stop at next possible spot')
    pdb_command_playground()

    print('command: d(own), purpose: step in to the function')

    print('Finished main')


if __name__ == '__main__':
    main()
