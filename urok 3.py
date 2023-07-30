def manipulate_string(input_string):
    if len(input_string) < 2:
        return ""

    return input_string[:2] + input_string[-2:]

# Test cases
sample_string_1 = 'helloworld'
result_1 = manipulate_string(sample_string_1)
print(f"Sample String: '{sample_string_1}'")
print(f"Expected Result: 'held'")
print(f"Actual Result: '{result_1}'")
print()

sample_string_2 = 'my'
result_2 = manipulate_string(sample_string_2)
print(f"Sample String: '{sample_string_2}'")
print(f"Expected Result: 'mymy'")
print(f"Actual Result: '{result_2}'")
print()

sample_string_3 = 'x'
result_3 = manipulate_string(sample_string_3)
print(f"Sample String: '{sample_string_3}'")
print(f"Expected Result: Empty String")
print(f"Actual Result: '{result_3}'")
