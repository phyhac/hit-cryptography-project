var pki = forge.pki;
var pemBankPublicKey = "-----BEGIN PUBLIC KEY-----\
MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAkXLAYu+vT/vcuXn5Mucq4Fl/rTvFV1VL6Eo15crLQ5CGvJBWkk5LxGyHnyrgxykdnhnqaJuKPezYP4SLfgpxlagQA8FavQJX5apWTQaLgEcIiDn8lLqUtrebwPM1IOQkIIWvP7vn32mZYTTT/7GK+KL+sHU/u8ZiqDK+zacOYrbmYlsx7PoXYOycWfPzhOmzXnp8YzNbYciPO7TcYDtHdytQR+tCwwGB07YuZZ4tFmBd0Vr+aqzW22CDg6GQJlt0Gu4Cj2kJFK0KCnzYzJjnwALQLRjCYs6Bxc6yufjoNfk6tUWl1z0EQ1MLvO8XyySzv0dr6XJurFZ+JztaFcTexwIDAQAB\
-----END PUBLIC KEY-----";

var pemBankPrivateKey = "-----BEGIN RSA PRIVATE KEY-----\
MIIEowIBAAKCAQEAkXLAYu+vT/vcuXn5Mucq4Fl/rTvFV1VL6Eo15crLQ5CGvJBWkk5LxGyHnyrgxykdnhnqaJuKPezYP4SLfgpxlagQA8FavQJX5apWTQaLgEcIiDn8lLqUtrebwPM1IOQkIIWvP7vn32mZYTTT/7GK+KL+sHU/u8ZiqDK+zacOYrbmYlsx7PoXYOycWfPzhOmzXnp8YzNbYciPO7TcYDtHdytQR+tCwwGB07YuZZ4tFmBd0Vr+aqzW22CDg6GQJlt0Gu4Cj2kJFK0KCnzYzJjnwALQLRjCYs6Bxc6yufjoNfk6tUWl1z0EQ1MLvO8XyySzv0dr6XJurFZ+JztaFcTexwIDAQABAoIBAGnwALyPA0vokI3vj1hKE2qxBVOx8zx2/gDE/JjQqlgdzmVNZCDQMlNxER8XZfzpr47WJWvnzjroZWFuMwOsq6prbK6viF2edVLsTEtx9u2Jz2cZhST2+RZUiXdyLUI1qTKe7FQpkuugyHyKs9bLBAOxBHyWCcPE7VrBC0RS5yFyI7XWJFvqQh+OaLBUSCdAlqQs7d8H4mNak3U/xdOcKyGG21X9oqgXKTZ4P713WaP8G5w1LR5BNPAQhgorkIoDpin/Dk+3wkmacGTgTBJQRaa4qZVxnlh7T3WVt+fpYkZVrmLB9tzCi2WatrPn+9ef3OVwR7dHwz9mOd3W9C226dECgYEA6tvF9WBTn7kD28aTKqjQgbNipJEA0JL8dw0jx/0L32Nb9kaeDgPIBjVofCeG0NpqlTbO6OAb5TaNWBBA8ujJj41uv3vpKdKIk0fwcr/PU1OEP11CkPmGGaV4cQNyANYgKATxVJGkSRQaRMZ8qFhrXcdzarsmhHXu5Ms4la0vL70CgYEAnoqNaogsliE39paiM1cfdWkLSFPS4RI84scNnVz2zQh7tyrhqaF+JPmQaVl1W6Mai01j3WdkvveGq6q3K4vInc4jBs1RddA87h+t9J47SZUaDLgi4sRT8AgyZuyBKhIjNT72mEOaz6unnoAfpxCq381jrLRScbsL6o5CGtM//tMCgYEAjHk9c2HVQsCn9SlV1vs4E4vXIXV1lkuEZDTgxPquwkOsuqZMXTeXyVbikvgVZBBwFaW9pn59UOELM7QtFN11yb4fkrqroI9Dj0xFHm1ptX5LqJbAfPQyaF6XpokYBDYO78DdE+c061zxxVcvMoYIWgQ1HY6pICtl40VGKAh5I8UCgYA9KZCC78PbqzcOz3AFxG+jeQHcRlJNeB67EjXDZrDjyokH0eg6681hcFHxAo0O7C56XUHQkWnBbnaq1XJSv1uG3ZaPsjfh7pMC/n+6piyTJ41kKMl0mG8VY+Ql5smxtEuW6BJ0DWi1AzDoKd+MMRbqvi7c2rgPnixrsbP461R99wKBgECq2KadxyWJPYRRt4rrPCxqQQIsVbkFtEp3Fvi7tVAeRiOUUqvoUE4w3HNQSgPbrD3FZAkmAukGi3r43Gi/OamtRLqaCu17oSQrTw2ilYoE8x2q327j9X2m40O4TpI57mMTeKuX87ugaHT75xGMFlKfN+UaO7Of1gxElxnTNAEd\
-----END RSA PRIVATE KEY-----";

var pemUserPublicKey = "-----BEGIN PUBLIC KEY-----\
MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAsw8BpTNLbPTNGMT/51CK\
iMc7v27UQLYgFfoyRN7ymcYpNvwCk/kS8pa/Fo0KpieVNu6j8yJSYeHfbs6E7O2b\
YVkfhA05ifmz1JSrZ4sJ7urC6YxNFLFatPwPBM7kH6Bis6aZOLKANdKat57XCnwa\
DfYAfbC0xkxXkBK83W3b42j3X2JTqLfJ7/lyyFcvrvrLYj4xvpzfOVwY2tl6BBFQ\
S7eb0Tgn8FZzjD2Y7rWLSprE0jzTxb3NkXuwV3uFcmfu1eii0F2n2LIQGBVL2mji\
3rb7AGZPPvxh0nSOx0mExmEEZCB2lEZQzDdt4M95WpWM4VRYlT1Y9J8x0OgFCM8T\
jwIDAQAB\
-----END PUBLIC KEY-----";

var pemUserPrivateKey = "-----BEGIN RSA PRIVATE KEY-----\
MIIEpAIBAAKCAQEAsw8BpTNLbPTNGMT/51CKiMc7v27UQLYgFfoyRN7ymcYpNvwC\
k/kS8pa/Fo0KpieVNu6j8yJSYeHfbs6E7O2bYVkfhA05ifmz1JSrZ4sJ7urC6YxN\
FLFatPwPBM7kH6Bis6aZOLKANdKat57XCnwaDfYAfbC0xkxXkBK83W3b42j3X2JT\
qLfJ7/lyyFcvrvrLYj4xvpzfOVwY2tl6BBFQS7eb0Tgn8FZzjD2Y7rWLSprE0jzT\
xb3NkXuwV3uFcmfu1eii0F2n2LIQGBVL2mji3rb7AGZPPvxh0nSOx0mExmEEZCB2\
lEZQzDdt4M95WpWM4VRYlT1Y9J8x0OgFCM8TjwIDAQABAoIBAAX0An/P8d2ql2E+\
WgmOCcdCZB/2UkD3cBPWnayDyLXOTHNniqLDuY7/7j1mECYHgiXIrEfak4tWS4MP\
PZwi+MSd+qtauZHrVZItPEt36E4XwAvyT6ljXwxOGuBFUhv1Qd53ND4CsUZepcwG\
hKWXgIBwgbxmPcrxRKaOVgTMdp1EiQNFXaUlnY/Ijr8+BuCmneVl4C5tQAUtGWPA\
wtGpHjLAPvZW0l9D7hN0eeGqabiYp7SZlmZuy5oxu9hvPEi1hZvhXPJSC/6w2Gje\
fvoHHPwLQtHaLkFeeyG8o9TUiDj7VivBpy+MD/qB7eQ0TOiSQXzzuaFoINK+AACC\
bYWQcAECgYEAuCZIbgAiOyxXAt1sV0sWcJNh1S1eMzE7lWuUWUluDomc2/4nBpqw\
Q5U6c6KaBdC/5XcxJ8oOKKq50C1T/ewammf5rLJDviPeKSCKmMdzyigLXcRyuXwf\
q8pDXDrh/wbz7845eokmSP70S+giZKrFlcKAUrgLTp5gDLKx0Y6N0cECgYEA+Ow3\
3e3tFEg2msAPYZpcJs/I6F3D+zZvopu0zecI9KhPsjvUSywQoA76vjW6e41mSXY8\
n1WmWP5P3OtUmpX7qz//hsY1dDcULcWvCF/T+T1kUFQ6qhuZGy0L+MjF3FdyIsp5\
GHEb/Be4EClLXon40tAd7jC6JvdeGKWd0tZvmU8CgYEAoHQ7CB31tbmc11I35Jf4\
pX7F8Ann2pM7Z6alTGc/Dku58bYyKv7+NuUAWWGE8yxBCKAipJjaXXTlEw9r8ASZ\
6ZBPbLqnbDW0jgFcwmKH8c2SmdFiZVxR/E3xA5wK7zwPsRPv4WU/hrsgAkPyM+TY\
5PTk+y6CK66z4lyRtBaSXAECgYEA567E2NUIoqYL3MECD/Ah8SXYcx5CuOCTyx9t\
i2+MEFtPwi6Zi1X6K1+F1eAgL7sOBzX7erm3WIFrR83pMvCCC4RHiuOVARP6vheO\
sBaxLvwLEBE1gPqq6HZm/Cmyr0DcxLD7QNqWF27kLHai5d05MM3v7bCAsp/ufrY3\
TPO1b1UCgYAn/MayunMzH5UdYBa3IrbvLzMABS7BY+knPlWm5UhoeEq45AJNEVoz\
1rMC5hSLTx4ud12MnrHA5pQ4YiuJcnLV5HoUSKarL+kY2Ds2Zvh9wTgBGLH+Sp0q\
No8Yz2+y3nQcQuyXEKaJcNTxzorqiMUL/qG+uJkRtNSGPrQu2sOoUQ==\
-----END RSA PRIVATE KEY-----";




var userPrivateKey = pki.privateKeyFromPem(pemUserPrivateKey);
var userPublicKey = pki.publicKeyFromPem(pemUserPublicKey);
var bankPrivateKey = pki.privateKeyFromPem(pemBankPrivateKey);
var bankPublicKey = pki.publicKeyFromPem(pemBankPublicKey);


function getSHA256InBase64(toSHA) {
    var toSHAInURI = encodeURIComponent(toSHA);
    var md = forge.md.sha256.create();
    md.update(toSHAInURI);
    return btoa(md.digest().bytes());
}

function getSHA256ToHex(toSHA) {
    var md = forge.md.sha256.create();
    md.update(toSHA);
    return md.digest().toHex();
}

function encryptToBase64(toEncrypt) {
    var toEncryptInURI = encodeURIComponent(toEncrypt);
    var ciphertext = bankPublicKey.encrypt(toEncryptInURI);
    return btoa(ciphertext);
}