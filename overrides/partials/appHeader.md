{{ app.description }}

{% if app.homepage or app.url -%}
[{{ app_name }} Homepage]({{ app.homepage or app.url }})
{% endif -%}

{% if app.licence_type == "proprietary" -%}

!!! warning
    {{ app_name }} is proprietary software. Make sure you meet the [requirements for it's usage](#licences).

{% endif -%}

## Available Modules

{% include "partials/appVersion.html" -%}

{% if app.network_licences.length > 0 -%}

## Licences

{% include "partials/appNetworkLicence.html" -%}

{% endif -%}
