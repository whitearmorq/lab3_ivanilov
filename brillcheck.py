from p_polard import pollards_rho
from brill import brillhart_morris
from time import time

tasklist = [3009182572376191, 1021514194991569, 4000852962116741, 15196946347083, 499664789704823, 269322119833303,
           679321846483919, 96267366284849, 61333127792637, 2485021628404193]

for task in tasklist:
    print(f"Розкладаю число {task} методом полларда:")
    start_time = time()
    res1 = pollards_rho(task)
    difference1 = time() - start_time
    print(f"Час розкладання поллардом(сек): {difference1}")
    print(f"Дільник знайдений поллардом: {res1}")

    print("---------------------------------------------")
    
    print(f"Розкладаю число {task} мето дом бріллхарта:")
    start_time = time()
    res2 = brillhart_morris(task)
    diff2 = time() - start_time
    print(f"Час розкладання бріллхартом(сек): {diff2}")
    print(f"Дільник знайдений брілхартом: {res2}")

    print("---------------------------------------------")