
batches = {
  "b1": 5,
  "b2":12,
  "b3":8  
}

orders = {
  "o1":2,
  "o2":8,
  "o3":2,
  "o4":5,
  "o5":9,
  "o6":5
}


expected_output = {
  "order_number":[],
  "batch_id" :[],
  "quantity":[]
}



for order, quanity in orders.items():
  while quanity > 0:
    if(sum(batches.values()) > 0):
      for batch , item in batches.items():
        if item > 0:  
          if item >= quanity:
            expected_output["order_number"].append(order)
            expected_output["batch_id"].append(batch)
            expected_output["quantity"].append(quanity)
            item = item - quanity
            quanity = 0
            batches.update({batch:item})
            orders.update({order:0})
            print(batches)
            break
            
          if item < quanity:
            expected_output["order_number"].append(order)
            expected_output["batch_id"].append(batch)
            expected_output["quantity"].append(item)
            quanity = quanity - item
            batches.update({batch:0})
            orders.update({order:quanity})
            print(batches)
    else:
      expected_output["batch_id"].append("Null")
      expected_output["quantity"].append("Null")
      quanity = 0     
      print(batches)
      print(batches)
      
    print(order,quanity)
    
            


print(expected_output)
          
        
    
  
  
  

