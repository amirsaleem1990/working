import time

s_start = !du -shc session* -B M| grep total
s_start = int(s_start[0].split("\t")[0][:-1])

privous_size = int()
while True:
    n = datetime.datetime.now()
    time.sleep(10)
    s = !du -shc session* -B M| grep total
    s = int(s[0].split("\t")[0][:-1])
    print(s - s_start, f"0{n.hour-12}:{n.minute}")
    s_start = s