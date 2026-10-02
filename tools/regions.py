"""The three retail releases of Pikmin (New Play Control!) and their disc versions.
"""
REGIONS = {
    'R9IE01': dict(label='New Play Control! Pikmin (USA)', short='USA', version=0),
    'R9IP01': dict(label='New Play Control! Pikmin (Europe)', short='Europe', version=0),
    'R9IJ01': dict(label='New Play Control! Pikmin (Japan)', short='Japan', version=0),
}

# retail DOL sizes, to give a clear error on someone else's modified dump
DOL_SIZES = {'R9IE01': 3531776, 'R9IP01': 3527488, 'R9IJ01': 3527104}
