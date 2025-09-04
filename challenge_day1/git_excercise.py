from Ivar import call_name, act1_33, act2_33, act3_33
from madeleine import get_teamname, get_name, act1_11, act2_11, act3_11
from Chris import call_name1, act1_55, act2_55, act3_55
from sophie import bestname, act1_22, act2_22, act3_22
from kacper import name, act1_44, act2_44, act3_44
from Todd import member_name, act1_66, act2_66, act3_66

print(get_teamname())
print(get_name())
bestname()
call_name()
print(name())
print(call_name1())
print(member_name())

print("The story:")
for n in range(1, 4): 
    for person in [11, 22, 33, 44, 55, 66]:
        func_name = f"act{n}_{person}"
        func = globals()[func_name]
        print(func())
