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
	if u.groups.all()[0].name== 'secretaria' and rol == 'secretaria':
		return True
	elif u.groups.all()[0].name== 'vendedor' and rol == 'vendedor':
		return True
	elif u.groups.all()[0].name== 'gerente':
		return True
	elif u.groups.all()[0].name== 'tecnico' and rol == 'tecnico':
		return True
	elif u.groups.all()[0].name== 'medico' and rol == 'medico':
		return True
	else:
		return False
