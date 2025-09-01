from Ivar import call_name, act1_ivar, act2_ivar, act3_ivar
from madeleine import get_name, act1_madeleine, act2_madeleine, act3_madeleine
from Chris import call_name1, act1_chris, act2_chris, act3_chris
from sophie import bestname, act1_sophie, act2_sophie, act3_sophie
from kacper import name, act1_kacper, act2_kacper, act3_kacper
from Todd import member_name, act1_todd, act2_todd, act3_todd

print(f"This is Team zin er in. We are:")
print(get_name())
bestname()
call_name()
print(name())
print(call_name1())
print(member_name())

print("The story:")
for n in range(1, 4): 
    for person in ["madeleine", "sophie", "ivar", "kacper", "chris", "todd"]:
        func_name = f"act{n}_{person}"
        func = globals()[func_name]
        print(func())
