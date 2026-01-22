"""CRIADA APENAS PARA ESTUDO
    essas são permissões personalizadas que 
    funcionam juntamente com a configuração das permissões de usuário 
    a partir do painel de admin do Django. 
"""


'''from rest_framework import permissions


class GenrePermissionClass(permissions.BasePermission):

    def has_permission(self, request, view):
        if request.method in ['GET', 'HEAD', 'OPTIONS']:
            return request.user.has_perm('genres.view_genre')
        
        if request.method == 'POST':
            return request.user.has_perm('genres.add_genre')
        
        if request.method in ['PATCH', 'PUT']:
            return request.user.has_perm('genres.change_genre')

        if request.method == 'DELETE':
            return request.user.has_perm('genres.change_genre')

        return False
'''        