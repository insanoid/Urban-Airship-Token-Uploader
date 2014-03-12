Urban-Airship-Token-Uploader
============================

Simple python script to upload a JSON array of device tokens into your Urban Airship account.
```bash
$ python token_uploader.py tokens.json
```

where tokens.json would contain device tokens as a JSON Array.
```JSON
["<Device Token 1>","<Device Token 2>","<Device Token 3>"]
```

TODO
============================
- [ ] Logic to handle errors.
- [ ] Retrying in case of failure.
- [ ] Confirming with the server if the total count of the tokens is correct.
