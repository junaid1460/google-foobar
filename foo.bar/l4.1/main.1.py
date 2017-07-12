

        


import numpy as np 
def answer(entrances, exits, path):
    path = np.array(path)
    print(path)
    print(path.T)
    

 

    
                


    
            

entrances = [0]
exits = [5]
path = [
  [0, 10, 0, 0, 0, 9],  # Room 0: Bunnies
  [10, 0, 4, 6, 0, 0],  # Room 1: Bunnies
  [4, 6, 0, 0, 5, 9],  # Room 2: Intermediate room
  [3, 0, 0, 0, 2, 0],  # Room 3: Intermediate room
  [0, 0, 0, 0, 0, 4],  # Room 4: Escape pods
  [0, 0, 0, 0, 0, 9],  # Room 5: Escape pods
]
# entrances = [0]
# exits = [3]
# path = [[0, 3, 4, 0], 
#         [0, 0, 0, 3], 
#         [0, 0, 0, 2],
#         [9, 0, 0, 0]]

entrances = [0, 1]
exits = [4, 5]
path = [
  [0, 0, 4, 6, 0, 0],  # Room 0: Bunnies
  [0, 0, 5, 2, 0, 0],  # Room 1: Bunnies
  [0, 0, 0, 0, 4, 4],  # Room 2: Intermediate room
  [0, 0, 0, 0, 6, 6],  # Room 3: Intermediate room
  [0, 0, 0, 0, 0, 0],  # Room 4: Escape pods
  [0, 0, 0, 0, 0, 0],  # Room 5: Escape pods
]

entrances = [0]
exits = [3]
path = [[0, 7, 0, 0], 
        [0, 0, 6, 0], 
        [0, 0, 0, 8], 
        [9, 0, 0, 0]]
answer(entrances,exits,path)