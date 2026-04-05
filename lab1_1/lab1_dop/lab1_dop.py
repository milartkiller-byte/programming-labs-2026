def calculate_inventory(matrix, K, E_max):
    """
    Функція розраховує результати обходу складу.
    Повертає: (сума_товарів_K, чи_вистачило_енергії, кількість_підзарядок)
    """
    if not matrix or not matrix[0]:
        return 0, True, 0

    N = len(matrix)
    M = len(matrix[0])
    total_cells = N * M
    
    r, c = 0, 0
    up_right = True
    
    current_energy = E_max
    recharges = 0
    goods_sum_K = 0
    
    for step in range(total_cells):
        if step < K:
            goods_sum_K += matrix[r][c]

        if step == total_cells - 1:
            break

        cost = 0
        if up_right:
            if c == M - 1:     
                r += 1
                up_right = False
                cost = 1
            elif r == 0:        
                c += 1
                up_right = False
                cost = 1
            else:               
                r -= 1
                c += 1
                cost = 2
        else:
            if r == N - 1:      
                c += 1
                up_right = True
                cost = 1
            elif c == 0:        
                r += 1
                up_right = True
                cost = 1
            else:               
                r += 1
                c -= 1
                cost = 2
        
        if current_energy < cost:
            recharges += 1
            current_energy = E_max 
            
        current_energy -= cost
        
    is_enough_energy = (recharges == 0)
    return goods_sum_K, is_enough_energy, recharges
