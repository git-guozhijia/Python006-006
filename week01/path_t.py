import os
from pathlib import Path

p = Path()
print(p.absolute())
print(p.resolve())

path = "/Users/qtt/Desktop/git-guozhijia/week01/a.py.go"
p = Path(path)
print(p)
print(p.name)
print(p.stem)
print(p.suffix)
print(p.suffixes)
print(p.parent)
print(p.parents)
for i in p.parents:
    print(i)
print(p.parts)



print(f"os.path.abspath(__file__):{os.path.abspath(__file__)}")
print(f"os.path.basename(__file__):{os.path.basename(__file__)}")
print(f"os.path.dirname(os.path.abspath(__file__)):{os.path.dirname(os.path.abspath(__file__))}")
print(f"os.path.dirname(__file__):{os.path.dirname(__file__)}")
print(f"os.path.exists('random_t.py'):{os.path.exists('random_t.py')}")
print(f"os.path.isdir('random_t.py'):{os.path.isdir('random_t.py')}")
print(f"os.path.isfile('random_t.py'):{os.path.isfile('random_t.py')}")
print(f"os.path.join(os.path.dirname(__file__), os.path.basename(__file__)):{os.path.join(os.path.dirname(__file__), os.path.basename(__file__))}")



