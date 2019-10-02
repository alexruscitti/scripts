Basic semaphore management function.
Logs all semaphore acquire and release attempts, the function that called the
attempt, and the result. 

TODO:
1. Restructure semaphoreManager() as a class, with acquire and release
functions, instead of a function with a ton of input parameters that specify
acquisition or release.
2. Remake logging functionality in some way that is more readable.
