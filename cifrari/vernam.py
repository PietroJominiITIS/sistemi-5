
a = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ ,.;:-_ò@çà#°ù§è[é+]*ì^\'=)(/&%$£""!\\|1234567890<>'
toa = {k: i for i, k in enumerate(a)}


def encrypt(msg, key):
    assert len(msg) <= len(key)
    return [toa[cm] + toa[ck] for cm, ck in zip(msg, key)]


def decrypt(msg, key):
    assert len(msg) <= len(key)
    return ''.join([
        a[(cm - ck) % len(a)] for cm, ck in zip(msg, map(lambda k: toa[k], key))
    ])


if __name__ == "__main__":
    MSG = 'abc :-)'
    KEY = 'keylong'
    assert MSG == decrypt(encrypt(MSG, KEY), KEY)
