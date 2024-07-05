shopping_list = []

def add_item(shopping_list):
    item = input("Enter the name of item:")
    shopping_list.append(item)
    print(item, "added successfully")

def remove_item(shopping_list):
        item = input("Enter the name of the item")
        for item in shopping_list:
              if item:
                 shopping_list.remove(item)
                 return
        print(item, "not found!") 

def view_item(shopping_list):
     for item in shopping_list:
          if item:
               print("Item_name:", item)  
               return
     print(name, "not found!")  
                    
                 
              
       
              
    


        
        

