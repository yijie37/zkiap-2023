pragma circom 2.1.2;

include "isequal.circom"
include "lessthan.circom"

template CalculateTotal(n) {
    signal input in[n];
    signal acc[n];
    signal output out;
    
    acc[0] <== in[0]
    for (var i = 1; i< n; i++) {
        acc[i] <== acc[i - 1] + in[i];
    }
    out <== acc[n - 1];
}

template Selector(nChoices) {
    signal input in[nChoices];
    signal input index;
    signal output out;

    component equals[nChoices];
    component total = CalculateTotal(nChoices);
    component lessThan = LessThan();

    for (var i = 0; i< nChoices; i++) {
        equals[i] = IsEqual();
        equals[i].in[0] <== i;
        equals[i].in[1] <== index;
        total.in[i] <== equals[i].out * i;
    }

    lessThan.in[0] <== index;
    lessThan.in[1] <== nChoices;
    
    out <== lessThan.out * total.out;
}