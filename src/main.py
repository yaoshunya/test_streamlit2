import streamlit as st
import yaml
from func1 import func
import os

st.write(os.listdir())
#st.write(os.listdir('..'))
st.write(os.listdir('data/'))


with open('data/user_info.yml') as file:
    config = yaml.load(file, Loader=yaml.SafeLoader)

def main():
    func()
    st.write('Hello world')
    st.write(config)

main()