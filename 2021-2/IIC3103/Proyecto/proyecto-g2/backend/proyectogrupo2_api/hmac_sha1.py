import hashlib
import hmac
import base64
import sys
sys.path.append("..")
from proyectogrupo2.settings import env

DEV_O_PROD = env("DEV_O_PROD") # Puede ser "dev" o "prod"

if DEV_O_PROD == "dev":
    TOKEN_BODEGA = env('TOKEN_BODEGA_DEV')
else:
    TOKEN_BODEGA = env('TOKEN_BODEGA_PROD')

def hmac_sha1_64(message):
    key = bytes(TOKEN_BODEGA, 'UTF-8')
    message = bytes(message, 'UTF-8')
    digester = hmac.new(key, message, hashlib.sha1)
    signature1 = digester.digest()
    signature2 = base64.b64encode(signature1)
    
    return str(signature2, 'UTF-8')