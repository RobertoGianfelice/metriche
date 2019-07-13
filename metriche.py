# Genera le metriche 5,3 con il solo schema 3,1,1
a=3
b=1
c=1

def metriche(a,b,c,metrica):
  l=len(metrica)
  if len(metrica)==5:
    print("metrica=",metrica)
  else:
    if a>0:
      metriche(a-1,b,c,metrica+"a")

    if b>0 and l>=1:
      metriche(a,b-1,c,metrica+"b")

    if c>0 and l>=2:
      metriche(a,b,c-1,metrica+"c")

metriche(3,1,1,"")
