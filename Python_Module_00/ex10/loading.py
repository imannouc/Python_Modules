from time import sleep


# elapsed seconds,
# 2.33 / 233 * (1000-233)
# 
def ft_progress(lst):
    current = 1
    total = max(lst) + 1
    print( current / total * 100)
    # for current in lst:
    #     print(f"ETA: {ETA}s [ {round(current / total * 100)}%][=====> ] {current}/{total} | elapsed time {(elapsed * 100)}s")
    #     yield current

listy = range(1000)
ret = 0
for elem in ft_progress(listy):
    ret += (elem + 3) % 5
    sleep(0.01)
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