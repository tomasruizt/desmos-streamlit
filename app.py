import numpy as np
import streamlit as st
import sympy as sp
from sympy.abc import x, y

st.title("My Desmos Calculator")

col1, col2 = st.columns([2, 5])

def get_rhs(expression: str) -> sp.Expr:
    try:
        return sp.parse_expr(expression)
    except:
        st.error("Invalid expression")
        st.stop()

with col1:
    st.subheader("Input")
    n_eqs = st.number_input("Number of equations", min_value=1)
    exps = [st.text_input("Expression for y", "x**2", key=i) for i in range(n_eqs)]
    rhss = [get_rhs(exp) for exp in exps]


xs = np.linspace(-3, 3, 100)

def ys(rhs: sp.Expr) -> np.ndarray:
    y_fn = sp.lambdify(x, rhs, ["numpy", "sympy"])
    return y_fn(xs)

def latex(rhs: sp.Expr) -> str:
    return sp.latex(sp.Eq(y, rhs))

data = [{"x": xs, "y": ys(rhs), "name": "hello"} for rhs in rhss]

with col1:
    st.markdown("**Equation(s):**")
    for rhs in rhss:
        st.write(f"$${latex(rhs)}$$")

with col2:
    st.plotly_chart(
        {
            "data": data,
            "layout": {
                "title": "Equations",
                "xaxis": {"title": "x"},
                "yaxis": {"title": "y"},
            },
        },
        use_container_width=True,
    )
