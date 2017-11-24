from django import template

register = template.Library()

@register.filter(name='addclass_type')
def addclass_type(value, arg):
    arg_list = arg.split(',')
    try:
        return_value = value.as_widget(attrs={'class': arg_list[0], 'type': arg_list[1]})
    except:
        return
    return return_value

@register.filter(name='addclass')
def addclass(value, arg):
    return value.as_widget(attrs={'class': arg})


@register.filter(name='addclass_type_step')
def addclass_type_step(value, arg):
    arg_list = arg.split(',')
    try:
        return_value = value.as_widget(attrs={'class': arg_list[0], 'type': arg_list[1], 'step': arg_list[2]})
    except:
        return
    return return_value
