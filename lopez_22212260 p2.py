"""
Práctica 1:Diseño de controladores


Departamento de Ingeniería Eléctrica y Electrónica, Ingeniería Biomédica
Tecnológico Nacional de México [TecNM - Tijuana]
Blvd. Alberto Limón Padilla s/n, C.P. 22454, Tijuana, B.C., México


Nombre del alumno: Santiago Lopez Lopez
Número de control: 22212260
Correo institucional: l22212260@tectijuana.edu.mx


Asignatura: Modelado de Sistemas Fisiológicos
Docente: Dr. Paul Antonio Valle Trujillo; paul.valle@tectijuana.edu.mx
"""
# Instalar librerias en consola
#!pip install control
#!pip install slycot


# Librerías para cálculo numérico y generación de gráficas
import numpy as np
import math as m
import matplotlib.pyplot as plt
import control as ctrl



# Datos de la simulación
x0,t0,tend,dt,w,h = 0,0,10,1e-3,7,3.5
n = round((tend- t0)/dt)+1
t = np.linspace(t0,tend,n)
u1 = np.ones(n)
u2 = np.zeros(n); u2[round(1/dt):round(2/dt)]=1
u3 = t/tend 
u4 = np.sin(m.pi/2*t)



# Componentes del circuito RLC y función de transferencia
R,L,C = 9e3,33e-3,22e-6
num = [C*L*R,C*R**2+L,R]
den = [3*C*L*R,5*C*R**2+L,2*R]
sys = ctrl.tf(num,den)
print(f"funcion de transferencia del sistema: {sys}")




# Componentes del controlador
kI= 525.5097
Cr = 1e-6
Re = 1/(kI*Cr)
print(f"El valor de la capacitancia propuesta de Cr es de {Cr} Faradios.")
print(f"El valor de la resistencia de Re es de {Re} ohms.")


numPID = [1]
denPID = [Re*Cr,0]
PID = ctrl.tf(numPID,denPID)
print(f"La funcion de transferencia del controlador PID es {PID}.")
# Sistema de control en lazo cerrado
X = ctrl.series(PID,sys)
sysPID = ctrl.feedback(X,1,sign = -1)
print (f"Funcion de transferencia del sistem de control en lazo cerrado {sysPID}")







# Respuesta del sistema en lazo abierto y en lazo cerrado
clr1 = np.array([0.93,0.64,0.35])
clr2 = np.array([0.23,0.67,0.20])
clr6 = np.array([1.00,0.29,0.76])

_,PAu1 = ctrl.forced_response(sys,t,u1,x0)
_,PAu2 = ctrl.forced_response(sys,t,u2,x0)
_,PAu3 = ctrl.forced_response(sys,t,u3,x0)
_,PAu4 = ctrl.forced_response(sys,t,u4,x0)


_,pìdu1 = ctrl.forced_response(sysPID,t,u1,x0)
_,pìdu2 = ctrl.forced_response(sysPID,t,u2,x0)
_,pìdu3 = ctrl.forced_response(sysPID,t,u3,x0)
_,pìdu4 = ctrl.forced_response(sysPID,t,u4,x0)

fg1= plt.figure()
plt.plot(t,u1,'-',color = clr1,label = 'Ve(t)')
plt.plot(t,PAu1,'--',color = clr2,label = 'Vs(t)')
plt.plot(t,pìdu1,':',linewidth = 4,color = clr6,label = 'PID(t)')
plt.xlim(0,10); plt.xticks(np.arange(0,11,1))
plt.ylim(0,1.1); plt.yticks(np.arange(0,1.2,0.1))
plt.xlabel('t[s]',fontsize = 11)
plt.ylabel('Vi(t) [V]',fontsize = 11)
plt.legend(bbox_to_anchor = (0.5,-0.2),loc = 'center', ncol = 3, 
    fontsize = 9,frameon = True)

plt.show()
fg1.savefig('step_python.pdf', bbox_inches = 'tight')

fg2= plt.figure()
plt.plot(t,u2,'-',color = clr1,label = 'Ve(t)')
plt.plot(t,PAu2,'--',color = clr2,label = 'Vs(t)')
plt.plot(t,pìdu2,':',linewidth = 4,color = clr6,label = 'PID(t)')
plt.xlim(0,10); plt.xticks(np.arange(0,11,1))
plt.ylim(0,1.1); plt.yticks(np.arange(0,1.2,0.2))
plt.xlabel('t[s]',fontsize = 11)
plt.ylabel('Vi(t) [V]',fontsize = 11)
plt.legend(bbox_to_anchor = (0.5,-0.2),loc = 'center', ncol = 3, 
    fontsize = 9,frameon = True)

plt.show()
fg2.savefig('step_python2.pdf', bbox_inches = 'tight')

fg3= plt.figure()
plt.plot(t,u3,'-',color = clr1,label = 'Ve(t)')
plt.plot(t,PAu3,'--',color = clr2,label = 'Vs(t)')
plt.plot(t,pìdu3,':',linewidth = 4,color = clr6,label = 'PID(t)')
plt.xlim(0,10); plt.xticks(np.arange(0,11,1))
plt.ylim(0,1.1); plt.yticks(np.arange(0,1.2,0.1))
plt.xlabel('t[s]',fontsize = 11)
plt.ylabel('Vi(t) [V]',fontsize = 11)
plt.legend(bbox_to_anchor = (0.5,-0.2),loc = 'center', ncol = 3, 
    fontsize = 9,frameon = True)

plt.show()
fg3.savefig('step_python3.pdf', bbox_inches = 'tight')

fg4= plt.figure()
plt.plot(t,u4,'-',color = clr1,label = 'Ve(t)')
plt.plot(t,PAu4,'--',color = clr2,label = 'Vs(t)')
plt.plot(t,pìdu4,':',linewidth = 4,color = clr6,label = 'PID(t)')
plt.xlim(0,10); plt.xticks(np.arange(0,11,1))
plt.ylim(0,1.1); plt.yticks(np.arange(-1.2,1.4,0.2))
plt.xlabel('t[s]',fontsize = 11)
plt.ylabel('Vi(t) [V]',fontsize = 11)
plt.legend(bbox_to_anchor = (0.5,-0.2),loc = 'center', ncol = 3, 
    fontsize = 9,frameon = True)

plt.show()
fg4.savefig('step_python4.pdf', bbox_inches = 'tight')