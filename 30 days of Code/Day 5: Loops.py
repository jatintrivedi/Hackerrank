if __name__ == '__main__':
    n = int(input().strip())
    pro = 1
    for i in range(1,11):
        pro = n * i
        print('{} x {} = {}'.format(n, i, pro))
