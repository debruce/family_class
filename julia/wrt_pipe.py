import time

with open('my_pipe', 'w') as f:
    for i in range(10):
        print(f"i={i}")
        f.write(f"i={i}\n")
        f.flush()
        time.sleep(5)