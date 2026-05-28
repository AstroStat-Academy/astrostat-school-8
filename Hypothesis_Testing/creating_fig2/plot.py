import numpy as np
import scipy.stats as st
import matplotlib.pyplot as plt


sample_mean = -2
sample_sem = 3
model_mean = 3


x_plot = np.linspace(sample_mean - 5 * sample_sem, sample_mean + 5 * sample_sem, 100)

diff = abs(sample_mean - model_mean)
xx_before = np.linspace(sample_mean - 5 * sample_sem, sample_mean - diff, 100)
xx_after = np.linspace(sample_mean + diff, sample_mean + 5 * sample_sem, 100)

mean_distribution = st.norm(sample_mean, sample_sem)
y_plot = mean_distribution.pdf(x_plot)


left = sample_mean - np.abs(sample_mean - model_mean)
right = model_mean

plt.figure(figsize=(8,2))
plt.fill_between(xx_before, mean_distribution.pdf(xx_before), 0, color="b", ec="none", alpha=0.3, label="Area more extreme")
plt.fill_between(xx_after, mean_distribution.pdf(xx_after), 0, color="b", ec="none", alpha=0.3)
plt.plot(x_plot, y_plot, "k-", lw=2, label="N(mean, sem)")
#plt.axvline(sample_mean, ls="-", color="b", label="Sample mean")

plt.axvline(right, ls="--", lw=2, color="b", label="Model mean")
plt.axvline(left, ls="--", lw=2, color="b", label="Model mean")


plt.annotate('critical value', xy=(right+0.2,0.1), xytext=(right+2.4,0.12),arrowprops=dict(facecolor='black', arrowstyle='->'),ha='left')
plt.annotate('critical value', xy=(left-0.2,0.1), xytext=(left-2.4,0.12),arrowprops=dict(facecolor='black', arrowstyle='->'),ha='right')

plt.annotate(r'$\alpha/2$', xy=(right+0.8,0.02), xytext=(right+2.4,0.042),arrowprops=dict(facecolor='black', arrowstyle='->'),ha='left')
plt.annotate(r'$\alpha/2$', xy=(left-0.8,0.02), xytext=(left-2.4,0.042),arrowprops=dict(facecolor='black', arrowstyle='->'),ha='right')


#plt.legend(loc="upper left")
plt.gca().set_axis_off()
plt.ylim(ymin=0.0)
plt.xlabel(r"$\log M\ [M_\odot]$")
plt.ylabel("PDF of the sample mean")
plt.savefig('critical_pvalue.png')
