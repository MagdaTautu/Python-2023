def validate_dict(rules, dictionary):
    for key, prefix, middle, suffix in rules:
        if key in dictionary:
            value = dictionary[key]
            if not value.startswith(prefix):
                return False
            if middle not in value[1:-1]:
                return False
            if not value.endswith(suffix):
                return False
        else:
            return False
    return True


rules = {("key1", "", "inside", ""), ("key2", "start", "middle", "winter")}
data = {
    "key1": "come inside, it's too cold out",
    "key2": "start the middle of winter",
    "key3": "this is not valid"
}

result = validate_dict(rules, data)
print(result)  
