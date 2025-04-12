import numpy as np

# parameters
n_emails = 10_000_000  # large number of emails for accuracy

# Step 1: Generate spam/non-spam labels
spam_flags = np.random.choice([1, 0], size=n_emails, p=[0.5, 0.5])  # 1 = spam, 0 = not spam

# Step 2: Assign "refinance" word appearance based on spam status
# For spam emails: 1% contain "refinance"
# For non-spam emails: 0.001% contain "refinance"
refinance_flags = np.zeros(n_emails, dtype=bool)
refinance_flags[spam_flags == 1] = np.random.rand((spam_flags == 1).sum()) < 0.01
refinance_flags[spam_flags == 0] = np.random.rand((spam_flags == 0).sum()) < 0.00001

# Step 3: Compute P(spam | refinance)
spam_given_refinance = (spam_flags[refinance_flags] == 1).sum() / refinance_flags.sum()
print(spam_given_refinance)
