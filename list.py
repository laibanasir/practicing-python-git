colors = ['blue', 'orange', 'green', 'grey', 'red']
cars = ['bmw', 'mercedees']

#lists
#slicing
colors_choice = colors[1:4] #(upto 4 , 4 not included)

#append
colors.append('yellow')

#insert (needs index and element)
colors.insert(2, 'cyan')

#extend 
colors.extend(colors_choice)

#remove
colors.remove('yellow')

#reverse
colors.reverse()

#concatenation 
concatenate = colors + cars

#repetition
repeat = cars * 3 #['bmw', 'mercedees', 'bmw', 'mercedees', 'bmw', 'mercedees']