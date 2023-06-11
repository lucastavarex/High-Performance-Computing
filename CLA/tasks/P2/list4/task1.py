import cla

print("╔════════════════════════════════════════╗")
print("║ Task1(P2)-Computacional Linear Algebra ║")
print("║        Professor: Luis Sagrilo         ║")
print("║                                        ║")
print("║Student1:Thiago Dias   |  DRE: XXXXXXXXX║")
print("║Student2:Lucas Tavares |  DRE: 120152739║")
print("║                                        ║")
print("║                  2023.1                ║")
print("╠════════════════════════════════════════╣")
print("║                                        ║")
print("║      Welcome to our program, Tchê!     ║")
print("║                                        ║")
print("╚════════════════════════════════════════╝")


#Sistema de equações do exercício 3 da Task1
f1 = "16*(x**4) + 16*(y**4) + z**4 - 16"        
f2 = "x**2 + y**2 + z**2 - 3"                   
f3 = "x**3 - y + z - 1"                        

print ("==> System of Equations:")
print ("- 1st Equation: {} = 0".format(f1))
print ("- 2nd Equation: {} = 0".format(f2))
print ("- 3rd Equation: {} = 0".format(f3))

#Obs: Nosso código resolve sistemas nxn. Basta acrescentar as equações acima e adaptar o código (***) 

# (***)Adapte o código a seguir para resolver sistemas nxn
print("╔═══════════════════╗")
print("║  Newton's Method  ║")
print("╚═══════════════════╝") 
print ("-> {}".format(cla.equations([f1, f2, f3], ['x','y','z'], [1, 1, 1], method='newton')))
print("╔═══════════════════╗")
print("║ Broyden's Method  ║")
print("╚═══════════════════╝")
print ("->  {}".format(cla.equations([f1, f2, f3], ['x','y','z'], [1, 1, 1], method='broyden')))