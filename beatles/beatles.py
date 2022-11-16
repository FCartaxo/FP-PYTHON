# step 1
beatles = []
print("Step 1:", beatles)

# step 2
beatles.append ('John Lennon')
beatles.append ('Paul McCartney')
beatles.append ('George Harrison')
print("Step 2:", beatles)


# step 3
print("Step 3:", beatles)

for i in range (2):
    member = input("Adicione nomes à banda: " )
    beatles.append(member)

# step 4
print("Step 4:", beatles)

for i in range (2):
    length = len(beatles) -1
    del beatles [length]

# step 5
print("Step 5:", beatles)

beatles.insert (0, 'Ringo Star')
print(beatles)

# testing list legth
print("The Fab", len(beatles))