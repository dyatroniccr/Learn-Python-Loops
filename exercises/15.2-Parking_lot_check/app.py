parking_state = [
  [1,1,1],
  [0,0,0],
  [1,1,2]
]

#Your code go here:

def get_parking_lot(park_matrix):
  
  state = {
      "total_slots": 0,
      "available_slots": 0,
      "occupied_slots": 0
  }

  for row in park_matrix:       
    for slots in row:
      if slots > 0:
        state["total_slots"] += 1
      if slots == 2:
        state["available_slots"] += 1
      if slots == 1:
        state["occupied_slots"] += 1
      
  return state

print(get_parking_lot(parking_state))
