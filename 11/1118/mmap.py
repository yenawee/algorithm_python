import timeit

def regular_io(filename):
    with open(filename, mode="r", encoding="utf8") as file_obj:
        text = file_obj.read()
        print(text)

# import mmap

# def mmap_io(filename):
#     with open(filename, mode="r", encoding="utf8") as file_obj:
#         with mmap.mmap(file_obj.fileno(), length=0, access=mmap.ACCESS_READ) as mmap_obj:
#             text = mmap_obj.read()
#             print(text)

t1 = timeit.repeat(
    'regular_io("text")',
    repeat=3,
    number=1,
    setup="from __main__ import regular_io")

print(t1)
# timeit.repeat(
#     "mmap_io_find(text)",
#     repeat=3,
#     number=1,
#     setup="from __main__ import mmap_io_find, filename")