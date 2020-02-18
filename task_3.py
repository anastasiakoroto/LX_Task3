from concurrent.futures import ThreadPoolExecutor


def function(args, a):
    for _ in range(args):
        a += 1
    return a


def main():
    a = 0
    with ThreadPoolExecutor(max_workers=5) as executor:
        for i in range(5):
            a = executor.submit(function, 1_000_000, a).result()

    print("----------------------", a)  # 5_000_000


main()
