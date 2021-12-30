
ch = '*'
ran = 30

def listing(module,verbose=True):
    if verbose:
        print(ch * ran)
        print('{}---{}'.format(module.__name__, module.__file__))
        print( ch * ran)

    count = 0
    for attr in module.__dict__:
        print('%-2d) %s'%(count, attr),end = ' ')
        if str(attr).startswith('__'):
            print('<built-in-name>')
        else:
            print(getattr(module, str(attr)))
        count += 1

    if verbose:
        print(ch * ran)
        print('{} has {} attributes'.format(module.__name__, count))
        print( ch * ran)

if __name__ == '__main__':
    import test1
    import test2
    listing(test1)
    listing(test2)