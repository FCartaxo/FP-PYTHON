"""
bubble_sort_demo.py
demonstrate bubble sort
"""

#my_list = [8, 10, 6, 2, 4]  # list to sort
#swapped = True  # It's a little fake, we need it to enter the while loop.

#while swapped:
 #   swapped = False  # no swaps so far
  #  for i in range(len(my_list) - 1):
   #     if my_list[i] > my_list[i + 1]:
    #        swapped = True  # a swap occurred!
     #       my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]

#print(my_list)

numero = int(input("Um numero? "))

if numero > 0:
    print("positivo")
elif numero < 0:
    print("negativo")
else:
    print("nulo")