from csp import *
import timeit

easy_puzzle_1 = [[  '*'  ,[14,''],[ 6,''],  '*'  ,  '*'  ,  '*'  ],
				 [['',14],  '_'  ,  '_'  ,[ 8,''],  '*'  ,  '*'  ],
				 [['', 8],  '_'  ,  '_'  ,  '_'  ,[14,''],[ 4,'']],
				 [  '*'  ,  '*'  ,['',18],  '_'  ,  '_'  ,  '_'  ],
				 [  '*'  ,  '*'  ,  '*'  ,['', 6],  '_'  ,  '_'  ]]

medi_puzzle_1 = [[  '*'  ,[16,''],[ 8,''],[21,''],  '*'  ,  '*'  ],
				 [['',23],  '_'  ,  '_'  ,  '_'  ,  '*'  ,  '*'  ],
				 [['',14],  '_'  ,  '_'  ,  '_'  ,[16,''],[17,'']],
				 [  '*'  ,  '*'  ,['',18],  '_'  ,  '_'  ,  '_'  ],
				 [  '*'  ,  '*'  ,['',23],  '_'  ,  '_'  ,  '_'  ]]

medi_puzzle_2 = [[  '*'  ,  '*'  ,  '*'  ,[38,''],[ 3,''],  '*'  ,  '*'  ,  '*'  ],
				 [  '*'  ,[23,''],[10,10],  '_'  ,  '_'  ,[39,''],  '*'  ,  '*'  ],
				 [['',17],  '_'  ,  '_'  ,  '_'  ,  '_'  ,  '_'  ,[10,''],  '*'  ],
				 [['',20],  '_'  ,  '_'  ,  '_'  ,['',11],  '_'  ,  '_'  ,[23,'']],
				 [['',17],  '_'  ,  '_'  ,  '_'  ,['',13],  '_'  ,  '_'  ,  '_'  ],
				 [  '*'  ,['', 8],  '_'  ,  '_'  ,[16,19],  '_'  ,  '_'  ,  '_'  ],
				 [  '*'  ,  '*'  ,['',31],  '_'  ,  '_'  ,  '_'  ,  '_'  ,  '_'  ],
				 [  '*'  ,  '*'  ,  '*'  ,['',16],  '_'  ,  '_'  ,  '*'  ,  '*'  ]]

hard_puzzle_1 = [[  '*'  ,  '*'  ,  '*'  ,[ 3,''],[23,''],[30,''],  '*'  ,  '*'  ],
				 [  '*'  ,[ 6,''],[23,15],  '_'  ,  '_'  ,  '_'  ,  '*'  ,  '*'  ],
				 [['',26],  '_'  ,  '_'  ,  '_'  ,  '_'  ,  '_'  ,  '*'  ,  '*'  ],
				 [['',11],  '_'  ,  '_'  ,[10,14],  '_'  ,  '_'  ,[ 7,''],[ 6,'']],
				 [['',13],  '_'  ,  '_'  ,  '_'  ,[23,13],  '_'  ,  '_'  ,  '_'  ],
				 [  '*'  ,  '*'  ,['', 8],  '_'  ,  '_'  ,[ 4, 3],  '_'  ,  '_'  ],
				 [  '*'  ,  '*'  ,['',18],  '_'  ,  '_'  ,  '_'  ,  '_'  ,  '_'  ],
				 [  '*'  ,  '*'  ,['',14],  '_'  ,  '_'  ,  '_'  ,  '*'  ,  '*'  ]]

v_hd_puzzle_1 = [[  '*'  ,[11,''],[29,''],[ 4,''],  '*'  ,[11,''],[17,''],  '*'  ,  '*'  ,  '*'  ],
				 [['',12],  '_'  ,  '_'  ,  '_'  ,[16,10],  '_'  ,  '_'  ,  '*'  ,  '*'  ,  '*'  ],
				 [['',23],  '_'  ,  '_'  ,  '_'  ,  '_'  ,  '_'  ,  '_'  ,[ 7,''],[17,''],[ 4,'']],
				 [['',10],  '_'  ,  '_'  ,['', 8],  '_'  ,  '_'  ,[35,11],  '_'  ,  '_'  ,  '_'  ],
				 [['',14],  '_'  ,  '_'  ,[23,28],  '_'  ,  '_'  ,  '_'  ,  '_'  ,  '_'  ,  '_'  ],
				 [  '*'  ,[ 3,''],[17,10],  '_'  ,  '_'  ,[10, 9],  '_'  ,  '_'  ,[30,''],[10,'']],
				 [['',33],  '_'  ,  '_'  ,  '_'  ,  '_'  ,  '_'  ,  '_'  ,['', 9],  '_'  ,  '_'  ],
				 [['',16],  '_'  ,  '_'  ,  '_'  ,[ 3, 7],  '_'  ,  '_'  ,[16,13],  '_'  ,  '_'  ],
				 [  '*'  ,  '*'  ,  '*'  ,['',28],  '_'  ,  '_'  ,  '_'  ,  '_'  ,  '_'  ,  '_'  ],
				 [  '*'  ,  '*'  ,  '*'  ,['', 3],  '_'  ,  '_'  ,['',19],  '_'  ,  '_'  ,  '_'  ]]

v_hd_puzzle_2 = [[  '*'  ,  '*'  ,  '*'  ,[17,''],[ 6,''],  '*'  ,[ 3,''],[24,''],  '*'  ,[16,''],[29,''],  '*'  ,  '*'  ,  '*'  ,  '*'  ],
	             [  '*'  ,[ 7,''],[24, 9],  '_'  ,  '_'  ,['', 9],  '_'  ,  '_'  ,[ 4,16],  '_'  ,  '_'  ,  '*'  ,[17,''],[ 3,''],  '*'  ],
                 [['',19],  '_'  ,  '_'  ,  '_'  ,  '_'  ,[17,27],  '_'  ,  '_'  ,  '_'  ,  '_'  ,  '_'  ,[ 6,11],  '_'  ,  '_'  ,  '*'  ],
                 [['',11],  '_'  ,  '_'  ,['',11],  '_'  ,  '_'  ,[35,10],  '_'  ,  '_'  ,['',21],  '_'  ,  '_'  ,  '_'  ,  '_'  ,  '*'  ],
				 [['',12],  '_'  ,  '_'  ,[ 4,''],[11,16],  '_'  ,  '_'  ,[16,''],  '*'  ,['', 6],  '_'  ,  '_'  ,[ 3,''],  '*'  ,  '*'  ],
				 [  '*'  ,  '*'  ,[30, 6],  '_'  ,  '_'  ,[ 7,15],  '_'  ,  '_'  ,[ 3,''],  '*'  ,['', 3],  '_'  ,  '_'  ,[30,''],  '*'  ],
                 [  '*'  ,[ 3,30],  '_'  ,  '_'  ,  '_'  ,  '_'  ,  '_'  ,  '_'  ,  '_'  ,[16,''],[23,''],[29, 9],  '_'  ,  '_'  ,[16,'']],
                 [['',11],  '_'  ,  '_'  ,['',12],  '_'  ,  '_'  ,  '_'  ,[17,24],  '_'  ,  '_'  ,  '_'  ,  '_'  ,['',15],  '_'  ,  '_'  ],
			     [['', 9],  '_'  ,  '_'  ,[16,19],  '_'  ,  '_'  ,  '_'  ,  '_'  ,[ 4,18],  '_'  ,  '_'  ,  '_'  ,[ 4,16],  '_'  ,  '_'  ],
                 [  '*'  ,['',16],  '_'  ,  '_'  ,[ 7,''],  '*'  ,['',34],  '_'  ,  '_'  ,  '_'  ,  '_'  ,  '_'  ,  '_'  ,  '_'  ,  '*'  ],
                 [  '*'  ,  '*'  ,['',11],  '_'  ,  '_'  ,[29,''],  '*'  ,['', 5],  '_'  ,  '_'  ,[17,12],  '_'  ,  '_'  ,[ 7,''],[24,'']],
	             [  '*'  ,  '*'  ,[ 3,''],[16,11],  '_'  ,  '_'  ,  '*'  ,[16,''],[ 6, 9],  '_'  ,  '_'  ,[ 7,''],['',10],  '_'  ,  '_'  ],
				 [  '*'  ,['',19],  '_'  ,  '_'  ,  '_'  ,  '_'  ,[ 3,10],  '_'  ,  '_'  ,[ 4,10],  '_'  ,  '_'  ,[ 4,12],  '_'  ,  '_'  ],
	             [  '*'  ,['', 8],  '_'  ,  '_'  ,['',18],  '_'  ,  '_'  ,  '_'  ,  '_'  ,  '_'  ,['',16],  '_'  ,  '_'  ,  '_'  ,  '_'  ],
				 [  '*'  ,  '*'  ,  '*'  ,  '*'  ,['', 9],  '_'  ,  '_'  ,['', 5],  '_'  ,  '_'  ,['', 3],  '_'  ,  '_'  ,  '*'  ,  '*'  ]]


class Kakuro(CSP):

	def __init__(self, grid):
		self.grid = grid
		variables = []
		domains = {}
		neighbors = {}
		self.height = len(grid)
		self.width = len(grid[0])
		self.times_called_constraint = 0

		x = 0
		y = 0
		for i in grid: #variables are all the cells with no value.(cells that contain '_')
			y = 0
			for j in i:
				if j == '_':
					variables.append((x,y))
					neighbors[(x,y)]=[]
				y += 1
			x += 1



		for var in variables:
			domains[var]=[1,2,3,4,5,6,7,8,9]



		x = 0
		y = 0
		'''
		the neighbors of each variable are all the other variables that take part in the same constraint.
		which means that the variables in the same row constraint and the variables in the same column constraint
		'''
		for i in grid:
			y = 0
			for j in i:
				if j != '_' and j != '*' : #find the constraint cells in the puzzle ([x,y] cells) 
					if j[0] != '':											   #the column constraint is not null
						temp_x = x + 1
						while temp_x < self.height and grid[temp_x][y] == '_': #all the _ underneath the constraint cell are neighbors
							temp_x2 = temp_x-1

							while temp_x2 >= 0 and  grid[temp_x2][y] == '_':
								neighbors[(temp_x,y)].append((temp_x2,y))
								temp_x2 -= 1
							temp_x2 = temp_x+1

							while temp_x2 < self.height and  grid[temp_x2][y] == '_':
								neighbors[(temp_x,y)].append((temp_x2,y))
								temp_x2+=1
							temp_x += 1

					if j[1] != '':											    #the row constraint is not null
						temp_y = y + 1
						while temp_y < self.width and grid[x][temp_y] == '_':   #all the _ on the left of the constraint cell are neighbors
							temp_y2 = temp_y-1
							while temp_y2 >= 0 and  grid[x][temp_y2] == '_':
								neighbors[(x,temp_y)].append((x,temp_y2))
								temp_y2 -= 1
							temp_y2 = temp_y+1
							while temp_y2 < self.width and  grid[x][temp_y2] == '_':
								neighbors[(x,temp_y)].append((x,temp_y2))
								temp_y2+=1
							temp_y += 1
				y += 1
			x += 1

		'''
		for every row or column constraint if S is the sum indicated by the constraint, 
		each variable cannot have a value larger than S -(i*(i-1)/2),
		where i is the number of variables with no value that take part in the constraint

		in the same way,each variable cannot have a value larger than 
		S - (20-i)*(i-1)/2

		source: https://www.slideshare.net/VaradMeru/kakuro-solving-constraint
		'''
		x = 0
		y = 0
		for i in grid:
			y = 0
			for j in i:
				if j != '_' and j != '*' :     #for every constraint cell


					if j[0] != '':   	   #if it has a column constraint
						temp_x = x+1
						count = 0
						while temp_x < self.height and grid[temp_x][y] == '_': #count the number of empty cells
							count += 1
							temp_x += 1

						S=0
						for n in range(1,count): #compute the max value that a variable can take
							S += n

						max_val = j[0]-S

						S=0
						for n in range(1,count): #compute the min value that a variable can take
							S += 10 - n

						min_val = j[0] -S

						temp_x = x+1
						while temp_x < self.height and grid[temp_x][y] == '_': #update the domains of the variables that take part in the constraint
							length = len(domains[(temp_x,y)])
							i = 0
							while i < length:
								if domains[(temp_x,y)][i] > max_val or domains[(temp_x,y)][i] < min_val:
									domains[(temp_x,y)].remove(domains[(temp_x,y)][i])
									i -= 1
									length -= 1
								i += 1
							temp_x += 1


					if j[1] != '':      #if it has a column constraint

						temp_y = y+1
						count = 0
						while temp_y < self.width and grid[x][temp_y] == '_': #count the number of empty cells
							count += 1
							temp_y += 1
						S=0
						for n in range(1,count): #compute the max value that a variable can take
							S += n
						max_val = j[1]-S 

						S=0
						for n in range(1,count): #compute the min value that a variable can take
							S += 10 - n

						min_val = j[1] -S

						temp_y = y+1
						while temp_y < self.width and grid[x][temp_y] == '_': #update the domains of the variables that take part in the constraint
							length = len(domains[(x,temp_y)])
							i = 0
							while i < length:
								if domains[(x,temp_y)][i] > max_val or domains[(x,temp_y)][i] < min_val:
									domains[(x,temp_y)].remove(domains[(x,temp_y)][i])
									i -= 1
									length -= 1
								i += 1


							temp_y += 1
				y += 1
			x += 1


		CSP.__init__(self, variables, domains, neighbors,self.kakuro_constraint)


	'''
	this constraint takes 2 variables A and B and their values a and b respectively.
	1)if they are not different return false
	2)if the row and column constraints for the two variables are not valid return false
	'''
	def kakuro_constraint(self, A, a, B, b):
		self.times_called_constraint += 1
		if(a == b):
			return False

		top_constr_A = -1
		top_constr_B = -1
		left_constr_A = -1
		left_constr_B = -1

		x = A[0]
		y = A[1]
		while x >= 0  and self.grid[x][y] == '_': 	#go up until the column constraint of A
			x -=1

		if x >=0:									#if there is a constraint save its coordinates
			if self.grid[x][y] != '*':
				top_constr_A = (x,y)
		else:										#else save that there is no top constraint for A
			top_constr_A = -1


		x = A[0]
		while y >= 0  and self.grid[x][y] == '_':  #go left until the row constraint of A
			y -=1

		if y >= 0:								   #if there is a constraint save its coordinates
			if self.grid[x][y] != '*':
				left_constr_A = (x,y)
		else:
			left_constr_A = -1 		               #else save that there is no left constraint for A

		x = B[0]
		y = B[1]								   #same for B

		if A[0] == B[0]:
			while x >= 0  and self.grid[x][y] == '_':
				x -=1
			if x >=0:
				if self.grid[x][y] != '*':
					top_constr_B = (x,y)
					left_constr_B = -1
			else:
				top_constr_B = -1

		if A[1] == B[1]:
			while y >= 0  and self.grid[x][y] == '_':
				y -=1
			if y >= 0:
				if self.grid[x][y] != '*':
					left_constr_B = (x,y)
					top_constr_B = -1
			else:
				left_constr_B = -1


		assignment = self.infer_assignment()        #get the partial assignment implied by the current inferences 

		for i in range (0,4):                       #for every constraint found
			if i == 0:
				constr = top_constr_A
			if i == 1:
				constr = left_constr_A
			if i == 2:
				constr = top_constr_B
			if i == 3:
				constr = left_constr_B

			if constr != -1:
				x = constr[0]
				y = constr[1]

				con = self.grid[x][y]               #get the [c1,c2] pair
				part_S = 0
				count = 0						    #this counts how many empty cells are there in a constraint

				if i == 0 or i == 2:				#column constraint
					iterator = self.height
					x = x+1
					j = x
					S = con[0]
				else:
					iterator = self.width           #rowconstraint
					y = y+1
					j = y
					S = con[1]

				while j < iterator and self.grid[x][y] == "_": #for every variable taking part in the constraint
					if (x,y) == A: #if its the A given use the a value given
						part_S += a

					if (x,y) == B: #if its the B given use the b value given
						part_S += b

					if assignment.get((x,y) , None) != None and (x,y) != B and (x,y) != A: #else use the value in the assignement
						part_S += assignment.get((x,y))
					
					else:  							#if there is no value for the variable update the count 
						if (x,y)!=A and (x,y)!=B:
							count += 1

					if i == 0 or i == 2:
						x += 1
					else:
						y += 1
					j += 1

				if count == 0:          #count == 0 means that values are given to all the variables that take part in the constraint
					if part_S < S:      #so the sum of the variables has to be equal to the constraint 
						return False

				if part_S > S:         #else there are variables with no value so the partial sum has to be less than the constraint
					return False

		return True

	def display(self, assignment): #remove comments to display the solution given for the puzzle
		'''x=0
		for var in self.variables:
			if var[0] > x:
				print('')
			x = var[0]
			print(var,":",result.get(var),' ',end ='')
		print('')'''
		print('Assigns made:',self.nassigns)




def main():
	for x in range(0,4):
		if x == 0:
			puzzle = medi_puzzle_2
			print("Medium puzzle 2:")
		elif x == 1:
			puzzle = hard_puzzle_1
			print("Hard puzzle 1:")
		elif x == 2:
			puzzle = v_hd_puzzle_1
			print("Very Hard puzzle 1:")
		else:
			puzzle = v_hd_puzzle_2
			print("Very Hard puzzle 2:")

		for y in range(0,4):
			kak = Kakuro(puzzle)
			start_time = timeit.default_timer()

			if y ==0:
				print("	BT    : ",end ='')
				result = backtracking_search(kak)
			elif y ==1:
				print("	FC    : ",end ='')
				result = backtracking_search(kak,inference = forward_checking)
			elif y ==2:
				print("	FC+MRV: ",end ='')
				result = backtracking_search(kak,inference = forward_checking,select_unassigned_variable = mrv)
			else:
				print("	AC3   : ",end ='')
				result = backtracking_search(kak,inference = mac)

			print(" elapsed time:",timeit.default_timer() - start_time,"assigns made:",kak.nassigns,"constraint calls:",kak.times_called_constraint)

if __name__ == "__main__":
	main()		




		