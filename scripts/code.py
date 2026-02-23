q = 0.02
gen = 10  

file = open("CF_freq.txt", "w")


file.write("Generation\tFreq_c\tFreq_CC\tFreq_Cc\tFreq_cc\n")

for generation in range(1, gen + 1):

    p = 1 - q
    CC = p ** 2
    Cc = 2 * p * q
    cc = q ** 2

    file.write(f"\t{generation}\t\t{q:.5f}\t{CC:.5f}\t{Cc:.5f}\t{cc:.5f}\n")

    total_survivors = CC + Cc

    if total_survivors == 0:
        break

    freq_CC_new = CC / total_survivors
    freq_Cc_new = Cc / total_survivors


    q = (freq_Cc_new * 0.5)

file.close()