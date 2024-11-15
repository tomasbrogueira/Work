def A(m, n):
    if m == 0: return n + 1
    if m > 0 and n == 0: return A(m-1, 1)
    return A(m-1, A(m, n-1))


class Mem:
    def __init__(self):
        self.memory = {}
    
    def val(self, m, n):
        if (m, n) in self.memory:
            return self.memory[(m, n)]
        
        if m == 0:
            result = n + 1
        elif m > 0 and n == 0:
            result = self.val(m-1, 1)
        else:
            result = self.val(m-1, self.val(m, n-1))
        
        self.memory[(m, n)] = result
        return result
    
    def mem(self):
        mem_str = "{"
        for key, value in self.memory.items():
            mem_str += f"({key[0]}, {key[1]}): {value},\n"
        mem_str = mem_str[:-1] + "}"
        return mem_str
