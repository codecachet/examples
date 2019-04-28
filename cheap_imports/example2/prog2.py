import sys
from pprint import pprint

print(f'path={sys.path}')
pprint(sys.path)

sys.path.append('..')
pprint(sys.path)

import example1.mod1

print(f'example1.mod1.var1={example1.mod1.var1}')