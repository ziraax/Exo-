
def somme(a,b=0,*arg):
  s=a+b
  for i in arg:
    s+=i
  return s
def Valeur_Pi(e):
  s1=1
  s2=s1-1/3
  i=2
  while abs(s1-s2)/2>=e:
    s1=s2
    s2=s2+(-1)**i/(2*i+1)
    i+=1
  print(4*s2)
def racine_carre(x,e):
  A=1 # on met dans A la valeur U0=1
  B=(A+x/A)/2 # on met dans B la valeur U1    
  while abs(A-B)/2>e: # on cherche la valeur de A=Un telque A=Un preque égale à B=U{n+1}
    A=B
    B=(A+x/A)/2
  return B
def Rang_uk(k):
  A=0.5
  rang = 0
  while A<=k:
    A=(A+1)/2
    rang +=1
  return rang
print(Rang_uk(0.999999))
