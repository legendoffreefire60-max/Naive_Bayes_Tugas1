import pandas as pd

# Total record dari soal
TOTAL_RECORDS = 30

# --- 1. Memasukkan Data Frekuensi ke dalam DataFrame ---

# Data Prior (Total Buy dan Not Buy)
# Total Buy = 19 + 5 = 24
# Total Not Buy (No) = 1 + 5 = 6
prior_data = {
    'Class': ['Buy', 'Not Buy'],
    'Count': [24, 6],
    'Prior Probability': [24/TOTAL_RECORDS, 6/TOTAL_RECORDS]
}
df_prior = pd.DataFrame(prior_data)

# Data Likelihood (Tabel Frekuensi Bersyarat)
# Disusun berdasarkan tabel yang ada pada gambar
likelihood_data = {
    'Feature': ['Discount=Yes', 'Discount=No',
                'Free Delivery=Yes', 'Free Delivery=No',
                'Day=Weekday', 'Day=Weekend', 'Day=Holiday'],
    'Buy_Count': [19, 5, 21, 3, 9, 7, 8],
    'No_Count': [1, 5, 2, 4, 2, 1, 3],
    # P(Feature | Buy) = Buy_Count / 24
    'P(Feature | Buy)': [19/24, 5/24, 21/24, 3/24, 9/24, 7/24, 8/24],
    # P(Feature | Not Buy) = No_Count / 6
    'P(Feature | Not Buy)': [1/6, 5/6, 2/6, 4/6, 2/6, 1/6, 3/6]
}
df_likelihood = pd.DataFrame(likelihood_data)

print("--- Data Prior P(Class) ---")
print(df_prior)
print("\n--- Data Likelihood P(Feature | Class) ---")
print(df_likelihood.round(4)) # Menampilkan 4 angka desimal
print("-" * 50)


# --- 2. Fungsi Naive Bayes untuk Perhitungan Probabilitas ---

def calculate_conditional_probability(day, free_delivery, discount, target_class):
    """
    Menghitung P(target_class | Day, Free Delivery, Discount)
    Menggunakan rumus Naive Bayes.
    """
    class_str = 'Buy' if target_class == 'Buy' else 'Not Buy'
    
    # Ambil Prior P(Class)
    prior = df_prior.loc[df_prior['Class'] == class_str, 'Prior Probability'].iloc[0]

    # Ambil Likelihood P(Feature | Class)
    P_day_given_class = df_likelihood.loc[df_likelihood['Feature'] == f'Day={day}', f'P(Feature | {class_str})'].iloc[0]
    P_fd_given_class = df_likelihood.loc[df_likelihood['Feature'] == f'Free Delivery={free_delivery}', f'P(Feature | {class_str})'].iloc[0]
    P_disc_given_class = df_likelihood.loc[df_likelihood['Feature'] == f'Discount={discount}', f'P(Feature | {class_str})'].iloc[0]

    # Hitung Pembilang (Numerator) = P(Class) * P(x1|Class) * P(x2|Class) * P(x3|Class)
    numerator_target = prior * P_day_given_class * P_fd_given_class * P_disc_given_class
    
    return numerator_target

# Fungsi untuk menghitung Posterior (P(Class | X))
def calculate_posterior(day, free_delivery, discount, target_class):
    # Hitung Pembilang untuk kedua kelas
    num_buy = calculate_conditional_probability(day, free_delivery, discount, 'Buy')
    num_not_buy = calculate_conditional_probability(day, free_delivery, discount, 'Not Buy')
    
    # Denominator (P(X)) = num_buy + num_not_buy
    denominator = num_buy + num_not_buy
    
    if denominator == 0:
        return 0.0 # Hindari ZeroDivisionError
    
    # P(Class | X) = Numerator / Denominator
    return num_buy / denominator if target_class == 'Buy' else num_not_buy / denominator

# --- 3. Perhitungan dan Penyajian Hasil dengan Pandas ---

scenarios = [
    # a. P(Buy | Day=Weekday, FD=Yes, Disc=Yes)
    ('a', 'Buy', 'Weekday', 'Yes', 'Yes'),
    # b. P(Buy | Day=Weekday, FD=No, Disc=No)
    ('b', 'Buy', 'Weekday', 'No', 'No'),
    # c. P(Not Buy | Day=Weekday, FD=Yes, Disc=Yes)
    ('c', 'Not Buy', 'Weekday', 'Yes', 'Yes'),
    # d. P(Not Buy | Day=Weekday, FD=No, Disc=No)
    ('d', 'Not Buy', 'Weekday', 'No', 'No'),
    # e. P(Buy | Day=Weekend, FD=Yes, Disc=Yes)
    ('e', 'Buy', 'Weekend', 'Yes', 'Yes'),
    # f. P(Buy | Day=Weekend, FD=No, Disc=No)
    ('f', 'Buy', 'Weekend', 'No', 'No'),
    # g. P(Not Buy | Day=Weekend, FD=Yes, Disc=Yes)
    ('g', 'Not Buy', 'Weekend', 'Yes', 'Yes'),
    # h. P(Not Buy | Day=Weekend, FD=No, Disc=No)
    ('h', 'Not Buy', 'Weekend', 'No', 'No'),
]

results = []
for index, target, day, fd, disc in scenarios:
    prob = calculate_posterior(day, fd, disc, target)
    results.append({
        'Soal': f'{index}. P({target} | Day={day}, Free Delivery={fd}, Discount={disc})',
        'Target Class': target,
        'Day': day,
        'Free Delivery': fd,
        'Discount': disc,
        'Probability': prob
    })

# Membuat DataFrame untuk hasil
df_results = pd.DataFrame(results)

print("\n--- Hasil Probabilitas Bersyarat (Naive Bayes) ---")
# Menampilkan kolom Soal dan Probabilitas, dibulatkan 4 angka
print(df_results[['Soal', 'Probability']].round(4))
print("-" * 50)