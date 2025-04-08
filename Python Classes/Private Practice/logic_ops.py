bool1: bool = True
bool2: bool = False


cond1: bool = bool1 and bool2
cond2: bool = bool1 or bool2
cond3: bool = not bool2
cond4: bool = not (bool1 and bool2) or not (bool1 or bool2)