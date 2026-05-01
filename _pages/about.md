---
title: "About"
layout: gridlay
sitemap: false
permalink: /about/
---

## About Me

<div class="section-card">
<div class="pi-card">
<img src="{{ site.url }}{{ site.baseurl }}/images/{{ site.photo }}" class="pi-photo" alt="{{ site.name }}" loading="lazy">
<div>
<h3 class="pi-name">{{ site.name }}</h3>
<p style="font-style: italic; color: var(--text-secondary);">{{ site.title }}, {{ site.institution }}</p>
<div class="pi-links">
{% if site.email %}<a href="mailto:{{ site.email }}" class="icon-link" title="Email"><i class="fa-solid fa-envelope"></i></a>{% endif %}
{% if site.links.cv and site.links.cv != "" %}<a href="{{ site.url }}{{ site.baseurl }}/{{ site.links.cv }}" class="icon-link" title="CV"><i class="ai ai-cv"></i></a>{% endif %}
{% if site.links.google_scholar and site.links.google_scholar != "" %}<a href="{{ site.links.google_scholar }}" class="icon-link" title="Google Scholar"><i class="ai ai-google-scholar"></i></a>{% endif %}
{% if site.links.github and site.links.github != "" %}<a href="{{ site.links.github }}" class="icon-link" title="GitHub"><i class="fa-brands fa-github"></i></a>{% endif %}
{% if site.links.researchgate and site.links.researchgate != "" %}<a href="{{ site.links.researchgate }}" class="icon-link" title="ResearchGate"><i class="ai ai-researchgate"></i></a>{% endif %}
</div>
{% if site.data.pi[0].education %}
<ul style="margin-top: var(--space-4);">
{% for education in site.data.pi[0].education %}
<li>{{ education | replace: "-","&#8211;" }}</li>
{% endfor %}
</ul>
{% endif %}
</div>
</div>
</div>


<div class="section-card">
  <h3>Current Positions</h3>
  <ul class="professional-list">
    <li>
      <strong>Assistant Professor</strong>, <a href="https://dc.exa.unrc.edu.ar/">National University of Río Cuarto (UNRC)</a> (2024 – Present)
    </li>
    <li>
      <strong>Associate Researcher</strong>, <a href="https://www.conicet.gov.ar/">CONICET</a> (2023 – Present)
    </li>
  </ul>
</div>


{% if site.data.projects %}
<div class="section-card">
<h3>Funded Projects</h3>
<ul>
{% for project in site.data.projects %}
  <li><strong>{{ project.title }}</strong> ({{ project.years }}): {{ project.description }}</li>
{% endfor %}
</ul></div>
{% endif %}


{% if site.data.grants %}
<div class="section-card">
<h3>Grants</h3>
<ul>
{% for grant in site.data.grants %}
<li>{{ grant.name }}</li>
{% endfor %}
</ul>
</div>
{% endif %}



