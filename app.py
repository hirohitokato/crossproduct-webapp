import streamlit as st
import numpy as np

def main():

    vectorA, vectorB = st.columns(2)
    # ベクトルA
    with vectorA:
        st.header('vector A:')
        a_x = st.slider(key='a_x',
                        label='x',
                        min_value=-10,
                        max_value=10,
                        value=0)
        a_y = st.slider(key='a_y',
                        label='y',
                        min_value=-10,
                        max_value=10,
                        value=1)
        a_z = st.slider(key='a_z',
                        label='z',
                        min_value=-10,
                        max_value=10,
                        value=2)
    # ベクトルB
    with vectorB:
        st.header('vector B:')
        b_x = st.slider(key='b_x',
                        label='x',
                        min_value=-10,
                        max_value=10,
                        value=0)
        b_y = st.slider(key='b_y',
                        label='y',
                        min_value=-10,
                        max_value=10,
                        value=0)
        b_z = st.slider(key='b_z',
                        label='z',
                        min_value=-10,
                        max_value=10,
                        value=0)
                        
    va = np.array([a_x, a_y, a_z])
    vb = np.array([b_x, b_y, b_z])
    cross = np.cross(va, vb)
    st.write(f'cross product: {cross}')

if __name__ == '__main__':
    main()
