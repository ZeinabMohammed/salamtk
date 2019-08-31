from rest_framework import permissions
class IsOwnerOrReadOnly(permissions.BasePermission):
	"""
	create custom permission allow only owner to edit it
	"""
	def has_object_permission(self, request,view, obj):
		#read allowd to all users
		#so we always allow GET, HEAD, OPTioNS
		if request.method in permissions.SAFE_METHODS:
			return True
		#write permissions only for allwed users:
		return obj.publisher == request.user.id