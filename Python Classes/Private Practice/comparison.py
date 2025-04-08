x: int = 2
y: float = 2.0
name: str = "Victor I"

cond1: bool = x > y
print("x>y:", cond1 )

cond2: bool = x < y
print("x<y:", cond2 )

cond3: bool = x <= y
print("x<=y:", cond3 ) 

cond4: bool = x >= y
print("x>=y:", cond4 )

cond5: bool = x == y
print("x==y:", cond5 )

cond6: bool = x != y
print("x!=y:", cond6 )

cond7: bool = name == "Victor I"
print("name==Victor I:", cond7 )

cond8: bool = x >= name
print("x>=name:", cond8 )
