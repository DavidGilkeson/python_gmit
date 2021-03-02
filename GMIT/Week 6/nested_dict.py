# Nested Dictionaries

level1 = {
  
  "var1" : 34,
  "module" : [ {
    
    "name" : "David",
    "grade" : 70
    
  }, {
    "name" : "John",
    "grade" : 89     
  }      
  ]
}

def displayModule(module):
  for x in module:
    print(module[x])
  
  
  
displayModule(level1)
  

  
  
  
  # Array or List to take in an argument 