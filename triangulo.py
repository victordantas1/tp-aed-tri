import tkinter as tk

def triangulo(nivel, canvas, pontas, ponta_esq, ponta_dir,  x1, y1, x2, y2, x3, y3):
    if nivel == 1:
        canvas.create_polygon([x1, y1, x2, y2, x3, y3], outline='black', fill='blue')
        return
    canvas.create_polygon([x1, y1, x2, y2, x3, y3], outline='black', fill='blue')
    if pontas:
        nivel -= 1
        triangulo(nivel, canvas, not pontas, (ponta_esq[0] - 20, ponta_esq[1] + 48),(ponta_dir[0] + 20, ponta_dir[1] + 48), x2, y2, x2 - 20, y2 + 48, x2 + 20, y2 + 48)
        triangulo(nivel, canvas, not pontas, (ponta_esq[0] - 20, ponta_esq[1] + 48),(ponta_dir[0] + 20, ponta_dir[1] + 48), x3, y3, x3 - 20, y3 + 48, x3 + 20, y3 + 48)
    else:
        triangulo(nivel, canvas, not pontas, (ponta_esq[0] - 20, ponta_esq[1] + 48),(ponta_dir[0] + 20, ponta_dir[1] + 48), ponta_dir[0], ponta_dir[1], ponta_dir[0] - 20, ponta_dir[1] + 48, ponta_dir[0] + 20, ponta_dir[1] + 48)
        triangulo(nivel, canvas, not pontas, (ponta_esq[0] - 20, ponta_esq[1] + 48),(ponta_dir[0] + 20, ponta_dir[1] + 48), ponta_esq[0], ponta_esq[1], ponta_esq[0] - 20, ponta_esq[1] + 48, ponta_esq[0] + 20, ponta_esq[1] + 48)

if __name__ == '__main__':
    window = tk.Tk()
    window.geometry("1366x768")
    canvas = tk.Canvas(window, width=1366, height=768)
    nivel = int(input())
    triangulo(nivel, canvas, True, (663,148), (703,148), 683, 100, 663, 148, 703, 148)
    canvas.pack()
    window.mainloop()
