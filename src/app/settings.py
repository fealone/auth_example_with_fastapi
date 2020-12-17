import datetime

PRIVATE_PEM = open("app/certs/private_key.pem", "r").read()

TOKEN_EXPIRE = datetime.datetime.utcnow() + datetime.timedelta(minutes=60)

JWKS = {
    "keys": [
        {
            "alg": "RS256",
            "kid": "khxzn9sqxz7xx2kvljtzilznckgowpx6o1wthi5f",
            "n": "vT-gy8DXpqERHPISXXj9ZjleSeCnabcZ96LP4k9LiMyd3JSRLUPGNJ8_NckD-e_x_qK9LJfrTVAzXDV1HmIbq4zcb3lqWl-ZgroqeyhzlHnUuIKc1HpjOltXB3WNV0UMjT5gqyx_w79te8Jkd9BKxaFAQh1whnq2Bxsm9vE4rnRZh3JOrJ_UkEz7F8QCBwUlxBjLykkVYc3pkP_ZbXloaz0GEp5E90sk3W7HvYJEOjnJULrDghfdMdVvTjXU2-caOc064Nl6jK15cNOVZQktSnWVh0nkaWAh2XN7dy9wr_FTsWtn4NGpy7TvADleSoCTi46D3XmeVTG-ltBXi2br-Q",  # NOQA
            "use": "sig",
            "e": "AQAB",
            "kty": "RSA"
        }
    ]
}
