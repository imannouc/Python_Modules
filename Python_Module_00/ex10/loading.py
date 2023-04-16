from time import sleep, time


# elapsed seconds,
# 2.33 / 233 * (1000-233)
def ft_progress(lst):
    t0 = time()
    elapsed = 0
    total = len(lst)
    if (total == 0):
        print("Invalid range.")
        exit()
    eta = 10000

    bar = '=>'
    for i in lst:
        yield i
        tn = time()
        elapsed = tn - t0
        if ( i != 0 ):
            eta = (elapsed / (i)) * (total - i)
        if (round((i / total) * 100) % 50 == 0):
            bar = '=' + bar
        print(f"ETA: {round(eta,2)}s [ {round((i / total) * 100)}%] BAR {i + 1}/{total} | elapsed time {round(elapsed,2)}s",end='\r')
# ETA: 14.67s [ 9%][=
# ETA: 8.67s [ 23%][=
listy = range(1000)
ret = 0
for elem in ft_progress(listy):
    ret += (elem + 3) % 5
    sleep(0.1)
print()
print(ret)


# EXAMPLE OF A GENERATOR FUNCTION

# def numeros_naturales(t):
#   n = 1
#   for n in t:
#     yield n
#     # n += 1
 
# for natural in numeros_naturales(range(100)):
#    print(natural)