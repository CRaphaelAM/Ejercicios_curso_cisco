class A:
    pass

class F(A):
    pass

class G(F):
    pass

class B(A):
    pass

class C(G):
    pass

class D(B,C):
    pass

print(D.mro())