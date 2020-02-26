from base64 import urlsafe_b64encode as b64encode
from hashlib import md5, sha1, sha256, sha512

from flask import Blueprint, request, jsonify

hash_bp = Blueprint('hash', __name__)

@hash_bp.route('/', methods=['GET'], strict_slashes=False)
def get_hash():
    q = request.args.get('q')
    if q is None:
        return jsonify(error="missing 'q' parameter.")

    if q is not None:
        md5_hash = md5(q.encode())
        sha1_hash = sha1(q.encode())
        sha256_hash = sha256(q.encode())
        sha512_hash = sha512(q.encode())
        d = {
            'md5': {
                'hex': md5_hash.hexdigest(),
                'base64': b64encode(md5_hash.digest()).decode()
            },
            'sha1':{
                'hex': sha1_hash.hexdigest(),
                'base64': b64encode(sha1_hash.digest()).decode()
            },
            'sha256': {
                'hex': sha256_hash.hexdigest(),
                'base64': b64encode(sha256_hash.digest()).decode() 
            },
            'sha512' : {
                'hex': sha512_hash.hexdigest(),
                'base64': b64encode(sha512_hash.digest()).decode()
            }
        }
        return jsonify(d)



