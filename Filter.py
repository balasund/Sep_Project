import pandas as pd
import streamlit as st


def A():
  B = pd.read_excel("mark.xlsx")
  A1 = B[["Name", "Math"]]
  return A1

def C():
  D = pd.read_excel("mark.xlsx")
  C1 = D[["Name", "Phy"]]
  return C1

def E():
  df = pd.read_excel("mark.xlsx")
  E1 = df[["Name", "Che"]]
  return E1

def F():
  df2 = pd.read_excel("mark.xlsx")
  F1 = df2[["Name", "Eng"]]
  return F1

def G():
  df3 = pd.read_excel("mark.xlsx")
  G1 = df3[["Name", "Bio"]]
  return G1  

def H():
  df4 = pd.read_excel("mark.xlsx")
  H1 = df4[["Name", "Tamil"]]
  return H1


st.title("Students Mark") 

key = st.text_input("How can I help you ...... ")

Y = key.lower()

T = ['show','the','me','mark','list','details','give','report','detail','register','of']

X = Y.split()

filter = [word for word in X if word.lower() not in T]

key = " ".join(filter)


if key =='Math' or key == 'math' or key == 'MATH' or key == 'maths' or key == 'MATHS':
    a1 = A()
    st.write(a1)

elif key == 'Phy' or key == 'phy' or key == 'PHY' or key == 'physics' or key == 'PHYSICS':
    a2 = C()
    st.write(a2)
    

elif key == 'Che' or key == 'che' or key == 'CHE' or key == 'chemistry' or key == 'CHEMISTRY':
    a3 = E()
    st.write(a3)
  

elif key == 'Eng' or key == 'eng' or key == 'ENG' or key == 'english' or key == 'ENGLISH':
    a4 = F()
    st.write(a4)

elif key == 'Bio' or key == 'bio' or key == 'BIO' or key == 'biology' or key == 'BIOLOGY':
    a5 = G()
    st.write(a5)

elif key == 'Tamil' or key == 'tamil' or key == 'TAMIL':
    a6 = H()
    st.write(a6)




