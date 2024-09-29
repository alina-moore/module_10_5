import time
from multiprocessing import Pool

def read_info(name):
    all_data = []
    with open(name, 'r') as file:
        while True:
            line = file.readline()
            if not line:
                break
            all_data.append(line.strip())
    return all_data  

if __name__ == '__main__':
    filenames = [f'./file {number}.txt' for number in range(1, 5)]

    # Линейный вызов
    start_time = time.monotonic()
    for filename in filenames:
        read_info(filename)
    end_time = time.monotonic()
    print(f"Линейный вызов занял: {end_time - start_time:.6f} секунд")

    # Многопроцессный вызов
    start_time = time.monotonic()
    with Pool() as pool:
        pool.map(read_info, filenames)
    end_time = time.monotonic()
    print(f"Многопроцессный вызов занял: {end_time - start_time:.6f} секунд")
