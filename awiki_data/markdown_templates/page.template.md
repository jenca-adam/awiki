## Reference
{% for author in page.author_names %}{{ author.last_name }}, {{ author.first_names }}{% if not loop.last %} {% endif %}{% endfor %} ({{ page.published.year }}) '{{ page.title }}', {% if page.jref is not none %}*{{page.jref}}*. {% endif %}. {% if page.published is not none %}(Published: {{ page.published.day }} {{ page.published.strftime('%b') }} {{ page.published.year }}){% endif %}
## Abstract
{{ page.abstract }}
