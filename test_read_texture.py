from read_texture import generate_random_samples_from_pixel_texture
import taichi as ti

ti.init(arch=ti.cpu)
rpoints = generate_random_samples_from_pixel_texture("letters.png")

gui = ti.GUI("Test letters", res=(520, 520))

while gui.running:
    gui.circles(rpoints, radius=2, color=0xFF0000)
    gui.show()
