class Parking:

    def __init__(self):
        self.my_parking = {}

    def register (self, username, licensePlateNumber):
        if username not in self.my_parking:
            self.my_parking[username] = licensePlateNumber
            return f"{username} registered {licensePlateNumber} successfully"
        return f"ERROR: already registered with plate number {licensePlateNumber}"

    def unregister (self, username):
        if username in self.my_parking:
            self.my_parking.pop(username)
            return f"{username} unregistered successfully"
        return f"ERROR: user {username} not found"

    def __repr__(self):
        result =''
        for username, licensePlateNumber in self.my_parking.items():
            result += f"{username} => {licensePlateNumber}"+'\n'
        return result

n=int(input())
parking = Parking()
for i in range (1, n+1):
    command = input()
    action, *data =command.split()
    if action =='register':
        name = data[0]
        pl_number = data[1]
        print (parking.register(name,pl_number))
    elif action =='unregister':
        name = data[0]
        print (parking.unregister(name))

print(parking)

