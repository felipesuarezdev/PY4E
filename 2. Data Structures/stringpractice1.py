str = "X-DSPAM-Confidence: 0.8475"

look_for_position = str.find(":")
print(look_for_position)

slice_the_str = (str[look_for_position+1:])
print(slice_the_str)

str_convert_to_float = float(slice_the_str)
print(str_convert_to_float)