def snake_to_camel(text: str) -> str:
    words = text.split('_')
    camel_case = words[0]


    for word in words[1:]:
        camel_case += word.capitalize()

    return camel_case

print(snake_to_camel('hello_world'))
print(snake_to_camel('my_variable_name'))
print(snake_to_camel('python'))
print(snake_to_camel('a_b_c_d'))