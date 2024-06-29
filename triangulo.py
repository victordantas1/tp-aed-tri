import tkinter as tk

def triangulo(nivel, canvas, pontas, dir, x1, y1, x2, y2, x3, y3):
    
    if nivel == 1:
        canvas.create_polygon([x1, y1, x2, y2, x3, y3], outline='black', fill='blue')
        return
    canvas.create_polygon([x1, y1, x2, y2, x3, y3], outline='black', fill='blue')
    if pontas:
        nivel -= 1
        triangulo(nivel, canvas, not pontas, not dir, x2, y2, x2 - 20, y2 + 48, x2 + 20, y2 + 48)
        triangulo(nivel, canvas, not pontas, dir, x3, y3, x3 - 20, y3 + 48, x3 + 20, y3 + 48)
    else:
        if dir:
            ponta_dir_x = x3
            ponta_dir_y = y3
            triangulo(nivel, canvas, not pontas, dir, ponta_dir_x, ponta_dir_y, ponta_dir_x - 20, ponta_dir_y + 48, ponta_dir_x + 20, ponta_dir_y + 48)
        else:
            ponta_esq_x = x2
            ponta_esq_y = y2
            triangulo(nivel, canvas, not pontas, not dir, ponta_esq_x, ponta_esq_y, ponta_esq_x - 20, ponta_esq_y + 48, ponta_esq_x + 20, ponta_esq_y + 48)

if __name__ == '__main__':
    window = tk.Tk()
    window.geometry("1366x768")
    canvas = tk.Canvas(window, width=1366, height=768)
    nivel = int(input())
    triangulo(nivel, canvas, True, True, 683, 100, 663, 148, 703, 148)
    canvas.pack()
    window.mainloop()
