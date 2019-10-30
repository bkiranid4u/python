def foo(name, **kwds):
    return 'name' in kwds


foo(name='Kiran', **{'name': 'Srinika'})
