def addition(input_list):
    output=sum(input_list)
    return output

while True:
    input_values=input("Please enter a value to calculate else enter 'q' :")
    if input_values !='q':
        input_values=int(input_values)
        input_variable_list.append(input_values)
    else:
        break
print("input valriables are",input_variable_list)

output=addition(input_variable_list)
print("Output is ",output)