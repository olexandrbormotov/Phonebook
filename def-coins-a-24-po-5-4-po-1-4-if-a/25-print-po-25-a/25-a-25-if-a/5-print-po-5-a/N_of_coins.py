def coins(a):
    """
    >>>24
    po 5 4
    po 1 4
    """
    if a/25:
        print 'po 25 ', a/25
    a %= 25
    if a/5:
        print 'po 5 ', a/5
    a %= 5
    if a:
        print 'po 1 ', a
