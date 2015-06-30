__author__ = 'ramvibhakar'
from datetime import datetime

startTime = datetime.now()
FILE_NAME = 'map.txt'

class SkiingInSingapore:
    elevation = []
    longest_sub_seq = []
    rows = 0
    columns = 0

    def input_into_graph(self):
        f = open(FILE_NAME, 'r')
        self.rows, self.columns = [int(x) for x in f.readline().split()]
        for i in xrange(0,self.rows):
            self.elevation.append([int(x) for x in f.readline().split()])

    def find_longest_steep_path(self):
        max = 0
        max_slope = 0
        for i in xrange(0,self.rows):
            self.longest_sub_seq.append([(0,0) for j in xrange(0,self.columns)])

        for i in xrange(0,self.rows):
            for j in xrange(0,self.columns):
                current,end = self.find_longest_of(i,j)
                slope = end - self.elevation[i][j]
                if current > max:
                    max = current
                    max_slope = slope
                elif current == max and slope > max_slope:
                    max_slope = slope
        return max, max_slope

    def find_longest_of(self,i,j):
        if self.longest_sub_seq[i][j][0] == 0:
            max = 0
            min_end = self.elevation[i][j]
            for k in range(-1,2):
                for l in range(-1,2):
                    if (not(k==0 and l==0)
                    and not(abs(k) == abs(l))
                    and (i+k >= 0) and i+k < self.rows
                    and j+l >= 0 and j+l < self.columns
                    and self.elevation[i+k][j+l] > self.elevation[i][j]):
                        current, end = self.find_longest_of(i+k, j+l)
                        if current > max:
                            max = current
                            min_end = end
                        elif current == max and end < min_end:
                            min_end = end
            self.longest_sub_seq[i][j] = (max + 1, min_end)
        return self.longest_sub_seq[i][j]

def main():
    obj = SkiingInSingapore()
    obj.input_into_graph()
    max_dist, max_drop = obj.find_longest_steep_path()
    print("The max length of skii is "+ str(max_dist))
    print("The drop of the skii is "+ str(max_drop))

if __name__ == "__main__":
    main()
    total_time_taken = datetime.now() - startTime
    print ('The program was excecuted in ' + str(total_time_taken))