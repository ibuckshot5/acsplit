import configargparse

def main():
    parser = configargparse.ArgumentParser()
    parser.add_argument('-af', '--accounts-file', default='accounts.csv', help='Base account file to use')
    parser.add_argument('-r', '--result', default='workers/hive<index>.csv', help='Result')
    parser.add_argument('-c', '--count', default=5, help='# of accounts')
    args = parser.parse_args()
    args.count += 1
    f = open(args.accounts_file, 'r')
    lines = f.readlines()
    i = 0
    hi = 1
    lc = []
    for line in lines:
        i += 1
        lc.append(line)
        if i == args.count:
            stre = ''
            for r in lc:
                stre += r
            temp = open(get_file_name(hi, args.result), 'w+')
            temp.write(stre.strip()[:-2])
            temp.close()
            hi += 1
            i = 0
            lc = []
            print('Writing {}'.format(get_file_name(hi, args.result)))


    print('All done!')


def get_file_name(index, template):
    return str(template).replace('<index>', str(index))

if __name__ == '__main__':
    main()
