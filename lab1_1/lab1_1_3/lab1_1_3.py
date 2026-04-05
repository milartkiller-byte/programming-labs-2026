def zigzag(matrix):
    
    if not matrix or not matrix[0]:
        return []

    m = len(matrix)       
    n = len(matrix[0])    
    result = []
    
    r, c = 0, 0
    up_right = True       

    for _ in range(m * n):
        result.append(matrix[r][c])
        
        if up_right:
            
            if c == n - 1:      
                r += 1
                up_right = False
            elif r == 0:        
                c += 1
                up_right = False
            else:               
                r -= 1
                c += 1
        else:
            
            if r == m - 1:      
                c += 1
                up_right = True
            elif c == 0:        
                r += 1
                up_right = True
            else:               
                r += 1
                c -= 1
                
    return result
import unittest

class TestZigzag(unittest.TestCase):

    def test_m_5_n_5(self):
     
        matrix = [
            [ 1,  2,  6,  7, 15],
            [ 3,  5,  8, 14, 16],
            [ 4,  9, 13, 17, 22],
            [10, 12, 18, 21, 23],
            [11, 19, 20, 24, 25]
        ]
        expected = list(range(1, 26))
        self.assertEqual(zigzag(matrix), expected)

    def test_m_2_n_4(self):
       
        matrix = [
            [1, 2, 3, 4],
            [5, 6, 7, 8]
        ]
        expected = [1, 2, 5, 6, 3, 4, 7, 8]
        self.assertEqual(zigzag(matrix), expected)

    def test_m_6_n_1(self):
        
        matrix = [
            [1], 
            [2], 
            [3], 
            [4], 
            [5], 
            [6]
        ]
        expected = [1, 2, 3, 4, 5, 6]
        self.assertEqual(zigzag(matrix), expected)

    def test_m_1_n_1(self):
     
        matrix = [[42]]
        expected = [42]
        self.assertEqual(zigzag(matrix), expected)

if __name__ == '__main__':
    unittest.main()
