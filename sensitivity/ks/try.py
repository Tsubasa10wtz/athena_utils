from scipy.stats import ks_2samp

a = [1,1,1,1,1,1,1,1,1]
b = [1,1,1,1,1,1,1,2,2]

result = ks_2samp(a,b)
print(result.pvalue)