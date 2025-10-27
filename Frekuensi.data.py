# Total record
TOTAL_RECORDS = 30

# Frekuensi P(Buy) dan P(Not Buy)
# Kita bisa hitung dulu total Buy dan Not Buy
# Dari tabel Discount: Buy = 19 + 5 = 24. No = 1 + 5 = 6. (TOTAL = 30)
PRIOR_PROBABILITY = {
    'Buy': 24 / TOTAL_RECORDS,
    'Not Buy': 6 / TOTAL_RECORDS
}
# P('Buy') = 24/30 = 0.8
# P('Not Buy') = 6/30 = 0.2

# Frekuensi Bersyarat (Likelihood) P(Feature | Class)
# P(Feature | Buy) dan P(Feature | Not Buy)

# 1. Discount
LIKELIHOOD_DISCOUNT = {
    'Yes': {'Buy': 19 / 24, 'No': 1 / 6},  # P(Discount=Yes | Buy), P(Discount=Yes | No)
    'No': {'Buy': 5 / 24, 'No': 5 / 6}   # P(Discount=No | Buy), P(Discount=No | No)
}

# 2. Free Delivery
LIKELIHOOD_FREEDELIVERY = {
    'Yes': {'Buy': 21 / 24, 'No': 2 / 6}, # P(Free Delivery=Yes | Buy), P(Free Delivery=Yes | No)
    'No': {'Buy': 3 / 24, 'No': 4 / 6}   # P(Free Delivery=No | Buy), P(Free Delivery=No | No)
}

# 3. Day
LIKELIHOOD_DAY = {
    'Weekday': {'Buy': 9 / 24, 'No': 2 / 6}, # P(Day=Weekday | Buy), P(Day=Weekday | No)
    'Weekend': {'Buy': 7 / 24, 'No': 1 / 6}, # P(Day=Weekend | Buy), P(Day=Weekend | No)
    'Holiday': {'Buy': 8 / 24, 'No': 3 / 6}  # P(Day=Holiday | Buy), P(Day=Holiday | No)
}

# Untuk kemudahan perhitungan P(Not Buy | ...)
# P(Not Buy | Day=X, FD=Y, Disc=Z) = 1 - P(Buy | Day=X, FD=Y, Disc=Z) TIDAK BERLAKU
# karena ini adalah probabilitas bersyarat, bukan biner.
# Kita akan hitung P(Not Buy | X, Y, Z) menggunakan Bayes' Theorem juga.
# Note: Kolom 'No' pada tabel merepresentasikan P(X | Not Buy) (karena totalnya 6),
#       bukan P(X | Buy) (total 24).