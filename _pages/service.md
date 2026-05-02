---
title: "Service"
layout: gridlay
sitemap: false
permalink: /service/
---

## Service

{% if site.data.service %}
<div class="section-card">
<ul>
{% for item in site.data.service.service_activities %}
  <li>
    <strong>{{ item.role }}</strong>: 
    {% if item.web %}
      <a href="{{ item.web }}" target="_blank">{{ item.description }}</a>.
    {% else %}
      {{ item.description }}.
    {% endif %}
    {% if item.location %} {{ item.location }}. {% endif %}
    {{ item.year }}.
  </li>
{% endfor %}
</ul>
</div>
{% endif %}

