# Задача-1: Написать класс для фигуры-треугольника, заданного координатами трех точек.
# Определить методы, позволяющие вычислить: площадь, высоту и периметр фигуры.

import math

class triangle: 

	def ___init___(self,ax,ay,bx,by,cx,cy):
		self.ax=ax
		self.ay=ay
		self.bx=bx
		self.by=by
		self.cx=cx
		self.cy=cy


	def lenght (self):
		a= (((self.ax - self.bx)**2)+((self.ay - self.by)**2))*0,5
		b= (((self.ax - self.cx)**2)+((self.ay - self.cy)**2))*0,5
		c= (((self.bx - self.cx)**2)+((self.by - self.cy)**2))*0,5


	def perimeter (self):
		P= self.length(a) + self.clength(b) + self.length(c)
		return(P)


	def area (self):
		ph= self.perimeter()/2
		S= sqr((ph - self.length(a))*(ph - self.length(b))*(ph - self.length(c))*ph)
		return(S)



	def hight (self):
		A=self.area()
		h= (2*A)/self.length(a)
		return(h)




# Задача-2: Написать Класс "Равнобочная трапеция", заданной координатами 4-х точек.
# Предусмотреть в классе методы:
# проверка, является ли фигура равнобочной трапецией;
# вычисления: длины сторон, периметр, площадь.

На большее времени не хатило, к сожелению. Но эту тему обязательно ещё буду ковырять в ближайщее время.

