def readFile(txtfile):
    with open(txtfile) as f:
        var = f.read()
        var = list(item for item in var.split("\n") if item.strip())
    return var
