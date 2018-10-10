import json
import logging

level = logging.INFO
log = logging.getLogger("Test")
fh = logging.FileHandler("app.log")
fh.setLevel(level)

fh.setFormatter(logging.Formatter("%(asctime)s - %(name)s: %(message)s"))
log.setLevel(level)
log.addHandler(fh)

log.debug("Hello from app")
log.info("Hello from app - INFO")
log.warn("Waring")

try:
    raise Exception()
except:
    log.exception("Error: %s" % "some error")

json_str = '{"id": 1, "friends": true, "name": "Ann", "address": {"city": "Kiev", "reg": "Obol"}}'

json_list = '[{"id": 1}, {}, 1.1]'

obj = json.loads(json_str)

# obj.address.city

# dct = json.loads(json_str)
# lst = json.loads(json_list)
# # print(dct["id"])
# print(lst[2], type(lst[2]))

# print(dct["friends"], type(dct["friends"]))
# print(lst, type(lst))

# print(json.loads("null"))


dumped = json.dumps({'id': 12})

print(dumped, type(dumped), json.loads(dumped))


class JsonObj:

    @classmethod
    def from_json(cls, json_str):
        dct = json.loads(json_str)
        return cls(**dct)

    def __init__(self, **kwds):
        for key, value in kwds.items():
            if isinstance(value, dict):
                setattr(self, key, JsonObj(**value))
            else:
                setattr(self, key, value)


obj = JsonObj(id=12, name="Ann")
print(obj.id, obj.name)

obj2 = JsonObj.from_json(json_str)

print(obj2.name, obj2.friends, obj2.address, type(obj2.address))
