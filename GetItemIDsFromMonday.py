from monday import MondayClient

print('Initializing Monday client...')
ApiFile = open("ApiKey.txt", 'r')
MondayApiKey = ApiFile.read()
ApiFile.close()
monday = MondayClient(MondayApiKey)

#Setting variables
my_board_id = input("Indsæt board ID fra Monday: ").strip() #RHG proceskatalog = 2603550432 #This is Mortens test board = 6533732620
my_group_id = input("Indsæt Group ID fra Monday: ").strip() #fx new_group37126 'new_group37126'

#This returns all ids from a group in a board as a list
def get_items_by_group(board_id, group_id):
    data = monday.groups.get_items_by_group(board_id, group_id, limit=500)
    # Extract and print names and ids
    #print(data)
    items = data['data']['boards'][0]['groups'][0]['items_page']['items']
    for item in items:
        print(f"Name: {item['name']} - ID: {item['id']}")
        #print(f"ID: {item['id']}")

    return items

itemsIDs = get_items_by_group(my_board_id, my_group_id)

newContent = ""
for line in itemsIDs:
    print(line)
    content = line["name"] + ";" + line["id"] + "\n"
    newContent =newContent + content

newFile = open("Items.csv", "w")
newFile.write(newContent)
newFile.close()