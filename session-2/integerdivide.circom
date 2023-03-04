pragma circom 2.1.2;

template IntegerDivide(nBits) {
    assert(nBits <= 126);
    signal input dividend;
    signal input divisor;

    signal output remainder;
    signal output quotient;

    ///
}