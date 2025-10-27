def calculate_unnormalized_posterior(day, free_delivery, discount, target_class):
    """
    Menghitung pembilang dari Naive Bayes (tanpa normalisasi P(X)):
    P(Class) * P(Day|Class) * P(FreeDelivery|Class) * P(Discount|Class)
    """
    class_str = 'Buy' if target_class == 'Buy' else 'No' # 'No' digunakan sebagai kunci untuk Not Buy di Likelihood
    
    # Prior Probability P(Class)
    prior = PRIOR_PROBABILITY[target_class]
    
    # Likelihoods P(Feature | Class)
    likelihood_day = LIKELIHOOD_DAY[day][class_str]
    likelihood_fd = LIKELIHOOD_FREEDELIVERY[free_delivery][class_str]
    likelihood_disc = LIKELIHOOD_DISCOUNT[discount][class_str]
    
    # Hasil perkalian: P(Class) * P(x1|Class) * P(x2|Class) * P(x3|Class)
    unnormalized_posterior = prior * likelihood_day * likelihood_fd * likelihood_disc
    
    return unnormalized_posterior

def calculate_conditional_probability(day, free_delivery, discount, target_class):
    """
    Menghitung probabilitas bersyarat P(target_class | Day, Free Delivery, Discount)
    menggunakan normalisasi.
    """
    # Hitung pembilang untuk Class: Buy
    numerator_buy = calculate_unnormalized_posterior(day, free_delivery, discount, 'Buy')
    
    # Hitung pembilang untuk Class: Not Buy
    numerator_not_buy = calculate_unnormalized_posterior(day, free_delivery, discount, 'Not Buy')
    
    # Denominator: P(X) = P(X|Buy)*P(Buy) + P(X|Not Buy)*P(Not Buy)
    # Ini sama dengan penjumlahan dari kedua pembilang
    denominator_px = numerator_buy + numerator_not_buy
    
    # Probabilitas bersyarat P(Class | X) = Numerator / Denominator
    if target_class == 'Buy':
        return numerator_buy / denominator_px
    else: # target_class == 'Not Buy'
        return numerator_not_buy / denominator_px