#!/usr/bin/env python3
"""Semantic validator for the one-level difference-Karatsuba identity used by
public Yukon pinning PR #2114.

This does NOT benchmark CUDA. It independently checks the exact 256x256->512
integer recombination identity over boundary vectors and deterministic random
vectors before we consider composing the mechanism with another public spine.
"""
import random

MASK128=(1<<128)-1
MASK256=(1<<256)-1
MASK512=(1<<512)-1

def kmul256(a:int,b:int)->int:
    assert 0 <= a <= MASK256 and 0 <= b <= MASK256
    a0=a&MASK128; a1=a>>128
    b0=b&MASK128; b1=b>>128
    lo=a0*b0
    hi=a1*b1
    da=a0-a1
    db=b1-b0
    cross=lo+hi+da*db
    return (lo+(cross<<128)+(hi<<256))&MASK512

def check(a,b):
    got=kmul256(a,b)
    want=(a*b)&MASK512
    if got != want:
        raise AssertionError(f"mismatch a={a:x} b={b:x}\ngot ={got:x}\nwant={want:x}")

def main():
    edge=[0,1,2,(1<<32)-1,1<<32,(1<<64)-1,1<<64,(1<<127)-1,1<<127,
          (1<<128)-1,1<<128,(1<<128)+1,(1<<255)-1,1<<255,MASK256]
    count=0
    for a in edge:
        for b in edge:
            check(a,b); count+=1
    rng=random.Random(0x5153424b4d554c)
    for _ in range(20000):
        check(rng.getrandbits(256),rng.getrandbits(256)); count+=1
    print(f"PASS: {count} exact 256x256 Karatsuba identity cases")

if __name__=="__main__":
    main()
