def toBinario(num):
    try:
        assert 0 < num <= 255
        if str(num).find(".")!=-1:
            raise Exception
    except:
        return -1
    return bin(num)[2:].zfill(8)

print(toBinario(22))
print(toBinario(129))
print(toBinario(255))
print(toBinario(345))
print(toBinario(22.5))
print(toBinario("Hola"))
print(toBinario(-2))
