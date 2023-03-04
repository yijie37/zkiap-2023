pragma circom 2.1.2;

include "num2bits.circom"

template LessThan() {
    signal input in[2];
    signal output out;

    component bits = Num2Bits(253);

    bits.in <== in[0]+ (1<<252) - in[1];

    out <== 1 - bits.out[252];
}

// LessThan extension 1
template LessThan1(n) {
    assert(n <= 252);
    signal input in[2];
    signal output out;

    component bits = Num2Bits(n+1);

    bits.in <== in[0]+ (1<<n) - in[1];

    out <== 1 - bits.out[n];
}

// LessThan extension 2: LessEqThan
template LessEqThan2(n) {
    signal input in[2];
    signal output out;

    component lt= LessThan(n+1);

    lt.in[0] = in[0];
    lt.in[1] = in[1] + 1;
    out <== lt.out;
}