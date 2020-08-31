# Programming for the Puzzled -- Srini Devadas
# You Will All Conform
# Input is a vector of F's and B's, in terms of forwards and backwards caps
# Output is a set of commands (printed out) to get either all F's or all B's
# Fewest commands are the goal

def pleaseConform(caps):
    # Initialization
    start = 0
    forward = 0
    backward = 0
    intervals = []

    # Concatenate 'END', so that no need to add the last interval after for loop completes execution
    caps = caps + ['END']

    # Determine intervals where caps are on in the same direction
    for i in range(1, len(caps)):
        if caps[start] != caps[i]:
            # each interval is a tuple with 3 elements (start, end, type)
            intervals.append((start, i - 1, caps[start]))

            if caps[start] == 'F':
                forward += 1
            else:
                backward += 1
            start = i

    ##    print (intervals)
    ##    print (forward, backward)
    if forward < backward:
        flip = 'F'
    else:
        flip = 'B'
    for t in intervals:
        if t[2] == flip:
            if t[0] == t[1]:
                print('Person at position', t[0], 'flip your caps!')
            else:
                print('People in positions', t[0],
                  'through', t[1], 'flip your caps!')

def pleaseConformOnepass(caps):
    caps = caps + [caps[0]]
    for i in range(1, len(caps)):
        if caps[i] != caps[i-1]:
            if caps[i] != caps[0]:
                print('People in positions', i, end='')
            else:
                print(' through', i-1, 'flip your caps!')

caps = ['F', 'F', 'B', 'B', 'B', 'F', 'B',
        'B', 'B', 'F', 'F', 'B', 'F']
cap2 = ['F', 'F', 'B', 'B', 'B', 'F', 'B', 'B', 'B', 'F', 'F', 'F', 'F']


pleaseConform(caps)
pleaseConformOnepass(caps)
##pleaseConform(cap2)