import time

def get_time_to_complete_task():
    t1 = time.time()
    output = []
    for i in range(1, 10000000):
        output.append(i**3)
    t2 = time.time()
    difference = t2 - t1
    print("Total Time taken:", difference)
    # 3.636352777481079
    # print(output)

def get_cube_with_list_comp():
    t1 = time.time()
    output = [x**3 for x in range(1, 10000000)]
    t2 = time.time()
    difference = t2 - t1
    print("Total Time taken:", difference)

def get_memory_usage():
    import psutil
    while True:
        print(psutil.virtual_memory())

get_memory_usage()