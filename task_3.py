from concurrent.futures import ThreadPoolExecutor

a = 0


def function(args):
    global a
    for _ in range(args):
        a += 1


def main():

    with ThreadPoolExecutor(max_workers=5) as executor:
        for i in range(5):
            executor.submit(function, 1_000_000).result()

    print("----------------------", a)  # 5_000_000


main()
