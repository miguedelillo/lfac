from afd import *

def automata_reconoce_L():
    # Sea L = (a|b)bb(a)*b
    q0 = t_estado('q0')
    q1 = t_estado('q1')
    q2 = t_estado('q2')
    q3 = t_estado('q3')
    qf = t_estado('qf')

    estados = set([q0, q1, q2, q3, qf])

    alfabeto = set('ab')

    funcion_transicion = t_transicion({
        (q0, 'a') : q1,
        (q0 ,'b') : q1,
        (q1 ,'b') : q2,
        (q2 ,'b') : q3,
        (q3 ,'b') : qf,
        (q3, 'a') : q3 
    })

    return t_automata(
        estados,
        alfabeto,
        funcion_transicion,
        estado_inicial= q0,
        estados_finales=set([qf])
    )

def automata_cant_par_a():
    par = t_estado('par')
    impar = t_estado('impar')

    estados = set([par, impar])

    alfabeto = set('a')

    funcion_transicion = t_transicion({
        (par,'a') : impar,
        (impar,'a') : par
        })

    return t_automata(
        estados=estados,
        alfabeto=alfabeto,
        transicion=funcion_transicion,
        estado_inicial=par,
        estados_finales=set([par])
    )