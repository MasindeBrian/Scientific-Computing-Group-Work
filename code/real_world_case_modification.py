"""3. Related Real-World Case Modification"""

import numpy as np

response_times = np.array([
    12, 18, 25, 10, 35, 22, 15, 40,
    17, 28, 20, 14, 31, 19, 26
])

average = np.mean(response_times)
minimum = np.min(response_times)
maximum = np.max(response_times)

print(f"Average response time: {average:.2f} minutes")
print(f"Fastest response: {minimum:.2f} minutes")
print(f"Slowest response: {maximum:.2f} minutes")
