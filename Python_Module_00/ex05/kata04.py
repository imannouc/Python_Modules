kata = (0, 4, 132.42222, 10000, 12345.67)

if __name__ == '__main__':
    print(f'module_{str(kata[0]).zfill(2)}, ex_{str(kata[1]).zfill(2)} : {kata[2]:.2f}, ',end='')
    print(f'{kata[3]:.2e}, {kata[4]:.2e}')
