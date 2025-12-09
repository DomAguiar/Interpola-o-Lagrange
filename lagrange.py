# Interpolação de Lagrange

## P(x) = Somatório^n_i=0(L_i(x)*y_i)
### L_i(x) = Produtorio^n_j=0&j!=i(x-xj/xi-xj)
import streamlit as st
import numpy as np
import plotly.graph_objects as go
from sympy import symbols, nsimplify, lambdify
x = symbols("x")


entradax = st.text_input("Coordenadas X","333 666 777")
entraday = st.text_input("Coordenadas Y", "3 1 32")

try:
    eixox = [float(i) for i in entradax.split(" ")]
    eixoy = [float(i) for i in entraday.split(" ")]

    if len(eixox) != len(eixoy):
        st.error("As listas X e Y precisam ter o mesmo tamanho.")
    else:
        n = len(eixox)

    soma = 0

    for i in range(0,n):
        produto = 1
        for j in range(0,n):
            if j == i:
                continue
            expr = (x-eixox[j])/(eixox[i]-eixox[j])
            produto *= expr
        
        soma += eixoy[i]*produto

    P = lambdify(x, soma, 'numpy')

    x = np.linspace(-100,100,1000)
    y = P(x)

    st.write(nsimplify(soma))

    fig = go.Figure()
    fig.add_trace(go.Scatter(x=x, y=y,
                mode='lines',
                name='Lagrange',
                line=dict(color='blue')))



    fig.update_layout(
        title= f"Interpolação de Lagrange",
        xaxis_title="x",
        yaxis_title="f(x)",
        showlegend=True,
        template="plotly_dark",  # fundo escuro
        width=800,
        height=400)

    st.plotly_chart(fig)


except Exception as e:
    st.error(f"Erro: {e}")


    
    
    
