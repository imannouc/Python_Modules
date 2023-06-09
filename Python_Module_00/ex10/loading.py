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
    eta = 1

    for i , item in enumerate(lst):
        tn = time()
        elapsed = tn - t0
        progressBar = f"[{'=' * (round(((i + 1) / total) * 100))}>{' ' *(100 - round(((i + 1) / total) * 100))}]"
        if ( i != 0 ):
            eta = (elapsed / (i)) * (total - i)
        print(f"ETA: {round(eta,2):>5.2f}s [{round(((i + 1) / total) * 100):>3}%] {progressBar} {i + 1:>{len(str(total))}}/{total:>{len(str(total))}} | elapsed time {round(elapsed,2):>5.2f}s",end='')
        print('',end='\r')
        yield item

listy = range(1000)
ret = 0
for elem in ft_progress(listy):
    ret += (elem + 3) % 5
    sleep(0.001)
print()
print(ret)
