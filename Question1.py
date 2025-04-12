# Question1 
## Queueville Airlines knows that on average 5% of the people making flight reservations do not show up. (They model this information by assuming that each person independently does not show up with probability of 5%.) Consequently, their policy is to sell 52 tickets for a flight that can only hold 50 passengers. What is the probability that there will be a seat available for every passenger who shows up?

# Answer1  
'''
	Assume X as number of passengers who show up
	X ~ Binomial (n=52, p=0.95)
	Flight can only seat 50, so P(X <= 50)
	P(X<=50) = ∑_(k=0)^50▒〖(52¦k) 〖(0.95)〗^k 〖(0.05)〗^(52-k) 〗
	Approximation using normal distribution, if  X ~ Bin(n, p) then X = N(µ, σ2)
Where µ = np = 52 * 0.95 = 49.4
σ = √(np(1-p) ) = √(52*0.95*0.05) = 1.57
P(X <= 50) = P(Z <= (50 + 0.5 – 49.4)/1.57) = P(Z <= 1.1/1.57) = P(Z <= 0.70)
P(Z <= 0.70) ≈ 0.75
	Approximately 75% chance that everyone who shows up gets a seat. 
'''

import scipy.stats as stats
# Parameters
n = 52       # total tickets sold
p = 0.95     # probability of showing up
k = 50       # maximum number of passengers that can be seated

# Calculate exact probability using Binomial CDF
probability = stats.binom.cdf(k, n, p)
print(probability)
#Result : 0.7405
#Per binomial probability calculation above, there is a 74% chance that everyone who shows up will get a seat. 
