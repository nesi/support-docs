There are 4 dual socket nodes on blade, connected to a single Aries
(switch) chip, and there are 16 Aries chips in a chassis connected to
the backplane. On Māui, this implies each chassis contains 64 nodes, or
2,560 Skylake cores. There are 3 chassis in an XC50 cabinet, and two
XC50 cabinets are an Electrical \"group\". Maui has 1.5 groups.

![UPM\_html\_2d91e9cdd34d272d.gif](https://support.nesi.org.nz/hc/article_attachments/360000488576/UPM_html_2d91e9cdd34d272d.gif){width="298"
height="263"}

The performance characteristics are:

1.  Intra-Chassis
    a.  Backplane
    b.  15 links in the backplane
    c.  Rank 1 (green) Network
    d.  14 Gbps
2.  Intra-group
    a.  Copper cables
    b.  15 links in 5 connectors
    c.  Rank 2 (black) Network
    d.  14 Gbps
3.  Inter-group links
    a.  Optical
    b.  10 links in 5 connectors
    c.  Rank 3 (blue) Network
    d.  12.5 Gbps

The centrepiece of the Aries network is dynamic routing through a large
variety of different routes from Aries A to Aries B. Therewith the
effective bandwidth is increased significantly. These dynamic routing on
alternative paths is applied on all 3 levels of the network.
