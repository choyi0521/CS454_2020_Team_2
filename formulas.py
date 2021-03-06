import math


def jaccard(ep, ef, np, nf):
    return ef / (ef + nf + ep)


def ochiai(ep, ef, np, nf):
    if ef == 0:  # considering zero division error
        return 0
    return ef / math.sqrt((ef + nf) * (ef + ep))


def tarantula(ep, ef, np, nf):
    if ef == 0:  # considering zero division error
        return 0
    return (ef / (ef + nf)) / (ep / (ep + np) + ef / (ef + nf))


def ample(ep, ef, np, nf):
    return abs(ef / (ef + nf) - ep / (ep + np))


def wong1(ep, ef, np, nf):
    return ef


def wong2(ep, ef, np, nf):
    return ef - ep


def wong3(ep, ef, np, nf):
    if ep <= 2:
        h = ep
    elif 2 < ep <= 10:
        h = 2 + 0.1 * (ep - 2)
    else:
        h = 2.8 + 0.001 * (ep - 10)
    return ef - h


def op1(ep, ef, np, nf):
    if nf > 0:
        return -1
    return np


def op2(ep, ef, np, nf):
    return ef - ep / (ep + np + 1)
