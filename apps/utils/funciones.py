class PermisosMixin:
	rol = None
	def dispatch(self,request,*args,**kwargs):
		if check(request,self.rol):
			return super().dispatch(request,*args,**kwargs)
		else:
			raise PermissionDenied

def check(request,rol):
	u = request.user
	if u.Trabajador and rol == 'trabajador':
		return True
	elif not (u.Trabajador) and rol == 'stalker':
		return True
	else:
		return False