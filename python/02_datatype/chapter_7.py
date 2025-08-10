# tuple

masala_spices = ('cardamon', 'cloves', 'cinnamon')

(spiece1 , spiece2, spice3) = masala_spices

print(f'main masala spieces: {spiece1}, {spiece2}, {spice3}')

ginger_ratio, cadramon_ratio = 2, 1
print(f"Ratio is G: {ginger_ratio} and C: {cadramon_ratio}")

ginger_ratio, cadramon_ratio = cadramon_ratio, ginger_ratio
print(f"Ratio is G: {ginger_ratio} and C: {cadramon_ratio}")

#membership

print(f"Is ginger in masala spieces? {"ginger" in masala_spices}")