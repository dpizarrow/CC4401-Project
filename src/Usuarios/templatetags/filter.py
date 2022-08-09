from django import template

register = template.Library()


@register.filter
def filtro(datos, id):
    return datos.filter(playlist_iden=id)
