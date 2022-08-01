#############################
# linear
###########################
_4 = MemRef('_4', 8, 8)
_4.zero()

@parfor(ranges=(range(0, 8, 1), range(0, 1, 1), range(0, 8, 1)))
def body(_arg3, _arg1, _arg2):
    fma = FMAC(_arg3, _arg1, _arg2)
    _7 = _arg0[_arg1, _arg3]
    _8 = _3[_arg3, _arg2]
    _9 = _4[_arg3, _arg2]
    _10 = fma.Mul(_7, _8)
    _11 = fma.Add(_9, _10)
    _4[_arg3, _arg2] = _11
    _4[_arg3, _arg2] = fma.Result(copy=False)

_4.registers = np.vstack([_4.registers, _2.registers])
_4.registers = np.apply_along_axis(ReduceAdd, 0, _4.registers)[np.newaxis]
Copy(_4, _4)
#############################
# linear
###########################


#############################
# conv
###########################



_7 = MemRef('_7', 8, 2, 1, 1, )
_7.zero()

@parfor(ranges=(range(0, 8, 1), range(0, 1, 1), range(0, 2, 1), range(0, 1, 1), range(0, 1, 1),))
def body(_arg5, _arg1, _arg2, _arg3, _arg4):
    fma = FMAC(_arg5, _arg1, _arg2, _arg3, _arg4)
    for _arg6 in range(0, 3, 1):
        for _arg7 in range(0, 3, 1):
            _10 = _arg3 + _arg6
            _11 = _arg4 + _arg7
            _12 = _5[_arg1, _arg5, _10, _11]
            _13 = _1[_arg2, _arg5, _arg6, _arg7]
            _14 = _7[_arg5, _arg2, _arg3, _arg4]
            _15 = fma.Mul(_12, _13)
            _16 = fma.Add(_14, _15)
            _7[_arg5, _arg2, _arg3, _arg4] = _16
    _7[_arg5, _arg2, _arg3, _arg4] = fma.Result(copy=False)


_7.registers = np.vstack([_7.registers, _6.registers])
_7.registers = np.apply_along_axis(ReduceAdd, 0, _7.registers)[np.newaxis]
Copy(_7, _7)
#############################
# conv
###########################
