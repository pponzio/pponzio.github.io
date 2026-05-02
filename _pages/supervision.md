---
title: "Supervision"
layout: gridlay
sitemap: false
permalink: /supervision/
---

## Supervision

<div class="section-card">
  <h3>Ph.D. Students</h3>
  <ul>
  {% for student in site.data.phd_students %}
    <li>
    <strong>{{ student.name }}</strong>, {{ student.institution }}. 
    <small>({{ student.status }}{% if student.completion_date %}: {{ student.completion_date }}{% endif %})</small>
    </li>
  {% endfor %}
  </ul>
</div>


<div class="section-card">
  <h3>Undergraduate Students</h3>
  <ul>
  {% for student in site.data.undergrad_students %}
    <li>
    <strong>{{ student.name }}</strong>, {{ student.institution }}. 
    <small>({{ student.status }}{% if student.completion_date %}: {{ student.completion_date }}{% endif %})</small>
    </li>
  {% endfor %}
  </ul>
</div>
