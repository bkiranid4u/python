""""
Draw English ruler using the recursive functions
"""

def draw_line(tick_length, tick_label=""):
    line = '-' * tick_length
    if tick_label:
        line += ' ' + tick_label
    print(line)

def draw_interval(centerLength):

    if centerLength > 0:
        draw_interval(centerLength - 1)
        # Execution will not go beyond this point until the base case is reached. once th base case reached the execution control moves to the next line 
        draw_line(centerLength)
        draw_interval(centerLength - 1)

# Identify the pattern of the call

def draw_ruler(num_inches, major_length):

    draw_line(major_length, '0')
    for j in range(1,num_inches+1):
        draw_interval(major_length-1)
        draw_line(major_length, str(j))

draw_ruler(2,5)
