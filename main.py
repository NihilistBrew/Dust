ROOMS = []

CURRENT_ROOM = None


class Thing:
    def __init__(self, id, ref, name, desc):
        self.id = id
        self.ref = ref
        self.name = name
        self.desc = desc

    def __repr__(self):
        return f'{self.__class__.__name__}({self.id=!r}, {self.ref=!r}, {self.name=!r}, {self.desc=!r})'


class Room(Thing):
    def __init__(self, id, ref, name, desc, exits):
        super().__init__(id, ref, name, desc)
        self.exits = [self.get_room(token) for token in exits]
        self.intro = f'You entered {name}: {desc}'

        ROOMS.append(self)

    def __repr__(self):
        return super().__repr__()[:-1] + f', {self.exits=})'

    @staticmethod
    def get_room(token):
        if token is Room:
            return token
        for room in ROOMS:
            if (token is int or token.isdigit()) and room.id == int(token):
                return room
            elif token is str and (room.ref == token or room.name == token):
                return room
        else:
            return None

    def goto(self, room_token):
        room = Room.get_room(room_token)
        if room is not None:
            if room in self.exits:
                room.enter()
            else:
                print(f'Unable to reach room "{room.name}" from here!')
        else:
            print(f'Could not find room "{room_token}"!')
            return False

    def enter(self):
        print(self.intro)
        print(str(self))


vardagsrum = Room(1, 'vardagsrum', 'Vardagsrum', 'Mitt vardagsrum', 'hall')


