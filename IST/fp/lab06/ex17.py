def remove_dup(l):
    l_simp = []
    for val in l:
        if val not in l_simp:
            l_simp.append(val)
    return l_simp

def soma_dicionarios(d1,d2):
    simp_lord = {}
    st = set()
    for key1 in d1:
        st.add(key1)
    for key2 in d2:
        st.add(key2)
    for key in st:
        if key in d1 and key in d2:
            simp_lord[key] = remove_dup(d1[key] + d2[key])
            continue
        if key in d1:
            simp_lord[key] = d1[key]
        if key in d2:
            simp_lord[key] = d2[key]
    return simp_lord
        