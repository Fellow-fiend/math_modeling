import numpy as np
import task_1 as t1
import task_2 as t2
import task_3 as t3
import task_4 as t4
import task_1_dop as t1d
import task_2_dop as t2d
import task_4_dop as t4d
'''
t1.square_plot(-12, 3, 25)
t2.parabola_plot()
t2.hyperbola_plot()
t3.cicrle_plot(np.linspace(0.01, 10, 100))
t3.ellipse_plot(12, 22, np.linspace(0.01, 10, 20))
t4.log_spiral(-0.12)
t4.arch_spiral()
t4.rod_spiral()
t4.rose_spiral(2/3*6)
t4.rose_spiral(2/3*4)
'''

t1d.Lissajous_curve(B = 17/23 * np.sqrt(np.pi), a = 4, b = 12)
t2d.ellipse(2, 14/15)
t4d.stairs()