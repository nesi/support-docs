<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.6.1/jquery.min.js"></script>
<script src="//d3js.org/d3.v3.min.js"></script>
{% include 'statuspage-widget.js' %}
<script>
    var scheduledColumn = $('#scheduled-column');
    var incidentsColumn = $('#incidents-column');
    var formatTime = d3.time.format("%d/%m/%Y %H%M");
    var sp = new StatusPage.page({ page: 'nbt2wg9kltqd' });
    sp.summary({
        success: function (data) {
            if (data.components.length) {
                data.components.filter(d => d.group_id == null).forEach(function (d, i) {
                    d3.select("#componentsstatus").selectAll("span")
                        .data([d])
                        .enter()
                        .append("svg")
                        .attr("width", 16)
                        .attr("height", 16)
                        .append("circle")
                        .attr("r", 8)
                        .attr("cx", 8)
                        .attr("cy", 8)
                        .style("fill", function (d) {
                            return d.status == "operational" ? "green" : "orange";
                        })
                        .append("title")
                        .text(d => d.name)
                })
            }
            if (data.scheduled_maintenances.length) {
                data.scheduled_maintenances.forEach(function (d, i) {

                    d3.select("#scheduled-column").selectAll("ul")
                        .data([d])
                        .enter().append("li")
                        .append("a")
                        .attr("href", d => d.shortlink)
                        .text(d => `${d.name} - ${formatTime(new Date(d.scheduled_for))}`)
                    // format date/time nicer!
                })
                d3.selectAll(".statuspage-scheduled").style("display", "block")
            } else if (data.scheduled_maintenances.length == null) {
                d3.select("#scheduled-column").selectAll("ul")
                    .text("No scheduled maintenance")
            }
            if (data.incidents.length) {
                d3.selectAll(".statuspage-incidents").style("display", "block")
                data.incidents.forEach(function (d, i) {
                    d3.select("#incidents-column").selectAll("ul")
                        .data([d])
                        .enter().append("li")
                        .append("a")
                        .attr("href", d => d.shortlink)
                        .text(d => d.name)
                })
            } else if (data.incidents.length == null) {
                d3.select("#incidents-column").selectAll("ul")
                    .text("No reported incident")
            }

            /*
            d3.select("#nonoperational").selectAll("li")
              .data(data.components.filter(d => d.status!=='operational'))
              .enter().append("li")
              .text(e => `${e.name}: ${e.status}, created: ${e.created_at}, updated: ${e.updated_at}`)
            */
        }
    });
</script>
Subscribe to status updates or see all details:
[status.nesi.org.nz](http://status.nesi.org.nz). Learn more about
[status notifications at
NeSI.](https://support.nesi.org.nz/hc/en-gb/articles/360000751636)
