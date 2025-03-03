
A = {"a", "b", "c", "d", "f", "g"}
B = {"b", "c", "h", "i", "j", "k", "l", "m", "o"}
C = {"c", "d", "f", "h", "j"}


elements_in_A_and_B = A & B
print("Elements in both A and B:", elements_in_A_and_B, "=> Total:", len(elements_in_A_and_B))


elements_only_in_B = B - (A | C)
print("Elements in B but not in A or C:", elements_only_in_B)



set_i = (B - A) & (B - C)
print("i:", set_i)


set_ii = A & C
print("ii:", set_ii)


set_iii = (A & B) | (B & C)
print("iii:", set_iii)


set_iv = (A & C) - B
print("iv:", set_iv)


set_v = A & B & C
print("v:", set_v)


set_vi = B - (A | C)
print("vi:", set_vi)
