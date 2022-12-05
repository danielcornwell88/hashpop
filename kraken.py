def kraken(m="", string="", s="", random_salt=False, algorithm="", crack_hash=""):
    # create a new hash
    if m == 1:
        h = hashlib.pbkdf2_hmac(algorithm, string, s, 800000, dklen=None)
        return s, h
    if m == 2:
        f = open("dictionary", "r")
        for l in f:
            if crack_hash == hashlib.md5(encode(l)):
                return 'md5', l.strip('\n')
            if crack_hash == hashlib.sha1(encode(l)):
                return 'sha1', l.strip('\n')
            if crack_hash == hashlib.sha224(encode(l)):
                return 'sha224', l.strip('\n')
            if crack_hash == hashlib.sha256(encode(l)):
                return 'sha256', l.strip('\n')
            if crack_hash == hashlib.sha384(encode(l)):
                return 'sha384', l.strip('\n')
            if crack_hash == hashlib.sha512(encode(l)):
                return 'sha512', l.strip('\n')
            if crack_hash == hashlib.blake2b(encode(l)):
                return 'blake2b', l.strip('\n')
        return 'Did not crack'


if __name__ == "__main__":
    import hashlib