def weight_on_planets():
   weight = int(input("What do you weigh on earth? "))
   mars = weight * 0.38
   jup = weight * 2.34
   print("\nOn Mars you would weigh {0} pounds.\nOn Jupiter you would weigh {1} pounds.".format(mars, jup))

   
   
if __name__ == '__main__':
   weight_on_planets()
