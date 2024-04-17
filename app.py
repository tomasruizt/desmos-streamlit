import numpy as np
import streamlit as st
import sympy as sp
from sympy.abc import x

st.title("My Desmos Calculator")

col1, col2 = st.columns([2, 5])


with col1:
    st.subheader("Input")
    exp1: str = st.text_input("Expression for y", "exp(-x**2)", key="1")
    exp2: str = st.text_input("Expression for y", "x**2", key="2")
    try:
        rhs1 = sp.parse_expr(exp1)
        rhs2 = sp.parse_expr(exp2)
    except:
        st.error("Invalid expression")
        st.stop()

    st.markdown("**Equation(s):**")
    st.write(f"$${sp.latex(rhs1)}$$")
    st.write(f"$${sp.latex(rhs2)}$$")

xs = np.linspace(-2, 2, 100)

def ys(rhs: sp.Expr) -> np.ndarray:
    y_fn = sp.lambdify(x, rhs, ["numpy", "sympy"])
    return y_fn(xs)

with col2:
    st.plotly_chart(
        {
            "data": [
                {"x": xs, "y": ys(rhs1), "name": str(rhs1)},
                {"x": xs, "y": ys(rhs2), "name": str(rhs2)},
            ],
            "layout": {
                "title": "Equations"
            },
        },
        use_container_width=True,
    )
