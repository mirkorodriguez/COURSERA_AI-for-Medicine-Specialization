import numpy as np

input_creatine=0.8
input_bilirubin=1.5
input_inr=1.3

# Coefficient values
coef_creatine = 0.957
coef_bilirubin = 0.378
coef_inr = 1.12
intercept = 0.643
# Calculate the natural logarithm of input variables
log_cre = np.log(input_creatine)
log_bil = np.log(input_bilirubin)
log_inr = np.log(input_inr)

# Compute output
meld_score = (coef_creatine * log_cre) +\
         (coef_bilirubin * log_bil ) +\
         (coef_inr * log_inr) +\
         intercept

# TODO: Multiply meld_score by 10 to get the final risk score
meld_score = meld_score*10

print (meld_score)
