import turtle
import math

# Налаштування вікна Turtle
screen = turtle.Screen()
screen.title("Pythagoras Tree Fractal")

# Створення черепахи
t = turtle.Turtle()
t.speed(0)  # Максимальна швидкість
t.left(90)  # Повертаємо черепаху на 90 градусів для вертикального старту

def draw_tree(t, branch_length, depth):
    if depth == 0:
        return

    # Малюємо стовбур
    t.forward(branch_length)

    # Малюємо праву гілку
    t.right(45)
    draw_tree(t, branch_length * math.sqrt(2) / 2, depth - 1)

    # Повертаємо черепаху назад
    t.left(90)
    draw_tree(t, branch_length * math.sqrt(2) / 2, depth - 1)

    # Повертаємо черепаху в початкове положення
    t.right(45)
    t.backward(branch_length)

def main():
    depth = int(input("Введіть рівень рекурсії: "))

    t.up()
    t.backward(200)
    t.down()

    draw_tree(t, 100, depth)

    screen.mainloop()

if __name__ == "__main__":
    main()
