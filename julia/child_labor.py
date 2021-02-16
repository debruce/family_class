from pprint import pprint
#import pprint

children = {
    "bobby": [ 3, 2, 1],
    "julie": "red trouble",
    "theo": 3,
    "luka": 1
}

pprint(children)
print(f"type of julie = {type(children['julie'])}")
print(f"type of theo = {type(children['theo'])}")
print(f"type of bobby = {type(children['bobby'])}")
print(f"type of bobby[0] = {type(children['bobby'][0])}")

# for k,v in children.items():
#     print(f"key={k}, value={v}")

# print(f"bobby = {children['bobby']}")
# print(f"luka = {children['luka']}")