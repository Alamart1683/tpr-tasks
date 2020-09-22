import math
# Накорябано Андреем Лисовым

# Метод вычисления дихотомией
def dihotomia(d, a, b, e0):
    iteration_number = math.ceil(math.log2((b-a-d)/(2*e0-d)))
    print("Метод счёта с помощью дихотомии")
    print("По формуле было определено, что необходимо", iteration_number, "итераций")
    print("")
    iteration = 1
    while iteration <= iteration_number:
        print ("Итерация ", iteration)
        x1 = (b + a - d)/2
        x2 = (b + a + d)/2
        x1 = round(x1, 4)
        x2 = round(x2, 4)
        print("x1 =", x1, "x2 =", x2)
        f1 = function(x1)
        f1 = round(f1, 4)
        f2 = function(x2)
        f2 = round(f2, 4)
        print("f(x1) =", f1, "f(x2) =", f2)
        if f1 <= f2:
            b = x2
            print("Так как f(x1) <= f(x2), то рассмотрим отрезок [a, x2]:")
        else:
            a = x1
            print("Так как f(x1) > f(x2), то рассмотрим отрезок [x1, b]:")
        e = (b - a)/2
        e = round(e, 4)
        print("Текущая a =", a)
        print("Текущая b =", b)
        print("Точность на текущей итерации =", e)
        if (e > e0):
            e_str = "e" + str(iteration)
            print(e_str, "=", e, ">", "e =", e0)
            print("Так как это больше минимального значения точности, переходим на следующую итерацию.")
            iteration += 1
            if (iteration == iteration_number):
                iteration_number += 1
        else:
            print("Достигнуто минимальное значение точности, переходим к финальному шагу алгоритма")
            break;
        print("")
    print("")
    print("Финальный шаг алгоритма:")
    final_x = round(((a + b)/2), 4)
    final_y = round(function(final_x), 4)
    print("x* =", final_x)
    print("f* =", final_y)
    print("")

# Метод вычисления золотым сечением
def golden_section(r, a, b, e0):
    iteration = 1
    print("Метод счёта с помощью золотого сечения")
    print("")
    while True:
        print("Итерация ", iteration)
        x1 = round((a + (1 - r)*(b - a)), 4)
        x2 = round((a + r*(b - a)), 4)
        print("x1 =", x1, "x2 =", x2)
        f1 = round(function(x1), 4)
        f2 = round(function(x2), 4)
        print("f(x1) =", f1, "f(x2) =", f2)
        if f1 <= f2:
            b = x2
            print("Так как f(x1) <= f(x2), то рассмотрим отрезок [a, x2]:")
        else:
            a = x1
            print("Так как f(x1) > f(x2), то рассмотрим отрезок [x1, b]:")
        print("Текущая a =", a)
        print("Текущая b =", b)
        e = round((b - a)/2,4)
        print("Точность на текущей итерации =", e)
        if e > e0:
            e_str = "e" + str(iteration)
            print(e_str, "=", e, ">", "e =", e0)
            print("Так как это больше минимального значения точности, переходим на следующую итерацию.")
            iteration += 1
        else:
            print("Достигнуто минимальное значение точности, переходим к финальному шагу алгоритма")
            break;
        print("")
    print("")
    print("Финальный шаг алгоритма:")
    final_x = round(((a + b)/2), 4)
    final_y = round(function(final_x), 4)
    print("x* =", final_x)
    print("f* =", final_y)
    print("")

###########################################################################################################
###########################################################################################################
###########################################################################################################
                                    # ТПР 5 БУДЬ ОНА НЕЛАДНА #

# Метод вычисления методом средней точки
def middle_point(a, b, e0):
    iteration = 1
    print("Метод счёта с помощью средней точки")
    print("")
    while True:
        print("Итерация ", iteration)
        x = round(((a + b) / 2), 4)
        print("x с палкой сверху =", x)
        f = round(function_d(x), 4)
        print("f'(икс с палкой сверху) =", f)
        if abs(f) > e0:
            f_str = "|f'(x с палкой)|"
            print(f_str, "=", f, ">", "e =", e0)
            print("Так как это больше минимального значения точности, переходим на следующую итерацию.")
            if f > 0:
                print("Так как f'(x с палкой) > 0, то рассмотрим отрезок [a, x с палкой]:")
                b = x
            else:
                print("Так как f'(x с палкой) <= 0, то рассмотрим отрезок [x с палкой, b]:")
                a = x
            print("Текущая a =", a)
            print("Текущая b =", b)
            iteration += 1
        else:
            print("Достигнуто минимальное значение точности, переходим к финальному шагу алгоритма")
            break;
        print("")
    print("")
    print("Финальный шаг алгоритма:")
    final_x = x
    final_y = round(function(x), 4)
    print("x* =", final_x)
    print("f* =", final_y)
    print("")
    
# Метод хорд
def hordes(a, b, e0):
    iteration = 1
    fa = function_d(a)
    fb = function_d(b)
    print("Метод счёта с помощью хорд")
    print("")
    while True:
        print("Итерация ", iteration)
        x = round((a - ((fa / (fa - fb)) * (a - b))), 4)
        print("x с волночкой сверху =", x)
        f = round(function_d(x), 4)
        print("f'(икс с волночкой сверху) =", f)
        if abs(f) > e0:
            f_str = "|f'(x с волночкой)|"
            print(f_str, "=", f, ">", "e =", e0)
            print("Так как это больше минимального значения точности, переходим на следующую итерацию.")
            if f > 0:
                print("Так как f'(x с волночкой) > 0, то рассмотрим отрезок [a, x с волночкой]:")
                b = x
                fb = f
            else:
                print("Так как f'(x с волночкой) <= 0, то рассмотрим отрезок [x с волночкой, b]:")
                a = x
                fa = f
            print("Текущая a =", a)
            print("Текущая b =", b)
            print("Текущая f'(a) =", fa)
            print("Текущая f'(b) =", fb)
            iteration += 1
        else:
            print("Достигнуто минимальное значение точности, переходим к финальному шагу алгоритма")
            break;
        print("")
    print("")
    print("Финальный шаг алгоритма:")
    final_x = x
    final_y = round(function(x), 4)
    print("x* =", final_x)
    print("f* =", final_y)
    print("")

# Метод Ньютона
def Newton(a, b, e0):
    print("Метод Ньютона")
    iteration = 1
    x0 = round(((a+b)/2), 4)
    print("x0 =", x0)
    x1 = round((x0 - (function_d(x0)/function_dd(x0))), 4)
    print("x1 =", x1)
    print("f'(x1) =", function_d(x1))
    print("")
    while abs(function_d(x1)) > e0:
        print("Итерация ", iteration)
        x1 = round((x0 - (function_d(x0)/function_dd(x0))), 4)
        print("Текущий x1 =", x1)
        print("f'(x1) =", function_d(x1))
        x0 = x1
        iteration += 1
        print("")
    print("Так как |f'(x1)| =", function_d(x1), " < e0 = 0.1, то завершаем счёт")
    print("")
    print("Финальный шаг алгоритма:")
    final_x = x1
    final_y = round(function(x1), 4)
    print("x* =", final_x)
    print("f* =", final_y)
    print("")

# Метод ломаных
def BrokenLine(a, b, e0):
    print("Метод ломаных")
    iteration = 1
    L = round(get_max(a, b), 4)
    print("L =", L)
    print("")
    while True:
        print("Итерация ", iteration)
        x0 = round((1/(2*L))*(function(a)-function(b)+L*a+L*b), 4)
        print("x0 =", x0)
        p0 = round(0.5*(function(a)+function(b)+ L*a - L*b), 4)
        print("p0 =", p0)
        d = round(((1/(2*L))*(function(x0)-p0)), 4)
        d_str = "d" + str(iteration)
        print(d_str, "=", d)
        x1p = round(x0-d, 4)
        print("x1' =", x1p)
        x1pp = round(x0+d, 4)
        print("x1'' =", x1pp)
        p1 = round((0.5*(function(x0)+p0)), 4)
        print("p1 =", p1)
        ld = round(2*L*d, 4)
        print("2Ld =", ld)
        if round(2*L*d, 4) > e0:
            print("Так как 2Ld > e0, то продолжаем поиск")
            if abs(function_d(x1p)) < abs(function_d(x1pp)):
                print("Так как |f'(x1')| < |f'(x1'')|:")
                b = x0
                print("b = x0 =", x0)
                x0 = x1p
                print("x0 = x1' =", x1p)
            else:
                print("Так как |f'(x1')| > |f'(x1'')|:")
                a = x0
                print("a = x0 =", x0)
                x0 = x1pp
                print("x0 = x1'' =", x1p)
            print("Текущая a =", a)
            print("Текущая b =", b)
            iteration += 1
            print("")
        else:
            print("Достигнуто минимальное значение точности, переходим к финальному шагу алгоритма")
            break
    print("")
    print("Финальный шаг алгоритма:")
    final_x = x0
    final_y = round(function(x0), 4)
    print("x* =", final_x)
    print("f* =", final_y)
    print("")

# Определить максимальное значение функции в окраинных точках
def get_max(a, b):
    if abs(function_d(a)) > abs(function_d(b)):
        return abs(function_d(a))
    else:
        return abs(function_d(b))
    
# Функции из вариантов задания
def function(x):
    y = x*x - x -1
    return y

# Производная от функции варианта задания
def function_d(x):
    y = 2*x - 1
    return y

# Производная второго порядка от функции варианта задания
def function_dd(x):
    y = 2
    return y

# dihotomia(0.08, -5, 5, 0.1)
# golden_section(0.618, -5, 5, 0.1)
# middle_point(-5, 5, 0.1)
# hordes(-5, 5, 0.1)
# Newton(-5, 5, 0.1)
# print(function(-1.0532))
BrokenLine(-5, 5, 0.1)
