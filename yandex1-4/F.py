def sort_second_level_keys(nested_dict):
    sorted_dict = {}
    for key, value in nested_dict.items():
        sorted_value = {k: v for k, v in sorted(value.items())}
        sorted_dict[key] = sorted_value
    return sorted_dict


file = open("input.txt", "r", encoding='utf-8')
x = file.readlines()
data = {}

for line in x:
  s = line.split()
  name, product, quantity = s[0], s[1], int(s[2])
  if name not in data:
    data[name] = {product: quantity}
  else:
    if product not in data[name]:
      data[name][product] = quantity
    else:
      data[name][product] += quantity


sorted_dict = dict(sorted(data.items()))
sorted_dict = sort_second_level_keys(sorted_dict)
for name in sorted_dict:
  print(name + ":")
  for product in sorted_dict[name]:
    print(product, sorted_dict[name][product])
