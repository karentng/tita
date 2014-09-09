from django import template

register = template.Library()

@register.tag(name="mypanel")
def do_panel(parser, token):
    nodelist = parser.parse(('endmypanel',))
    args = token.split_contents()[1:]
    parser.delete_first_token()
    return UpperNode(nodelist, *args)

class UpperNode(template.Node):
    def __init__(self, nodelist, title="'panelcillo'", paneltype="'primary'"):
        self.nodelist = nodelist
        self.title = template.Variable(title)
        self.paneltype = template.Variable(paneltype)
    def render(self, context):
        content = self.nodelist.render(context)
        title = self.title.resolve(context)
        paneltype = self.paneltype.resolve(context)
        return """
            <div class="panel panel-%(paneltype)s">
                <div class="panel-heading">
                    <h4 class="panel-title">%(title)s</h4>
                </div>
                <div class="panel-body">
                    %(content)s
                </div>
            </div>
        """ % locals()