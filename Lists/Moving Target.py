class Target:
    def __init__(self, target_lst):
        self.target_lst = target_lst

    def shoot(self, index, power):
        if 0 <= index < len ( self.target_lst ):
            if self.target_lst[index] - power <= 0:
                self.target_lst.pop ( index )
            else:
                self.target_lst[index] -= power
        return self.target_lst

    def add(self, index, value):
        if 0 <= index < len ( self.target_lst ):
            self.target_lst.insert ( index, value )
        else:
            print ( "Invalid placement!" )
        return self.target_lst

    def strike(self, index, radius):
        if (index - radius >= 0) and (index + radius < len ( self.target_lst )):
            del self.target_lst[(index - radius):(index + radius + 1)]
        else:
            print ( "Strike missed!" )
        return self.target_lst


targets_lst = list ( map ( int, input ().split ( ' ' ) ) )
target = Target ( targets_lst )
while True:
    command = input ()
    if command == 'End':
        break
    action, index, power = command.split ( ' ' )
    if action == 'Shoot':
        targets_lst = target.shoot ( int ( index ), int ( power ) )
    elif action == 'Add':
        targets_lst = target.add ( int ( index ), int ( power ) )
    elif action == 'Strike':
        targets_lst = target.strike ( int ( index ), int ( power ) )

out_lst = ("|".join ( map ( str, targets_lst ) ))
print ( out_lst )

