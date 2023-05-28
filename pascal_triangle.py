from time import time

def print_pascal_triangle(num_rows: int, triangle, optimized = False): #OUTER FUNCTION: Calls generate_pascal_triangle [optimized + standard] + Prints 2D triangle array -> R: delta_t_opti
    start_time = time() #Starts timer for triangle generation + complete print out of pascal triange!
    if optimized: #Calls and prints either optimized or standard pascal triangle function
        print("\n" + " OPTIMIZED ".center((len(triangle[-1])*4) + 2,"=")) #Start with \n
    else:
        print("\n" + " STANDARD ".center((len(triangle[-1])*4) + 2,"=")) #Start with \n
    print("row_idx:")
    for row_idx in range(num_rows): #Iterates through row indices == triangle row indices
        print(f"{row_idx} {'  ' * (num_rows-1 - row_idx)}",end = "") #Prints preceeding idx and spacer of "2X" without \n
        for col_idx in range(row_idx + 1): #Iterates from 0 to col_idx == row_idx(incl.) --> BECAUSE col_idx of last element of current triangle row == row_idx!
            print(f"{triangle[row_idx][col_idx]:<4}", end="") #IMPLEMENT artificial delay timer for visual live building!!!
        print()#END of line \n after ROW(row_idx) is completed.
    tri_width = ((len(triangle[-1])*4) + 2)
    print(f"{tri_width * '-'}") #Foundation of triangle

    #TIME STATS for function execution:
    end_time_opti = time() #Takes time stamp after complete triangle construction and printouts for benchmarking.
    delta_t_opti = (end_time_opti - start_time)
    print(">" + " TIME ELAPSED: ".center((len(triangle[-1])*4),"=") + "<") #Header for timings
    print(">" + f" {(delta_t_opti) * 1000:.4f} msec ".center((len(triangle[-1])*4),"=") + "<" + "\n") #Measure delta-time for start_time2 and end_time_optimized.
    return delta_t_opti

#STANDARD VERSION CONSISTS OF 3x CHAINED FUNCTIONS:
def generate_pascal_triangle(num_rows: int) -> list[list[int]]: #Returns 2D triangle list -> Chains 3x funcs!
    ###num_rows data check - start!
    if not isinstance(num_rows, int):
        raise TypeError("The input value of 'num_rows' should be 'int'")
    if num_rows == 0:
        return []
    elif num_rows < 0: #neg. int
        raise ValueError("The input value of 'num_rows' should be greater than or equal to 0")
    ###num_rows data check - ends!

    triangle: list[list[int]] = [] #Creates empty triangle list = [].
    for current_row_idx in range(num_rows): #row_idx starts at 0 to num_rows - 1
        current_row = populate_current_row(triangle, current_row_idx) #Assigns complete row list to current_row
        triangle.append(current_row) #Embeds current_row list as 2nd level list inside outer triangle list. --> 2D list array
    return triangle #Returns completed 2D pyramid list for all rows.

def populate_current_row(triangle: list[list[int]], current_row_idx: int) -> list[int]: #Returns current_row = [] for current_row_idx --> current_row_idx one ahead of triangle max_idx
    current_row = [-1] * (current_row_idx + 1) #Placeholder list [-1,-1,-1,...,-1] --> len(num_rows)
    # first and last elements of current row are equal to 1
    current_row[0], current_row[-1] = 1, 1
    for current_col_idx in range(1, current_row_idx): #Iterates through current_row[1:-1] -> Exclusive outer 1's
        calculate_current_element(triangle, current_row, current_row_idx, current_col_idx) #len(triangle) == current_row_idx
    return current_row #Returns 1D list array as current_row

def calculate_current_element(triangle: list[list[int]], current_row: list[int], current_row_idx: int, current_col_idx: int) -> None:
    above_to_left_elt = triangle[current_row_idx - 1][current_col_idx - 1]
    above_to_right_elt = triangle[current_row_idx - 1][current_col_idx]
    current_row[current_col_idx] = above_to_left_elt + above_to_right_elt

#OPTIMIZED VERSION IN ONE FUNCTION:
def generate_pascal_triangle_optimized(num_rows: int) -> list[list[int]]: #Returns Triangle 2D list array
    #INPUT CHECKS for num_rows ensuring --> type:int AND num_rows > 0 
    if not isinstance(num_rows, int):
        raise TypeError("The input value of 'num_rows' should be 'int'")
    if num_rows == 0:
        return []
    elif num_rows < 0:
        raise ValueError("The input value of 'num_rows' should be greater than or equal to 0")
    #MAIN TRIANGLE ALGORITHM
    result: list[list[int]] = [[1]] #Creates 2D list with first element: [1]
    for row_index in range(1, num_rows): #Starts from row_index = 1 to last row_idx incl!! --> row_idx == triangle__max_idx + 1 (one idx ahead)
        #Preparing variables for triangle algorithm
        temp_row = [0] + result[-1] + [0] #Temp row from result[row-idx - 1] to help constructing current_row --> last result list + framing 0's
        row_length = row_index + 1 #Shifts row_idx to abs row length --> row_length + 1 = len(temp_row)
        distinct_elements = sum(divmod(row_length, 2)) #Divmod: tuple(float, remainder) -> sum(divmod_tuple) == no. of distinct elements
        
        #Calculating and adding first and second halves for triangle row [current row_idx] --> Appending it to 2D result list array.
        row_first_half = [temp_row[i - 1] + temp_row[i] for i in range(1, distinct_elements + 1)] #list comprehension of first half row
        #-> Since all distinct elements are in first half (incl. mid element(1 or 2)) --> range iterates through distinct elements to calculate each
        row_second_half = row_first_half[: (row_index + 1) // 2] #Slices first half list either excl. mid element (odd row length) or exact half (even row length)
        row_second_half.reverse() #Mirrors second half list slice (excl. mid element for odd row length) OR exact mirror for even row lengths.
        row = row_first_half + row_second_half #Adds both list components into current row list.
        result.append(row) #2D list appending of newly built row list into outer result list --> result = [...,[prev_row],[row]]
    return result #Returns result list (2D array)

def benchmark(num_rows): #Final comparison summary between normal and optimized Pascal triangle algorithms:
    std_triangle = generate_pascal_triangle(num_rows)
    opt_triangle = generate_pascal_triangle_optimized(num_rows)
    tri_width = len(opt_triangle[-1])*4 + 2
    print("\n" + f"{tri_width * '*'}" + "\n" + " BENCHMARKING ".center(tri_width, "*") + "\n" + f"{tri_width * '*'}")

    std_time = print_pascal_triangle(num_rows, std_triangle, False) #Generates, prints STANDARD pascal triangle algorithm --> Returns delta execution time
    opt_time = print_pascal_triangle(num_rows, opt_triangle, True) #Generates, prints OPTIMIZED pascal triangle algorithm --> Returns delta execution time
    
    print(">>> RESULT: ", end = "")
    if opt_time < std_time:
        print(f"OPTIMIZED algorithm ({opt_time * 1000 :.4f}ms) is about {round((std_time/opt_time),1)}x faster than STANDARD algorithm ({std_time * 1000 :.4f}ms)")
    else:
        print(f"STANDARD algorithm ({std_time * 1000 :.4f}ms) is about {round((opt_time/std_time),1)}x faster than OPTIMIZED algorithm ({opt_time * 1000 :.4f}ms)")
    print()

if __name__ == "__main__":
    benchmark(9)