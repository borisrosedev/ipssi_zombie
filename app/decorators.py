from functools import wraps
from flask import request, jsonify
# import logging 
# logger = logging.getLogger(__name__)
# logging.basicConfig(filename="decorators.log",level=logging.DEBUG)


def check_for_keys(*keys):
    print("----keys---------")
    print(keys)
    def check_body(fc):
        @wraps(fc)
        def content_analyzer(*args,**kwargs):
            data = request.get_json()
            for key in keys:
                print(key)
                if data.get(key) is  None:
                    return jsonify({"message": f"missing {key}"}), 400
            return fc(*args,**kwargs)
        return content_analyzer
    return check_body


