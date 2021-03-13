from az import *

resp, err = az_cli("az account list")

# tulostetaan koko json-rakenne
print("vm's: %s\n" % (resp))

# tulos resp on json-muotoa. Tulostetaan esimerkiksi kaikkien name
for x in resp:
    print("name: %s" % (x['name']))
