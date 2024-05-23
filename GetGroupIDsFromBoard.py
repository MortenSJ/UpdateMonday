from monday import MondayClient

print('Initializing Monday client...')
ApiFile = open("ApiKey.txt", 'r')
MondayApiKey = ApiFile.read()
ApiFile.close()
monday = MondayClient(MondayApiKey)

#Setting variables
board_id = int(input("Indsæt board ID fra Monday: ").strip()) #RHG proceskatalog = 2603550432 #This is Mortens test board = 6533732620


#This returns all groups from a board in a list
def get_board_group_Ids(board_id):
    data = monday.groups.get_groups_by_board([board_id])

    group_ids = [group['id'] for board in data['data']['boards'] for group in board['groups']]
    return group_ids

newContent = str(get_board_group_Ids(board_id))

newFile = open("GroupIDs.txt", "w")
newFile.write(str(newContent))
newFile.close()