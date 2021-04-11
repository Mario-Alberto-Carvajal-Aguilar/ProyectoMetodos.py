import math

contador = 0
while contador != 5:
    print("Menu")
    print("1.- Bisección")
    print("2.- Newton")
    print("3.- Secante")
    print("4.- G(x)")
    print("5.- Salir del programa")
    opcion = input("Ingrese la opcion que desea ejecutar: ")

    if opcion == "1":
        print("---Metodo biseccion---")
        print("Funcion utilizada: x**3 + 4*x**2-10")
        xi = float(input("Ingrese el valor de Xi: "))
        xs = float(input("Ingrese el valor de Xs: "))
        cota = float(input("Ingrese el valor de la cota: "))
        maxiteraciones = int(input("Ingrese la cantidad de iteraciones: "))


        def biseccion1(xi, xs, cota, maxiteraciones):
            error=1
            i=0
            xranterior=0
            while error > cota and i < maxiteraciones:
                xr = (xi + xs) / 2
                fxi = fx(xi)
                fxr = fx(xr)
                comp = fxi * fxr
                error = errorf(xr, xranterior)
                xranterior = xr
                if error < 0:
                    error = error*(-1)
                i += 1
                print(i, "  xi={:.4f}".format(xi), "  xs={:.4f}".format(xs), "xr={:.4f}".format(xr),
                      "fx(xi)={:.4f}".format(fxi), "fx(xr)={:.4f}".format(fxr), "f(xi)*f(xr)={:.4f}".format(comp),
                      "  Error V={:.4f}".format(error))
                if comp < 0:
                    xs = xr
                elif comp > 0:
                    xi = xr

        def fx(x):
            return x**3 + 4*x**2-10

        def errorf(xactual, xanterior):
            return abs(xactual - xanterior) / xactual

        biseccion1(xi, xs, cota, maxiteraciones)

    elif opcion == "2":
        print("---Metodo Newton---")
        print("Funcion utilizada: (e(-x))-x")
        x0 = float(input("Ingrese el valor de x0: "))
        cota = float(input("Ingrese el valor de la cota: "))
        maxiteraciones = int(input("Ingrese la cantidad de iteraciones: "))

        def fx(x):
            return (math.exp(-x))-x

        def derivadafx(x):
            return -(math.exp(-x))-1

        def getError(xactual, xanterior):
            return abs(xactual-xanterior)/xactual

        def newton(x0, cota, maxiteraciones):
            error = 1
            xi = x0
            i = 0
            while error > cota and i < maxiteraciones:
                fxi = fx(xi)
                fdxi = derivadafx(xi)
                part1 = xi
                part2 = fxi / fdxi
                xip1mfxddefx = part1 - part2
                error = (xip1mfxddefx - xi) / xip1mfxddefx
                if error < 0:
                    error = error*(-1)
                i += 1
                print(i, "  xi={:.4f}".format(xi), "f(xi)={:.4f}".format(fxi), "f´(xi)={:.4f}".format(fdxi), "xi+1-f(x)/f´(x)={:.4f}".format(xip1mfxddefx),
                      "  Error V={:.4f}".format(error))
                xi = xip1mfxddefx
        newton(x0, cota, maxiteraciones)
    elif opcion == "3":
        print("---Metodo Secante---")
        print("Funcion utilizada: e^-2-x")
        x0 = float(input("Ingrese el valor de x0: "))
        x1 = float(input("Ingrese el valor de x1: "))
        tol = float(input("Ingrese el valor de la cota: "))
        maxiteraciones = int(input("Ingrese la cantidad de iteraciones: "))


        def secante(x0, x1, tol, maxiteraciones):
            error1 = 1e3
            n = 0
            xim1 = x0  # 1
            xi = x1  # 2
            while error1 > tol and maxiteraciones > n:
                fxim1 = f(xim1)
                fxi = f(xi)
                xim1mxi = xim1-xi
                raiz2 = fxi * xim1mxi
                raiz3 = fxim1 - fxi
                raiz4 = raiz2/raiz3
                raiz = xi - raiz4
                error1 = (raiz - xi) / raiz
                if error1 < 0:
                    error1 = error1*(-1)
                n += 1
                print(n, "  xi-1= {:.4f}".format(xim1), "  xi= {:.4f}".format(xi), "f(xi-1)= {:.4f}".format(fxim1),
                      "f(xi)= {:.4f}".format(fxi), "xi-1-xi= {:.4f}".format(xim1mxi), "raiz= {:.4f}".format(raiz),
                      "  Error V= {:.4f}".format(error1))
                xim1 = xi
                xi = raiz

        def f(x):
            return (math.exp(-x**2))-x

        secante(x0, x1, tol, maxiteraciones)
    elif opcion == "4":
        print("---Metodo punto fijo---")
        xi = float(input("Ingrese el valor inicial: "))
        tol = float(input("Ingrese el valor de la cota: "))
        maxiteraciones = int(input("Ingrese la cantidad de iteraciones: "))
        print()

        def puntofijo(xi, tol, maxiteraciones):
            error=1
            i = 0
            while error > tol and maxiteraciones > i:
                gxi = gx(xi)
                fxi = fx(gxi)
                error = (gxi-xi)/gxi
                if error < 0:
                    error = error*(-1)
                i = i + 1
                print(i, "  xi= {:.4f}".format(xi),"  xi+1-g(x)= {:.4f}".format(gxi), "  f(x)= {:.4f}".format(fxi),
                      "  Error V= {:.4f}".format(error))
                xi = gxi

        def fx(x):
            return (math.exp(-x))-x

        def gx(x):
            return math.exp(-x)

        puntofijo(xi, tol, maxiteraciones)
    elif opcion == "5":
        print("---Saliendo del programa---")
        contador = 5

    else:
        print("Seleccione una opcion valida")


