import streamlit as st
import numpy as np
from matplotlib import pyplot as plt
import matplotlib.cm as cm

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

    # 計算                        
    va = np.array([a_x, a_y, a_z])
    vb = np.array([b_x, b_y, b_z])
    cross = np.cross(va, vb)

    # グラフのプロット
    st.write(f'cross product: {cross}')
    fig = plt.figure()
    ax = fig.gca(projection='3d')
    ax.set_xlim([-10,10])
    ax.set_ylim([-10,10])
    ax.set_zlim([-10,10])
    ax.set(xlabel='x', ylabel='y', zlabel='z')
    origin = np.zeros((3,3))
    vectors = np.array((va,vb,cross))
    cmap = cm.get_cmap(name='rainbow')

    ax.quiver(origin[:,0],origin[:,1],origin[:,2],
              vectors[:,0],vectors[:,1],vectors[:,2],
              colors=['blue', 'green', 'red'])
    st.pyplot(fig)


if __name__ == '__main__':
    main()
