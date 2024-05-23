from monday import MondayClient

print('Initializing Monday client...')
ApiFile = open("ApiKey.txt", 'r')
MondayApiKey = ApiFile.read()
ApiFile.close()
monday = MondayClient(MondayApiKey)

#This updates the value for a specifik item, in a specific column on a specifik board.
def change_item_value(board_id, item_id, column_id, value):
    item_id = item_id
    print(f"Updating value...") #for {item_id} on board {board_id}
    monday.items.change_item_value(board_id,item_id,column_id,value)
    print("Update done!")
    
#file = open("UpdateMondayData\monday_data_v4.csv", "r+")
file = open("monday_data_v4.csv", "r+")

for line in file: 
    monday_item = line.split(",")
    board = monday_item[3]
    item = monday_item[5]
    column = monday_item[4]
    value = monday_item[2]
    if item == "" or value == "" or board == "BoardID":
        print("Skipping line...")
    else: 
        try: 
            change_item_value(board,item,column,value)
        except Exception:
            print("Der er sket en fejl med item: " + str(item))