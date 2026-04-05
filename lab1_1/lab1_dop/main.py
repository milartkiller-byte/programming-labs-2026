from lab1_dop import calculate_inventory

def main():
    print("=" * 50)
    print("РОБОТ-ІНВЕНТАРИЗАТОР НА СКЛАДІ")
    print("=" * 50)

    try:
        N = int(input("Введіть кількість рядків складу (N): "))
        M = int(input("Введіть кількість стовпців складу (M): "))

        if N <= 0 or M <= 0:
            print("Помилка: Розміри складу мають бути більшими за 0.")
            return

        matrix = []
        print(f"\nВведіть кількість товарів (через пробіл) для {M} стовпців:")
        for i in range(N):
            row_input = input(f"Рядок {i+1}: ")
            row = list(map(int, row_input.split()))

            if len(row) != M:
                print(f"Помилка: Ви ввели {len(row)} елементів, а потрібно {M}.")
                return
            matrix.append(row)
            
        K = int(input("\nВведіть кількість клітинок для обходу (K): "))
        E_max = int(input("Введіть максимальний заряд батареї (E_max): "))

        # Викликаємо функцію з імпортованого модуля
        goods_sum_K, is_enough_energy, recharges = calculate_inventory(matrix, K, E_max)

        print("\n" + "=" * 50)
        print("РЕЗУЛЬТАТИ:")
        print(f"Сума зібраних товарів за {K} кроків: {goods_sum_K}")
        print(f"Чи вистачило енергії без підзарядок: {'Так' if is_enough_energy else 'Ні'}")
        print(f"Кількість підзарядок: {recharges}")
        print("=" * 50)

    except ValueError:
        print("\nПомилка: Будь ласка, вводьте лише цілі числа.")

if __name__ == "__main__":
    main()