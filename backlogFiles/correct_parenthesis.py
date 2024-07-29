string = input("enter a string :")
print("input_string", string)
# print("string[-1]",string[-1])
output_string = ''
counter = 0
for i in string:
    # print("Index",i)
    # print("counter",counter)
    # print("length",len(string) )
    if counter < len(string) - 1:
        if string[counter] == "(":

            if string[counter + 1] == ")":
                corr_parenthesis = str(string[counter]) + str(string[counter + 1])
                output_string = output_string + corr_parenthesis

    counter = counter + 1

print("output_string", len(output_string))
