def logic_gate_outputs(a, b):
    and_output = a & b
    or_output = a | b
    xor_output = a ^ b
    return f"AND: {and_output}, OR: {or_output}, XOR: {xor_output}"

result = logic_gate_outputs(1, 0)  # AND: 0, OR: 1, XOR: 1
