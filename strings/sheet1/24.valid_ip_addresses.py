def valid_ip_addresses(s):
    def valid_part(part):
        return part != "" and len(part) <= 3 and (part == "0" or part[0] != "0") and 0 <= int(part) <= 255

    results = []
    n = len(s)
    for i in range(1, min(4, n - 2)):
        for j in range(i + 1, min(i + 4, n - 1)):
            for k in range(j + 1, min(j + 4, n)):
                p1, p2, p3, p4 = s[:i], s[i:j], s[j:k], s[k:]
                if valid_part(p1) and valid_part(p2) and valid_part(p3) and valid_part(p4):
                    results.append(".".join([p1, p2, p3, p4]))
    return results

result = valid_ip_addresses("25525511135")  # ['255.255.11.135', '255.255.111.35']
