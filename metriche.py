# Genera tutte le metriche n,3
def metriche(a,b,c,n,m,metrica):

  l=len(metrica)
  completo=a>0 and b>0 and c>0
  if l==n and completo:
    print("metrica=",metrica)
  else:
    if a+b+c<=n and a<=n-m+1 and l>=0:
      metriche(a+1,b,c,n,m,metrica+"a")

    if a+b+c<=n and b<=n-m+1 and l>=1 and a>0:
      metriche(a,b+1,c,n,m,metrica+"b")

    if a+b+c<=n and c<=n-m+1 and l>=2 and b>0:
      metriche(a,b,c+1,n,m,metrica+"c")

metriche(0,0,0,3,3,"")
