def make_flat_json(nested_json):
    out = {}

    def flat(pairs, key=''):
        if type(pairs) is dict:
            for pair in pairs:
                flat(pairs[pair], key + pair + '.')
        elif type(pairs) is list:
            i = 0
            for pair in pairs:
                flat(pair, key + str(i) + '.')
                i += 1
        else:
            out[key[:-1]] = pairs

    flat(nested_json)
    return out
