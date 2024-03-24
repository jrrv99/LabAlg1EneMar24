from typing import Callable, Tuple, List
import tkinter as tk


def change_color(canvas, item, color=str) -> Callable[[tk.Event], None]:
    return lambda event: canvas.itemconfig(item, fill=color)


def circulo(
    canvas: tk.Canvas, x: int, y: int, r: int, c: str, move_on_click: bool = True
) -> int:
    """
    Dibuja un circulo y lo mueve un poco a la derecha si `move_on_click` es true.

    Args:
        canvas: El canvas donde se dibujará el circulo.
        x: La coordenada x del centro de la circulo.
        y: La coordenada y del centro de la circulo.
        r: el radio del circulo.
        c: el color de la cara.
        move_on_click: booleano que indica si se debe mover al hacer click, para hacer este metodo reutilizable

    Returns:
        El ID del circulo dibujado.
    """
    assert r > 0

    circle = canvas.create_oval(x - r, y - r, x + r, y + r, fill=c)

    if move_on_click:
        canvas.tag_bind(circle, "<Button-1>", lambda x: canvas.move(circle, 100, 0))

    return circle


def cuadrado(
    canvas: tk.Canvas, x: int, y: int, l: int, c1: str, c2: str = "yellow"
) -> int:
    assert l > 0

    square = canvas.create_rectangle(x, y, x + l, y + l, fill=c1)
    canvas.tag_bind(square, "<Enter>", change_color(canvas, square, c2))
    canvas.tag_bind(square, "<Leave>", change_color(canvas, square, c1))

    return square


# Define la función para desaparecer la cruz
def delete_cross(canvas, line1, line2):
    canvas.delete(line1, line2)


def cruz(canvas: tk.Canvas, x: int, y: int, l: int, width=5) -> Tuple[int, int]:
    """
    Dibuja una casita en el canvas.

    Args:
        canvas: El canvas donde se dibujará la casita.
        x: La coordenada x del centro de la cruz.
        y: La coordenada y del centro de la cruz.
        l: longitud de cada linea de la cruz.
        width: el grueso de cada linea de la cruz (opcional).

    Returns:
        Una tupla con las IDs de los objetos dibujados.
    """
    assert l > 10

    half_length = l / 2
    start_x1 = x - half_length
    start_y1 = y - half_length
    end_x1 = x + half_length
    end_y1 = y + half_length
    start_x2 = x + half_length
    start_y2 = y - half_length
    end_x2 = x - half_length
    end_y2 = y + half_length
    line1: int = canvas.create_line(start_x1, start_y1, end_x1, end_y1, width=width)
    line2: int = canvas.create_line(start_x2, start_y2, end_x2, end_y2, width=width)

    canvas.tag_bind(
        line1, "<Button-1>", lambda event: delete_cross(canvas, line1, line2)
    )
    canvas.tag_bind(
        line2, "<Button-1>", lambda event: delete_cross(canvas, line1, line2)
    )

    return (line1, line2)


def cara(canvas: tk.Canvas, x: int, y: int, c: str, r: int = 80) -> List[int]:
    """
    Dibuja una casita en el canvas.

    Args:
        canvas: El canvas donde se dibujará la casita.
        x: La coordenada x del centro de la cara.
        y: La coordenada y del centro de la cara.
        c: el color de la cara.
        r: el radio de la cara (opcional)

    Returns:
        Una lista con las IDs de los objetos dibujados.
    """
    # Face circle
    face_circle = circulo(canvas, x, y, r, c, move_on_click=False)

    # Left eye
    eyes_radius = r / 3
    left_eye_center = (x - r / 2, y)
    left_eye = circulo(
        canvas, *left_eye_center, eyes_radius, "white", move_on_click=False
    )

    # Right eye
    right_eye_center = (x + r / 2, y)
    right_eye = circulo(
        canvas, *right_eye_center, eyes_radius, "white", move_on_click=False
    )

    # Draw the nose
    nose_line = canvas.create_line(x, y, x, y + r // 3, width=3)

    # Draw the mouth line
    mouth_left = (x - r // 2, y + r // 2)
    mouth_right = (x + r // 2, y + r // 2)
    mouth_line = canvas.create_line(mouth_left, mouth_right, width=3)

    return [left_eye, right_eye, nose_line, mouth_line]


def casita(canvas: tk.Canvas, x: int, y: int) -> List[int]:
    """
    Dibuja una casita en el canvas.

    Args:
        canvas: El canvas donde se dibujará la casita.
        x: La coordenada x de la esquina inferior izquierda de la casa.
        y: La coordenada y de la esquina inferior izquierda de la casa.

    Returns:
        Una lista con las IDs de los objetos dibujados.
    """
    # Dimensiones de la casa
    ancho = 100
    alto = 120

    base = canvas.create_rectangle(x, y, x + ancho, y + alto, fill="tan")

    techo = canvas.create_polygon(
        x, y, x + ancho / 2, y - alto / 2, x + ancho, y, fill="brown"
    )

    puerta_x = x + ancho / 4
    puerta_y = y + alto * 0.75
    puerta = canvas.create_rectangle(
        puerta_x, puerta_y, puerta_x + ancho / 2, puerta_y + alto / 4, fill="yellow"
    )

    pomo = circulo(
        canvas,
        puerta_x + ancho / 3,
        puerta_y + alto / 8,
        5,
        "black",
        move_on_click=False,
    )

    ventana_x = x + ancho * 0.75
    ventana_y = y + alto * 0.3
    ventana = cuadrado(
        canvas,
        ventana_x,
        ventana_y,
        ancho / 4,
        "lightblue",
    )

    # Devolver una lista con las IDs de los objetos dibujados
    return [base, techo, puerta, pomo, ventana]


def main() -> None:
    window = tk.Tk(className="LabSem9 - José Riobueno")
    dvw = 700
    dvh = 550

    center_x = dvw // 2
    center_y = dvh // 2

    # Face radius and color
    face_radius = 80
    face_color = "yellow"

    window.geometry(f"{dvw}x{dvh}")
    canvas = tk.Canvas()

    canvas.pack(fill="both", expand=True)

    cara(canvas, center_x, center_y, face_color)
    cuadrado(canvas, 5, 5, 200, "red", "black")
    circulo(canvas, 105, 105, 100, "red")
    cruz(canvas, 105, 105, 200)
    casita(
        canvas,
        205,
        205,
    )

    window.mainloop()


if __name__ == "__main__":
    main()
