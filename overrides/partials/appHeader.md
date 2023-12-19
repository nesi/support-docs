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
<!-- Uncomment this if we make a good page on modues -->
<!-- _See [environment modules]() for more info on how NeSI uses modules._ -->

{% if app.network_licences -%}

## Licences

<p>The following network licence servers can be accessed from the NeSI cluster.</p>
{% include "partials/appNetworkLicence.html" -%}
<p>If you do not have access, or want a server connected {% include "partials/support_request.html" %}.</p>

{% endif -%}
