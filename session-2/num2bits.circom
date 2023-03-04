pragma circom 2.1.2;

template Num2Bits(nBits) {
    signal input in;
    signal output out[nBits];
    var acc;
    var base = 1;

    for (var i = 0; i< nBits; i++) {
        out[i] <-- (in >> i) % 2;
        out[i] * (out[i] - 1) === 0;
        acc += out[i] * base;
        base += base;
    }
    acc === in;
}