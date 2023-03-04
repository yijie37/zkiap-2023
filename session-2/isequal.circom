pragma circom 2.1.2;

include "iszero.circom"

// template IsEqual() {
//     signal input in[2];
//     signal output out;

//     out <-- in[0] - in[1] == 0 ? 1 : 0; // Will not be constrainted.
//     out * (out - 1) === 0;
//     in[0] * 0 === 0;
//     in[1] * 0 === 0;
// }

template IsEqual() {
    signal input in[2];
    signal output out;

    component isz = IsZero();

    isz.in <== in[1] - in[0]; // inputs: 1, GLOBAL_FIELD_P + 1; output: 1

    out <== isz.out;
}