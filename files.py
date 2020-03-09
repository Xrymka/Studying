import os
st = os.path.join('C:/Users','Katerina','Desktop','st.txt')
print(st)
             
with open(st, 'r') as f:
    print(f.read())
