from django.core.exceptions import PermissionDenied

class PermisosMixin:
	rol = None
	def dispatch(self,request,*args,**kwargs):
		if check(request,self.rol):
			return super().dispatch(request,*args,**kwargs)
		else:
			raise PermissionDenied

def check(request,rol):
	u = request.user
	if u.groups.all()[0].name and rol == 'secretaria':
		print("Hola soy S")
		return True
	elif u.groups.all()[0].name and rol == 'vendedor':
		print("Hola soy V")
		return True
	elif u.groups.all()[0].name and rol == 'gerente':
		print("Hola soy G")
		return True
	elif u.groups.all()[0].name and rol == 'tecnico':
		print("Hola soy T")
		return True
	elif u.groups.all()[0].name and rol == 'medico':
		print("Hola soy M")
		return True
	else:
		print("Hola soy dAVIsito")
		return False
