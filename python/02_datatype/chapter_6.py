chai_type = "Ginger chai"
customer_name = "Priya"

print(f"Oder for {customer_name} : {chai_type} please !")

chai_discription = "Aromatic and Bold"
print(f"First word: {chai_discription[0:5]}")
print(f"Last word: {chai_discription[12:]}")
print(f"Last word: {chai_discription[::-1]}") # reverse the string
# print(f"First word: {chai_discription[0:8:2]}")

label_text = "chai Spècial"
print(f"coded label: {label_text}")

ecoded_label = label_text.encode("utf-8")
print(f"Encoded label: {ecoded_label}")
decoded_label = ecoded_label.decode('utf-8')
print(f"Encoded label: {decoded_label}")