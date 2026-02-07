import math
import tkinter as tk
from tkinter import ttk


class TriangleApp:
	def __init__(self, root: tk.Tk) -> None:
		self.root = root
		self.root.title("Rechtwinkliges Dreieck")

		self.a_var = tk.StringVar(value="3")
		self.b_var = tk.StringVar(value="4")
		self.msg_var = tk.StringVar(value="")

		form = ttk.Frame(root, padding=10)
		form.pack(side=tk.TOP, fill=tk.X)

		ttk.Label(form, text="Kathete a:").grid(row=0, column=0, sticky=tk.W, padx=4, pady=4)
		ttk.Entry(form, textvariable=self.a_var, width=10).grid(row=0, column=1, sticky=tk.W)

		ttk.Label(form, text="Kathete b:").grid(row=0, column=2, sticky=tk.W, padx=4, pady=4)
		ttk.Entry(form, textvariable=self.b_var, width=10).grid(row=0, column=3, sticky=tk.W)

		ttk.Button(form, text="Zeichnen", command=self.draw).grid(
			row=0, column=4, sticky=tk.W, padx=8
		)

		ttk.Label(form, textvariable=self.msg_var, foreground="#b00020").grid(
			row=1, column=0, columnspan=5, sticky=tk.W, padx=4
		)

		self.canvas = tk.Canvas(root, width=520, height=380, background="#f8f8f8")
		self.canvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True, padx=10, pady=10)

		self.canvas.bind("<Configure>", self.on_resize)

		self.draw()

	def parse_inputs(self) -> tuple[float, float] | None:
		try:
			a = float(self.a_var.get().replace(",", "."))
			b = float(self.b_var.get().replace(",", "."))
		except ValueError:
			self.msg_var.set("Bitte Zahlen fuer a und b eingeben.")
			return None

		if a <= 0 or b <= 0:
			self.msg_var.set("a und b muessen groesser als 0 sein.")
			return None

		self.msg_var.set("")
		return a, b

	def on_resize(self, _event: tk.Event) -> None:
		self.draw()

	def draw(self) -> None:
		data = self.parse_inputs()
		if data is None:
			self.canvas.delete("all")
			return

		a, b = data
		c = math.hypot(a, b)

		self.canvas.delete("all")

		padding = 50
		width = max(1, self.canvas.winfo_width())
		height = max(1, self.canvas.winfo_height())

		max_a = width - 2 * padding
		max_b = height - 2 * padding
		scale = min(max_a / a, max_b / b)

		ax = padding
		ay = height - padding
		bx = ax + a * scale
		by = ay
		cx = ax
		cy = ay - b * scale

		self.canvas.create_polygon(ax, ay, bx, by, cx, cy, outline="#1f2937", fill="#e5e7eb")
		self.canvas.create_line(ax, ay, bx, by, width=3, fill="#111827")
		self.canvas.create_line(ax, ay, cx, cy, width=3, fill="#111827")
		self.canvas.create_line(bx, by, cx, cy, width=3, fill="#111827")

		# Right angle marker
		marker = 22
		self.canvas.create_line(ax, ay, ax + marker, ay, width=2, fill="#111827")
		self.canvas.create_line(ax + marker, ay, ax + marker, ay - marker, width=2, fill="#111827")
		self.canvas.create_line(ax + marker, ay - marker, ax, ay - marker, width=2, fill="#111827")

		a_label_x = (ax + bx) / 2
		a_label_y = ay + 18
		b_label_x = ax - 22
		b_label_y = (ay + cy) / 2
		dx = cx - bx
		dy = cy - by
		length = max(1.0, math.hypot(dx, dy))
		nx = -dy / length
		ny = dx / length
		mid_x = (bx + cx) / 2
		mid_y = (by + cy) / 2
		centroid_x = (ax + bx + cx) / 3
		centroid_y = (ay + by + cy) / 3
		if (mid_x - centroid_x) * nx + (mid_y - centroid_y) * ny < 0:
			nx = -nx
			ny = -ny
		offset = max(18, min(32, 0.08 * min(width, height)))
		right_shift = max(10, min(26, 0.04 * width))
		c_label_x = mid_x + nx * offset + right_shift
		c_label_y = mid_y + ny * offset

		self.canvas.create_text(
			a_label_x,
			a_label_y,
			text=f"a = {a:g}",
			fill="#111827",
			font=("Segoe UI", 11, "bold"),
		)
		self.canvas.create_text(
			b_label_x,
			b_label_y,
			text=f"b = {b:g}",
			fill="#111827",
			font=("Segoe UI", 11, "bold"),
			angle=90,
		)
		self.canvas.create_text(
			c_label_x,
			c_label_y,
			text=f"c = {c:g}",
			fill="#111827",
			font=("Segoe UI", 11, "bold"),
		)


def main() -> None:
	root = tk.Tk()
	app = TriangleApp(root)
	root.minsize(520, 380)
	root.mainloop()


if __name__ == "__main__":
	main()
