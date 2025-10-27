# a. P(Buy | Day = Weekday, Free Delivery = Yes, Discount = Yes)
p_a = calculate_conditional_probability('Weekday', 'Yes', 'Yes', 'Buy')

# b. P(Buy | Day = Weekday, Free Delivery = No, Discount = No)
p_b = calculate_conditional_probability('Weekday', 'No', 'No', 'Buy')

# c. P(Not Buy | Day = Weekday, Free Delivery = Yes, Discount = Yes)
p_c = calculate_conditional_probability('Weekday', 'Yes', 'Yes', 'Not Buy')
# Catatan: P(Not Buy | X) = 1 - P(Buy | X) (hanya jika Class adalah biner)
# Kita hitung ulang untuk memastikan konsistensi dan akurasi
# p_c_check = 1 - p_a

# d. P(Not Buy | Day = Weekday, Free Delivery = No, Discount = No)
p_d = calculate_conditional_probability('Weekday', 'No', 'No', 'Not Buy')
# p_d_check = 1 - p_b

# e. P(Buy | Day = Weekend, Free Delivery = Yes, Discount = Yes)
p_e = calculate_conditional_probability('Weekend', 'Yes', 'Yes', 'Buy')

# f. P(Buy | Day = Weekend, Free Delivery = No, Discount = No)
p_f = calculate_conditional_probability('Weekend', 'No', 'No', 'Buy')

# g. P(Not Buy | Day = Weekend, Free Delivery = Yes, Discount = Yes)
p_g = calculate_conditional_probability('Weekend', 'Yes', 'Yes', 'Not Buy')
# p_g_check = 1 - p_e

# h. P(Not Buy | Day = Weekend, Free Delivery = No, Discount = No)
p_h = calculate_conditional_probability('Weekend', 'No', 'No', 'Not Buy')
# p_h_check = 1 - p_f

# Tampilkan hasil (dibulatkan 4 angka di belakang koma)
results = {
    'a': p_a, 'b': p_b, 'c': p_c, 'd': p_d,
    'e': p_e, 'f': p_f, 'g': p_g, 'h': p_h
}

print("Hasil Perhitungan Probabilitas (dibulatkan 4 angka):")
print("-" * 40)
print(f"a. P(Buy | Weekday, FD=Yes, Disc=Yes):  {results['a']:.4f}")
print(f"b. P(Buy | Weekday, FD=No, Disc=No):    {results['b']:.4f}")
print(f"c. P(Not Buy | Weekday, FD=Yes, Disc=Yes): {results['c']:.4f}")
print(f"d. P(Not Buy | Weekday, FD=No, Disc=No):   {results['d']:.4f}")
print(f"e. P(Buy | Weekend, FD=Yes, Disc=Yes): {results['e']:.4f}")
print(f"f. P(Buy | Weekend, FD=No, Disc=No):   {results['f']:.4f}")
print(f"g. P(Not Buy | Weekend, FD=Yes, Disc=Yes):  {results['g']:.4f}")
print(f"h. P(Not Buy | Weekend, FD=No, Disc=No):    {results['h']:.4f}")
print("-" * 40)