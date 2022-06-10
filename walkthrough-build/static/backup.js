{% for school in school_object_list %}
{% if school.district_x == district.district %}
{% if school.lat != "no_result" %}
console.log(feature)
var marker = L.circleMarker([{{ school.lat }}, { { school.lon } }], {
    stroke: true,
        color: '#1D8ACB',
            weight: 1,
                opacity: 1,
                    radius: 5,
                        fill: true,
                            fillOpacity: 0.2,
        }).addTo(map);

{% endif %}
{% endif %}
{% endfor %}
