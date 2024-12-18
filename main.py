# 1-misol
# import threading
#
# def a_sum(n):
#     result = sum(int(b) for b in str(n))
#     print(f"{n} -> {result}")
#
# num = 21513
# thread1 = threading.Thread(target=a_sum, args=(num,))
# thread1.start()
# thread1.join()


# 2-misol

# def soniyalar_to_dhms(seconds):
#     days = seconds // 86400
#     hours = (seconds % 86400) // 3600
#     minutes = (seconds % 3600) // 60
#     seconds = seconds % 60
#     print(f"{seconds} sekund = {days} kun, {hours} soat, {minutes} minut, {seconds} sekund")
#
# seconds = 54523154865321
# thread2 = threading.Thread(target=soniyalar_to_dhms, args=(seconds,))
# thread2.start()
# thread2.join()

# 3-misol
# def katata_harf(names):
#     result = [name.capitalize() for name in names]
#     print(f"Natija: {result}")
#
# iasmlar = ['alfred', 'tabitha', 'william', 'arla']
# thread3 = threading.Thread(target=katata_harf, args=(iasmlar,))
# thread3.start()
# thread3.join()

# 4-misol

# def son_filtr(ball):
#     result = [score for score in ball if score > 75]
#     print(f"Natija: {result}")
#
# rqamamlar = [66, 90, 68, 59, 76, 60, 88, 74, 81, 65]
# thread4 = threading.Thread(target=son_filtr, args=(rqamamlar,))
# thread4.start()
# thread4.join()


# 5-misol
# def a(sozlar):
#     result = [soz for soz in sozlar if soz.lower() == soz[::-1].lower()]
#     print(f"Natija: {result}")
#
# a = ['Anna', 'Alexey', 'Alla', 'Kazak', 'Dom']
# thread5 = threading.Thread(target=a, args=(words,))
# thread5.start()
# thread5.join()

# 6-misol

# def almashtrish(text):
#     a = ""
#     i = 0
#     while i < len(text):
#         result += '3' if text[i] == 'e' else text[i]
#         i += 1
#     print(a)
#
# text = input("Matn kiriting: ")
# thread6 = threading.Thread(target=almashtrish, args=(text,))
# thread6.start()
# thread6.join()


# 7-misol
# def boshjoy(text):
#     a = ""
#     i = 0
#     while i < len(text):
#         if text[i] != ' ':
#             a += text[i]
#         i += 1
#     print(a)
#
# text = input("Matn kiriting: ")
# thread7 = threading.Thread(target=boshjoy, args=(text,))
# thread7.start()
# thread7.join()


# 8-misol
# def 2_ga_kopaytiring(index, value):
#     print(f"Element {index}: {value} * 2 = {value * 2}")
#
# numbers = [i for i in range(1, 11)]
# threads = []
#
# for i, num in enumerate(numbers):
#     t = threading.Thread(target=2_ga_kopaytiring, args=(i, num))
#     threads.append(t)
#     t.start()
#
# for t in threads:
#     t.join()


# 9-misol
# import random
#
# def yaratish_tasodifiy(index):
#     rand_num = random.randint(1, 100)
#     print(f"Oqim {index}: {rand_num}")
#
# threads = []
#
# for i in range(10):
#     t = threading.Thread(target=yaratish_tasodifiy, args=(i,))
#     threads.append(t)
#     t.start()
#
# for t in threads:
#     t.join()
