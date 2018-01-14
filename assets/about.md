---
layout: page
title: About
permalink: /about/
---

### About

#### Roboteers




<ul>
{% for person in site.data.people %}
 {%  assign p = person[1]  %}

  <li>
    <a href="/roboteer/{{person[0]}}">
      {{ p.name }}
    </a>
  </li> 
{% endfor %}
</ul>