# Pascals Triangle Algo in Python
## This implementation compares and benchmarks a standard functional VS. optimized algorithm version

The element having a row index of r and column index of c can be derived as follows:
 * Input value for benchmark(num_rows) is the desired amount of rows for the Pascal's Triangle to be generated. (int AND >0)
 * A Pascal's triangle is a triangular array containing binomial coefficients: [https://en.wikipedia.org/wiki/Pascal%27s_triangle](https://en.wikipedia.org/wiki/Pascal%27s_triangle)
 * The commented code & Wiki article should make both code approaches (standard + optimized) comprehensible
 * The STANDARD version is quite intuitive as it creates the 2D array for the triangle row-by-row and each step is refactored into separate functions: calculating individual values --> combining them into rows --> combinings the rows into the final list.
 * The OPTIMIZED version makes use of some not so intuitive, but handy mathematical "knacks" to realise the same triangle with far less code by combining each row of the triangle with a left and right half (calculating // 2 and divmod(row_length,2)) which I commented in the code.
 * Both algorithm function call versions are embedded in a benchmark container function that starts & stops timers before & after each function execution. --> Benchmark results and timing differences are presented in the CLI!
 
 ## THE RESULT: turns out the optimized version is about 1.2x faster than the standard version! Try yourself!
