# hook: WPADProbe, where it stores the extension type for its caller
# (`stw r0,0(r30)`, r0 = type, r30 = the caller's out pointer).  The game asks
# WPADProbe about the extension in many places and raises its "attach the Nunchuk"
# prompt for any type but 1, so a Classic Controller (type 2) has to read as a
# Nunchuk there too.  Every other type is stored as it is.
    cmplwi  0, 2
    bne     9f
    li      0, 1                        # Classic Controller -> Nunchuk
9:
    stw     0, 0(30)                    # displaced instruction
