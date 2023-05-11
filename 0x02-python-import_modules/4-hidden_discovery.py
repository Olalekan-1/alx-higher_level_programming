import dis
def print_names(module):
    code = module.__code__
    names = []
    for i in code.co_consts:
        if isinstance(i, str) and not i.startswith('__'):
            names.append(c)
    names.sort()
    for name in names:
        print(name)

module = __import__('hidden_4')
print_names(module)
