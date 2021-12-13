# PyJWT encoding / decoding example

Run `./genkeys.sh` to create a private/public RSA key pair.
Then run `python3 jwt_test.py` to see if PyJWT correctly generates JWT and
decodes it.

# Troubleshooting

### Could not deserialize key data. The data may be in an incorrect format ..

Your RSA key may not be generated properly. If you are using your own key pair,
check `genkeys.sh`.

### TypeError: load_pem_private_key() missing 1 required positional argument...

Check `cryptography` package and upgrade it if it is older than v3.1.
```
pip3 list --outdated
pip3 install -U cryptography
```
