# coding: utf-8
from __future__ import unicode_literals

from django import template


register = template.Library()


def parse_args(args):
    data = {}
    for arg in args:
        parts = arg.split('=', 1)
        if len(parts) > 1:
            value = parts[1][1:-1]
        else:
            value = True
        data[parts[0]] = value
    return data


@register.tag
def inkrow(parser, token):
    nodelist = parser.parse(('endinkrow',))
    parser.delete_first_token()
    args = token.split_contents()
    parsed_args = parse_args(args[1:])
    return RowNode(nodelist, parsed_args)


@register.tag
def inkcolumn(parser, token):
    nodelist = parser.parse(('endinkcolumn',))
    parser.delete_first_token()
    args = token.split_contents()
    parsed_args = parse_args(args[1:])
    return ColumnNode(nodelist, parsed_args)


class RowNode(template.Node):
    def __init__(self, nodelist, args):
        self.nodelist = nodelist

    def render(self, context):
        content = self.nodelist.render(context)
        return ('<table class="row"><tr>{content}</tr></table>'
                .format(content=content))


class ColumnNode(template.Node):
    def __init__(self, nodelist, args):
        self.nodelist = nodelist
        self.columns = args.pop('columns')
        self.is_last = args.pop('last', False)
        self.td_classes = args.keys()

    def render(self, context):
        tpl = ('<td class="wrapper{last_class}">'
               '<table class="{columns} columns"><tr>'
               '<td class="{td_classes}">{content}</td>'
               '<td class="expander"></td>'
               '</tr></table>'
               '</td>')

        content = self.nodelist.render(context)
        if 'center' in self.td_classes:
            content = '<center>{}</center>'.format(content)

        return tpl.format(columns=self.columns, content=content,
                          last_class=' last' if self.is_last else '',
                          td_classes=' '.join(self.td_classes))
