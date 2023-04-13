kata = (0, 4, 132.42222, 10000, 12345.67)

if __name__ == '__main__':
    print(f'module_{str(kata[0]).zfill(2)}, ex_{str(kata[1]).zfill(2)} : {round(kata[2],2)}, ',end='')
    print('{:.2e} {:.2e}'.format(kata[3],kata[4]))

# $> python3 kata04.py
# module_00, ex_04 : 132.42, 1.00e+04, 1.23e+04
# $> python3 kata04.py | cut -c 10,18
# ,: