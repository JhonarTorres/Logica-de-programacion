import matplotlib.pyplot as plt
x=[3,4,5,6,6,5,4,3,2,1,0,0,1,2,3]
y=[0,1,2,3,4,5,5,4,5,5,4,3,2,1,0]
plt.plot(x,y,color='red',linewidth=3)
plt.scatter(x,y,color='red',s=48)
plt.xlabel('Eje x')
plt.ylabel('Eje y')
plt.title('Dibujo de corazon')
plt.legend()
plt.savefig('Dibujo_de_Corazon')
plt.show()
