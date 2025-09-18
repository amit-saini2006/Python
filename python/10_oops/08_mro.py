class A:
    label = "A: Base class"

class B(A):
    label = "B: Masala blend"

class C(A):
    label = "C: Herbel blend"

class D(B, C):
    pass

cup = D()
print(cup.label)
print(D.__mro__)