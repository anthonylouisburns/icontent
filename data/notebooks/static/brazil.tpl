{#
i found this very useful
https://realpython.com/blog/python/primer-on-jinja-templating/

these templates are jinja templates
http://jinja.pocoo.org/docs/dev/api/#basics
#}

{%- extends 'full.tpl' -%}
{% block body %}
 </div>
{% for css in resources.css -%}
    <link rel="stylesheet" href="{{ css }}">
{% endfor %}
<div id="headerbox">
    <h1>BRAZIL</h1>
</div>
{% include resources.sideleft ignore missing%}
<div id="main">
{{ super() }}
</div>
{%- endblock body %}