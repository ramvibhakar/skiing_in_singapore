__author__ = 'ramvibhakar'
from datetime import datetime

startTime = datetime.now()
FILE_NAME = 'map.txt'

# The problem is a type of finding the largest decreasing subsequence of 2D array
# This problem can be simplified using the dynamic programming approach
class SkiingInSingapore:
    elevation = []                  # Store the elevation of each point here
    longest_sub_seq = []            # Datastructure used to store the length of longest decreasing sub-sequence (length)
                                    # and the smallest elevation of the sub-sequence (small)
                                    # These two parameters are stored as a tuple (length, small)
    rows = 0            # number of rows in file
    columns = 0         # number of columns in file

    # This method reads the file map.txt and loads data into elevation[][]
    def input_into_2d_array(self):
        f = open(FILE_NAME, 'r')
        self.rows, self.columns = [int(x) for x in f.readline().split()]
        for i in xrange(0,self.rows):
            self.elevation.append([int(x) for x in f.readline().split()])

    # This method finds the largest decreasing subsequence which has a higher drop
    def find_longest_steep_path(self):
        max = 0
        max_slope = 0
        # Initialize the longest_sub_seq with (0,0)
        for i in xrange(0,self.rows):
            self.longest_sub_seq.append([(0,0) for j in xrange(0,self.columns)])

        # Find the longest decreasing subsequence of each element
        for i in xrange(0,self.rows):
            for j in xrange(0,self.columns):
                current,end = self.find_longest_of(i,j)
                slope = self.elevation[i][j] - end
                # Find the max of length and slope
                if current > max:
                    max = current
                    max_slope = slope
                # If length is same, check the slope
                elif current == max and slope > max_slope:
                    max_slope = slope
        return max, max_slope

    def find_longest_of(self,i,j):
        if self.longest_sub_seq[i][j][0] == 0:
            max = 0
            min_end = self.elevation[i][j]
            for k in range(-1,2):
                for l in range(-1,2):                       # These lines are used
                    if (not(k==0 and l==0)                  # to check the NESW neighbours
                    and not(abs(k) == abs(l))               # of an element
                    and (i+k >= 0) and i+k < self.rows      # Donot check the neighbours
                    and j+l >= 0 and j+l < self.columns     # who are diagonal
                    and self.elevation[i+k][j+l] < self.elevation[i][j]):  # check if the neighbour is lower than
                                                                           # the current element
                        # Recursively find the length of longest decreasing subsequence of neighbors
                        current, end = self.find_longest_of(i+k, j+l)
                        # Move to the neighbour who have a large length of subsequence
                        if current > max:
                            max = current
                            min_end = end
                        # If the max length is same, the check for the smallest elevation
                        elif current == max and end < min_end:
                            min_end = end
            self.longest_sub_seq[i][j] = (max + 1, min_end)
        return self.longest_sub_seq[i][j]

def main():
    obj = SkiingInSingapore()
    obj.input_into_2d_array()
    max_dist, max_drop = obj.find_longest_steep_path()
    print("The max length of skii is "+ str(max_dist))
    print("The drop of the skii is "+ str(max_drop))

if __name__ == "__main__":
    main()
    total_time_taken = datetime.now() - startTime
    print ('The program was excecuted in ' + str(total_time_taken))