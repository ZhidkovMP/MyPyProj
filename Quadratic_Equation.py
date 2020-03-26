# Wrote by MikeWing

while True:

# this code is printing options:

    print('=====================================================================')
    print('Options:')
    print('-----------------------')
    print(' - Enter "quit" if you want to close this program')
    print(' - Enter the coefficients of your quadratic equation axx+bx+c=0 like this:"a,b,c":')
    print('|--------------------->')

# this code is asking coefficients of equation by user:

    user_input = input()
    if user_input == 'quit':
        print('=====================================================================')
        print('Wrote by Mikhail (MikeWing) Zhidkov.'.rjust(70))
        break
    print('-----------------------')

# this code is converting list to the tuple of float numbers:
    try:
        user_input = tuple(float(item) for item in user_input.split(','))

# this code is assigning coefficients a, b, c:

        a = user_input[0]
        b = user_input[1]
        c = user_input[2]

# this code is assigning discriminant

        d = b ** 2 - 4 * a * c

# this code is searching roots if discriminant is positive:

        if d >= 0:
            x1 = (-b + d ** (1 / 2)) / (2 * a)
            x2 = (-b - d ** (1 / 2)) / (2 * a)
            print('x1=' + str(round(x1, 2)))
            print('x2=' + str(round(x2, 2)))

# this code is searching roots if discriminant is negative:

        else:
            d = -d
            im_root = abs((d ** (1 / 2)) / (2 * a))
            re_root = (-b) / (2 * a)
            print('x1=' + str(round(re_root, 2)) + '+' + str(round(im_root, 2)) + 'i')
            print('x2=' + str(round(re_root, 2)) + '-' + str(round(im_root, 2)) + 'i')

# this code is printing exceptions

    except ValueError:
        print("Oups.. You probably enter symbols, not numbers. Try again.")
    except ZeroDivisionError:
        print("Oups.. You probably enter coefficient a = 0. It is not quadratic equation, try to solve it by yourself.")
    except IndexError:
        print("Oups.. You probably enter one or two coefficients. Please enter three coefficients divided by comma, like this: a,b,c")
    except Exception:
        print('Oups.. Something going wrong and the programm crashed down. Please write about it to e-mail')
    finally:
        True