from enum import Enum
import time


class EdMoveType(Enum):
    REMOVE = 0
    INSERT = 1
    SUBSTITUTE = 2
    PASS = 3


class EdMove:
    def __init__(self, type, letter):
        self.type = type
        self.letter = letter
        self.sub = ""
        self.index = 0

    def show(self, show_pass=False):
        if self.type == EdMoveType.SUBSTITUTE:
            print(self.type.name.lower(),
                  "(", self.letter, ", ", self.sub, ", ", self.index, ")", sep='')
        elif show_pass or self.type != EdMoveType.PASS:
            print(self.type.name.lower(),
                  "(", self.letter, ", ", self.index, ")", sep='')


class EdData:
    def __init__(self, x, y):
        self.p = []
        self.prep = []
        self.ed = 0
        self.x = x
        self.y = y
        self.last = None
        self.start_time = time.time()
        self.time = 0.0

    def complete_path(self):
        """
        Compute the path created with the markers and reverse
        """
        # Check if something need to be done
        if len(self.prep) != 0:
            # Finding the path (DP)
            (oldi, oldj) = self.prep[0]
            for k in range(1, len(self.prep)):
                (i, j) = self.prep[k]
                # Find difference between the locations
                di = oldi - i
                dj = oldj - j
                if di == 1 and dj == 1:  # TOPLEFT MOVE
                    self.add_pass(self.x[oldi])
                elif di == 1 and dj == 0:  # TOP MOVE
                    self.add_remove(self.x[oldi])
                elif di == 0 and dj == 1:  # LEFT MOVE
                    self.add_insert(self.y[oldj])
                oldi = i
                oldj = j

    def complete_reverse(self):
        """
        Reverse the path created with complete_path or add_remove/add_insert/add_pass
        """
        self.p.reverse()

    def complete_indexes(self):
        """
        Compute the indexes of self.p
        """
        index = 0
        for i in range(len(self.p)):
            self.p[i].index = index
            if self.p[i].type != EdMoveType.REMOVE:
                index += 1
        self.time = time.time() - self.start_time

    def add_marker(self, i, j):
        """
        Add a location marker, must be completed with complete_path(self)
        """
        self.prep.append((i, j))

    def add_remove(self, letter):
        """
        Add a remove operation
        """
        if self.last != None and self.last.type == EdMoveType.INSERT:
            n = self.last
            n.type = EdMoveType.SUBSTITUTE
            n.sub = n.letter
            n.letter = letter
        else:
            self.last = EdMove(EdMoveType.REMOVE, letter)
            self.p.append(self.last)
            self.ed += 1

    def add_insert(self, letter):
        """
        Add an insert operation
        """
        if self.last != None and self.last.type == EdMoveType.REMOVE:
            n = self.last
            n.type = EdMoveType.SUBSTITUTE
            n.sub = letter
        else:
            self.last = EdMove(EdMoveType.INSERT, letter)
            self.p.append(self.last)
            self.ed += 1

    def add_pass(self, letter):
        """
        Add a pass operation
        """
        self.last = EdMove(EdMoveType.PASS, letter)

        self.p.append(self.last)

    def show(self, show_pass=False):
        print("path =", self.prep)
        print("x =", self.x)
        print("y =", self.y)
        print("ED =", self.ed)
        for v in self.p:
            v.show(show_pass)
        print("Time = ", self.time, "s", sep="")
