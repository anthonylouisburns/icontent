{#
i found this very useful
https://realpython.com/blog/python/primer-on-jinja-templating/

these templates are jinja templates
http://jinja.pocoo.org/docs/dev/api/#basics
#}

{%- extends 'full.tpl' -%}
{% block body %}
 </div>

<link rel="stylesheet" href="{{ resources.css }}">
<div id="headerbox">
    BRAZIL
</div>
{% include resources.sideleft ignore missing%}
<div id="main">
{{ super() }}
</div>
{%- endblock body %}