#!/usr/bin/env python3
"""Draws the diagrams for docs/Software/Parallel_Computing/NUMA_Domains.md, as SVG files.

The first three share one layout, so readers can map the story onto the real node:
  1. NUMA_Domains_Lab_Story.svg   - two buildings of labs; a scientist fetches samples from near and far fridges
  2. NUMA_Domains_Milan_Node.svg  - a Milan node drawn the same way: sockets, NUMA domains, cores, memory
  3. NUMA_Domains_Genoa_Node.svg  - a Genoa node drawn the same way (8 NUMA domains of 21 cores)
  4. NUMA_Domains_Desktop_vs_Genoa.svg - a desktop processor and a Genoa node, to scale
  5. NUMA_Domains_Cores_Spread.svg - a job's cores in one NUMA domain, and spread over three
  6. NUMA_Domains_Thread_Moves.svg - a thread before and after the operating system moves it

Run it from the top of the repository. It only needs Python 3:

    python3 misc/plot_numa_domains.py [OUTPUT_DIR]

OUTPUT_DIR defaults to docs/assets/images.
"""
import sys
from pathlib import Path

FONT = "Roboto, 'Helvetica Neue', Helvetica, Arial, sans-serif"
TEXT = "#001C36"          # REANNZ dark blue
MUTED = "#3F4E5C"
BUILDING_FILL = "#F5F6F7"
BUILDING_STROKE = "#5A6875"
ROOMS = [("#E2F5FB", "#007C99"), ("#E3F3EC", "#00765F")]  # (fill, stroke), alternating
CORE = "#8479B7"          # REANNZ purple: cores and scientists
MEM_FILL = "#FDEBD3"      # memory and fridges
MEM_STROKE = "#A85700"
LINK = "#C3C8C8"          # REANNZ grey: socket link and footbridge
GREEN, ORANGE, RED = "#00765F", "#A85700", "#B42318"

M = 20                    # outer margin
RW, RH, RG = 152, 122, 8  # room (lab / NUMA domain) width, height, gap
BP, BL = 10, 30           # building padding, building label height
BW = BP * 2 + RW * 2 + RG
BH = BL + RH * 2 + RG + BP
GAP = 84                  # gap between the two buildings (footbridge / socket link)
W = M * 2 + BW * 2 + GAP


def esc(s):
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


class Svg:
    def __init__(self, w, h, title, desc):
        self.w, self.h, self.title, self.desc = w, h, title, desc
        self.parts = []

    def add(self, s):
        self.parts.append(s)

    def rect(self, x, y, w, h, fill, stroke="none", sw=1.5, rx=6, dash=None):
        d = f' stroke-dasharray="{dash}"' if dash else ""
        self.add(f'<rect x="{x:g}" y="{y:g}" width="{w:g}" height="{h:g}" rx="{rx:g}" '
                 f'fill="{fill}" stroke="{stroke}" stroke-width="{sw:g}"{d}/>')

    def text(self, x, y, s, size=13, weight="normal", anchor="start", fill=TEXT, rotate=False):
        r = f' transform="rotate(-90 {x:g} {y:g})"' if rotate else ""
        self.add(f'<text x="{x:g}" y="{y:g}" font-size="{size:g}" font-weight="{weight}" '
                 f'text-anchor="{anchor}" fill="{fill}"{r}>{esc(s)}</text>')

    def line(self, x1, y1, x2, y2, stroke, sw=1.5, dash=None):
        d = f' stroke-dasharray="{dash}"' if dash else ""
        self.add(f'<line x1="{x1:g}" y1="{y1:g}" x2="{x2:g}" y2="{y2:g}" stroke="{stroke}" '
                 f'stroke-width="{sw:g}"{d}/>')

    def path(self, d, stroke, sw=2.5, dash=None, marker=None):
        da = f' stroke-dasharray="{dash}"' if dash else ""
        m = f' marker-end="url(#{marker})"' if marker else ""
        self.add(f'<path d="{d}" fill="none" stroke="{stroke}" stroke-width="{sw:g}" '
                 f'stroke-linejoin="round"{da}{m}/>')

    def badge(self, x, y, label, colour):
        self.add(f'<circle cx="{x:g}" cy="{y:g}" r="10" fill="#FFFFFF" stroke="{colour}" stroke-width="2"/>')
        self.text(x, y + 4.5, label, size=12.5, weight="bold", anchor="middle", fill=colour)

    def render(self):
        markers = "".join(
            f'<marker id="ah-{n}" viewBox="0 0 10 10" refX="8.5" refY="5" markerWidth="5" '
            f'markerHeight="5" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 z" fill="{c}"/></marker>'
            for n, c in (("green", GREEN), ("orange", ORANGE), ("red", RED), ("grey", MUTED)))
        return (
            f'<svg xmlns="http://www.w3.org/2000/svg" width="{self.w}" height="{self.h}" '
            f'viewBox="0 0 {self.w} {self.h}" role="img" aria-labelledby="title desc" '
            f'font-family="{FONT}">\n'
            f'<title id="title">{esc(self.title)}</title>\n<desc id="desc">{esc(self.desc)}</desc>\n'
            f'<defs>{markers}</defs>\n'
            f'<rect width="{self.w}" height="{self.h}" fill="#FFFFFF"/>\n'
            + "\n".join(self.parts) + "\n</svg>\n")


# ---------------------------------------------------------------- shared drawing

def scientist(svg, cx, top, fill=CORE):
    svg.add(f'<circle cx="{cx:g}" cy="{top + 6:g}" r="6" fill="{fill}"/>')
    svg.add(f'<path d="M{cx - 9:g},{top + 30:g} V{top + 21:g} Q{cx - 9:g},{top + 14:g} {cx - 2:g},{top + 14:g} '
            f'H{cx + 2:g} Q{cx + 9:g},{top + 14:g} {cx + 9:g},{top + 21:g} V{top + 30:g} Z" fill="{fill}"/>')


def fridge(svg, x, y, w=28, h=50):
    svg.rect(x, y, w, h, MEM_FILL, MEM_STROKE, sw=1.5, rx=4)
    svg.line(x, y + h * 0.36, x + w, y + h * 0.36, MEM_STROKE, sw=1.2)
    svg.line(x + w - 6, y + 5, x + w - 6, y + h * 0.36 - 5, MEM_STROKE, sw=2)
    svg.line(x + w - 6, y + h * 0.36 + 5, x + w - 6, y + h * 0.36 + 16, MEM_STROKE, sw=2)


def memory(svg, x, y, w=26, h=78, label="memory"):
    svg.rect(x, y, w, h, MEM_FILL, MEM_STROKE, sw=1.5, rx=3)
    svg.text(x + w / 2 + 4.5, y + h / 2, label, size=12, anchor="middle", rotate=True)


def cores_grid(svg, x, y, n, per_row, size=10, gap=3):
    for i in range(n):
        r, c = divmod(i, per_row)
        svg.rect(x + c * (size + gap), y + r * (size + gap), size, size, CORE, rx=1.5)


def two_buildings(svg, top, label, draw_room, link_label, room_label):
    """Two buildings (sockets) of 2 x 2 rooms (labs / NUMA domains), with a link between them."""
    rooms = {}
    for b in range(2):
        bx = M + b * (BW + GAP)
        svg.rect(bx, top, BW, BH, BUILDING_FILL, BUILDING_STROKE, sw=1.8, rx=8)
        svg.text(bx + BP, top + 21, label(b), size=14.5, weight="bold")
        for r in range(4):
            row, col = divmod(r, 2)
            rx = bx + BP + col * (RW + RG)
            ry = top + BL + row * (RH + RG)
            fill, stroke = ROOMS[(row + col) % 2]
            svg.rect(rx, ry, RW, RH, fill, stroke, sw=1.8, rx=6)
            n = b * 4 + r
            svg.text(rx + 9, ry + 19, room_label(n), size=13.5, weight="bold")
            rooms[n] = (rx, ry)
            draw_room(svg, n, rx, ry)
    # link between the buildings, level with the top row of rooms
    lx = M + BW - 2
    ly = top + BL + 74
    svg.rect(lx, ly, GAP + 4, 40, LINK, sw=0, rx=0)
    svg.text(M + BW + GAP / 2, ly + 58, link_label, size=12.5, anchor="middle", fill=MUTED)
    return rooms, (lx, ly)


def legend(svg, x, y, items, col_w):
    for i, (kind, label) in enumerate(items):
        cx = x + (i % 2) * col_w
        cy = y + (i // 2) * 26
        if kind == "core":
            svg.rect(cx + 4, cy - 11, 13, 13, CORE, rx=1.5)
        elif kind == "scientist":
            scientist(svg, cx + 10, cy - 20)
        elif kind == "you":
            scientist(svg, cx + 10, cy - 20, fill=TEXT)
        elif kind == "memory":
            svg.rect(cx, cy - 13, 22, 17, MEM_FILL, MEM_STROKE, sw=1.5, rx=3)
        elif kind == "room":
            svg.rect(cx, cy - 13, 22, 17, ROOMS[0][0], ROOMS[0][1], sw=1.8, rx=3)
        elif kind == "building":
            svg.rect(cx, cy - 13, 22, 17, BUILDING_FILL, BUILDING_STROKE, sw=1.8, rx=3)
        elif kind == "link":
            svg.rect(cx, cy - 10, 22, 11, LINK, rx=0)
        svg.text(cx + 32, cy, label, size=13)


# ---------------------------------------------------------------- 1: the lab story

def fig_lab_story():
    top = 46
    key_top = top + BH + 34
    H = key_top + 4 * 27 + 4
    svg = Svg(W, H, "Near and far memory, told as a story about labs",
              "Two buildings joined by a footbridge. Each building has 4 labs, and each lab has scientists "
              "and a fridge. A scientist in lab 0 fetches a sample from the fridge in their own lab (quick), "
              "from lab 1 in the same building (slower), and from lab 4 in the other building, over the "
              "footbridge (slowest).")
    svg.text(M, 28, "Scientists, labs and fridges", size=17, weight="bold")
    you = {}

    def draw_lab(svg, n, rx, ry):
        for i in range(4):
            cx = rx + 20 + i * 24
            scientist(svg, cx, ry + 30, fill=TEXT if (n == 0 and i == 0) else CORE)
            if n == 0 and i == 0:
                you["x"], you["y"] = cx, ry + 60
        fridge(svg, rx + RW - 38, ry + 12)

    rooms, (lx, ly) = two_buildings(svg, top, lambda b: f"Building {b}", draw_lab, "footbridge",
                                    lambda n: f"Lab {n}")
    x, y = you["x"], you["y"]
    lanes = {1: 80, 2: 93, 3: 106}   # relative to the top of lab 0
    ry0 = rooms[0][1]
    # each trip leaves the scientist, drops to its own lane, and walks to the fridge it needs
    for trip, dx, room, colour, dash, marker in (
            (1, 6, 0, GREEN, None, "ah-green"),
            (2, 0, 1, ORANGE, "7 4", "ah-orange"),
            (3, -6, 4, RED, "2.5 3.5", "ah-red")):
        lane = ry0 + lanes[trip]
        fx = rooms[room][0] + RW - 38 + 14
        svg.path(f"M{x + dx:g},{y + 2:g} V{lane:g} H{fx:g} V{rooms[room][1] + 12 + 50 + 3:g}",
                 colour, dash=dash, marker=marker)
    svg.badge(rooms[0][0] + RW - 60, ry0 + lanes[1], "1", GREEN)
    svg.badge(rooms[1][0] + RW - 60, ry0 + lanes[2], "2", ORANGE)
    svg.badge(lx + (GAP + 4) / 2, ry0 + lanes[3], "3", RED)

    y = key_top
    legend(svg, M, y, [("you", "a scientist who needs a sample")], 300)
    for label, colour, dash, words in (
            ("1", GREEN, "", "the fridge in their own lab (quickest)"),
            ("2", ORANGE, "7 4", "a lab down the corridor (slower)"),
            ("3", RED, "2.5 3.5", "a lab in the other building, across the footbridge (slowest)")):
        y += 27
        svg.line(M, y - 4, M + 24, y - 4, colour, sw=2.5, dash=dash or None)
        svg.badge(M + 42, y - 4, label, colour)
        svg.text(M + 60, y + 0.5, words, size=13)
    return svg


# ---------------------------------------------------------------- 2 and 3: real nodes, laid out like the labs

def fig_node(name, cores_per_socket, cores_per_domain, draw_cores):
    top = 46
    key_top = top + BH + 40
    H = key_top + 3 * 26 + 2
    svg = Svg(W, H, f"A {name} node and its 8 NUMA domains",
              f"Two sockets of {cores_per_socket} cores, joined by a socket link. Each socket is split into "
              f"4 NUMA domains, numbered 0 to 7. Each NUMA domain has {cores_per_domain} cores and its own memory.")
    svg.text(M, 28, f"A {name} node", size=17, weight="bold")

    def draw_domain(svg, n, rx, ry):
        draw_cores(svg, rx, ry)
        memory(svg, rx + RW - 36, ry + 30)

    two_buildings(svg, top, lambda b: f"Socket {b}  ·  {cores_per_socket} cores", draw_domain, "socket link",
                  lambda n: f"NUMA domain {n}")
    legend(svg, M, key_top, [
        ("core", "core  (a scientist)"), ("room", "NUMA domain  (a lab)"),
        ("memory", "memory  (a fridge)"), ("building", "socket  (a building)"),
        ("link", "socket link  (the footbridge)")], 330)
    return svg


def fig_milan_node():
    # 16 cores: 4 rows of 4
    return fig_node("Milan", 64, 16, lambda svg, rx, ry: cores_grid(svg, rx + 10, ry + 34, 16, 4, size=17, gap=5))


def fig_genoa_node():
    # 21 cores: 3 rows of 7, centred on the memory block
    return fig_node("Genoa", 84, 21, lambda svg, rx, ry: cores_grid(svg, rx + 10, ry + 49, 21, 7, size=11, gap=4))


# ---------------------------------------------------------------- 4: a desktop and a Genoa node, to scale

# One colour per NUMA domain in a processor: (light, mid, dark)
QUAD = [("#E2F5FB", "#79C9DE", "#007C99"),   # blue
        ("#E3F3EC", "#7CC5AA", "#00765F"),   # green
        ("#ECE9F6", "#ACA3D6", "#5B4E9E"),   # purple
        ("#FBE4E6", "#E3A0AB", "#A3364A")]   # rose
PACKAGE_FILL = "#EEF0F2"
PACKAGE_STROKE = "#5A6875"


def fig_desktop_vs_genoa():
    s = 1.8                                # pixels per millimetre, the same for everything
    mm = lambda v: v * s
    dimm_len, dimm_w = 133.35, 6.0         # a memory module (DIMM) is 133.35 mm long
    srv_pitch, desk_pitch = 7.6, 9.5       # spacing of memory slots
    sp5_w, sp5_h = 72.0, 75.4              # Genoa processor package (SP5)
    am5 = 40.0                             # desktop processor package (AM5), 40 x 40 mm
    bank_w = 5 * srv_pitch + dimm_w        # six slots
    gap_bank = 14.0
    group_w = bank_w + gap_bank + sp5_w + gap_bank + bank_w
    gap_sockets = 30.0
    m = 20
    W = round(m * 2 + mm(group_w * 2 + gap_sockets))
    dt = 70                                # top of the desktop drawing
    st = round(dt + mm(dimm_len) + 56)     # top of the Genoa drawing
    sb = st + mm(dimm_len)                 # bottom of the Genoa memory slots
    legend_top = sb + 64
    H = round(legend_top + 3 * 24 + 20 + 8)

    svg = Svg(W, H, "A desktop processor and a Genoa node, drawn to the same scale",
              "The desktop has one processor, about 4 cm across, with its memory slots on one side, all wired to "
              "the same part of the processor, so it has one NUMA domain. The Genoa node has two processors, each "
              "about 7.5 cm across, joined by a link, with six memory slots on each side of each processor. "
              "Each quarter of a Genoa processor, with its chips of cores and the memory slots wired to it, "
              "is one NUMA domain, giving 8 in the node.")
    svg.text(M, 28, "A desktop and a Genoa node, drawn to the same scale", size=17, weight="bold")

    def slot(x, y, colour):
        light, mid, dark = colour
        svg.rect(x, y, mm(dimm_w), mm(dimm_len), mid, dark, sw=1, rx=2)
        svg.line(x + mm(dimm_w) / 2, y + 6, x + mm(dimm_w) / 2, y + mm(dimm_len) - 6, dark, sw=0.8)

    def chip(x, y, w, h, colour):
        svg.rect(x, y, mm(w), mm(h), colour[1], colour[2], sw=1, rx=1.5)

    def size_label(cx, y, words):
        svg.text(cx, y, words, size=12.5, anchor="middle", fill=MUTED)

    # ---- desktop: one small processor, memory on one side, one NUMA domain
    svg.text(M, 58, "Desktop: one processor, one NUMA domain", size=14.5, weight="bold")
    px, py = M, dt + mm((dimm_len - am5) / 2)
    svg.rect(px, py, mm(am5), mm(am5), PACKAGE_FILL, PACKAGE_STROKE, sw=1.5, rx=3)
    for i in range(2):                                     # two chips of cores
        chip(px + mm(8 + i * 13), py + mm(6), 11, 7, QUAD[0])
    svg.rect(px + mm(12), py + mm(21), mm(16), mm(12), QUAD[0][0], QUAD[0][2], sw=1, rx=1.5)   # central chip
    size_label(px + mm(am5) / 2, py - 8, "about 4 cm")
    bx = px + mm(am5 + 25)
    for i in range(4):
        slot(bx + mm(i * desk_pitch), dt, QUAD[0])
    tx = bx + mm(3 * desk_pitch + dimm_w) + 40
    svg.text(tx, dt + mm(dimm_len) / 2 - 10, "All of the memory is wired to the same part of the processor,", size=13.5)
    svg.text(tx, dt + mm(dimm_len) / 2 + 12, "so every core reaches it the same way.", size=13.5)

    # scale bar: 5 cm
    sx, sy = tx, dt + mm(dimm_len) - 20
    svg.line(sx, sy, sx + mm(50), sy, TEXT, sw=2)
    for x in (sx, sx + mm(50)):
        svg.line(x, sy - 6, x, sy + 6, TEXT, sw=2)
    svg.text(sx + mm(50) + 10, sy + 4.5, "5 cm", size=12.5)

    # ---- Genoa node: two large processors, memory on both sides of each, 4 NUMA domains in each
    svg.text(M, st - 12, "Genoa node: two processors, 8 NUMA domains", size=14.5, weight="bold")
    centres = []
    for p in range(2):
        gx = M + mm(p * (group_w + gap_sockets))
        # memory slots on the left: outer three wired to quarter 0, inner three to quarter 2
        for i in range(6):
            slot(gx + mm(i * srv_pitch), st, QUAD[0] if i < 3 else QUAD[2])
        px = gx + mm(bank_w + gap_bank)
        py = st + mm((dimm_len - sp5_h) / 2)
        svg.rect(px, py, mm(sp5_w), mm(sp5_h), PACKAGE_FILL, PACKAGE_STROKE, sw=1.5, rx=3)
        size_label(px + mm(sp5_w) / 2, py - 8, "about 7.5 cm")
        # chips of cores: a column of six down each side of the central chip
        col_h = 6 * 7 + 5 * 2.5
        y0 = py + mm((sp5_h - col_h) / 2)
        for j in range(6):
            cy = y0 + mm(j * (7 + 2.5))
            chip(px + mm(6), cy, 11, 7, QUAD[0] if j < 3 else QUAD[2])
            chip(px + mm(sp5_w - 6 - 11), cy, 11, 7, QUAD[1] if j < 3 else QUAD[3])
        # central chip (I/O die) with its four quarters, numbered by NUMA domain
        iw, ih = 28, 26
        ix, iy = px + mm((sp5_w - iw) / 2), py + mm((sp5_h - ih) / 2)
        svg.rect(ix, iy, mm(iw), mm(ih), "#FFFFFF", PACKAGE_STROKE, sw=1, rx=1.5)
        for q in range(4):
            qx = ix + (q % 2) * mm(iw) / 2
            qy = iy + (q // 2) * mm(ih) / 2
            svg.rect(qx + 1, qy + 1, mm(iw) / 2 - 2, mm(ih) / 2 - 2, QUAD[q][0], QUAD[q][2], sw=1, rx=1)
            svg.text(qx + mm(iw) / 4, qy + mm(ih) / 4 + 4, str(p * 4 + q), size=11.5, weight="bold",
                     anchor="middle", fill=QUAD[q][2])
        # memory slots on the right: inner three wired to quarter 3, outer three to quarter 1
        rx0 = px + mm(sp5_w + gap_bank)
        for i in range(6):
            slot(rx0 + mm(i * srv_pitch), st, QUAD[3] if i < 3 else QUAD[1])
        centres.append((px + mm(sp5_w) / 2, py + mm(sp5_h)))

    # link between the two processors, under the memory slots
    (x0, y0), (x1, _) = centres
    ly = sb + 16
    svg.path(f"M{x0:g},{y0:g} V{ly:g} H{x1:g} V{y0:g}", "#8C99A6", sw=5)
    svg.text((x0 + x1) / 2, ly + 22, "link between the two processors", size=12.5, anchor="middle", fill=MUTED)

    # key
    y = legend_top
    svg.rect(M, y - 11, mm(11), mm(7), QUAD[0][1], QUAD[0][2], sw=1, rx=1.5)
    svg.text(M + 30, y, "chip of cores", size=12.5)
    svg.rect(M + 150, y - 12, 26, 15, QUAD[0][0], QUAD[0][2], sw=1, rx=1.5)
    svg.text(M + 184, y, "central chip, with the memory controllers", size=12.5)
    svg.rect(M + 480, y - 12, 40, 10, QUAD[0][1], QUAD[0][2], sw=1, rx=2)
    svg.text(M + 528, y, "memory slot", size=12.5)
    y += 24
    svg.text(M, y, "In each Genoa processor, each colour is one NUMA domain:", size=12.5)
    y += 20
    svg.text(M, y, "a quarter of the processor, with its chips of cores and the memory slots wired to it.", size=12.5)
    y += 24
    svg.text(M, y, "Processors and memory slots are roughly to scale. The layout inside each processor is simplified.",
             size=12, fill=MUTED)
    return svg


# ---------------------------------------------------------------- 5 and 6: when NUMA domains matter
# Each picture is one Genoa socket, drawn the same size as a socket in the Genoa node diagram,
# and each figure is as wide as the others, so they all fill the page's column the same way.

CORE_X, CORE_Y, CORE_S, CORE_P = 10, 49, 11, 15    # first core's place in its domain, core size, core pitch
MEM_X, MEM_Y, MEM_W, MEM_H = RW - 36, 30, 26, 78   # memory's place in its domain, and its size
DATA_W, DATA_H, DATA_Y, DATA_P = 18, 8, 8, 13      # a block of data in memory: size, first block's place, pitch
WHEN_TOP = 74                                       # top of the two sockets
CAPTION_Y = WHEN_TOP + BH + 24                      # first line of the captions under them
KEY_Y = CAPTION_Y + 18 + 38                         # first line of the key


def core_xy(rx, ry, i):
    """Top left corner of core i (0 to 20, in rows of 7) in the NUMA domain whose top left corner is rx, ry."""
    r, c = divmod(i, 7)
    return rx + CORE_X + c * CORE_P, ry + CORE_Y + r * CORE_P


def genoa_socket(svg, x, y, title, job, data, ghost=None, good=True):
    """One Genoa socket with 4 NUMA domains of 21 cores.
    job: {domain: [cores the job uses]}, data: {domain: blocks of data in its memory},
    ghost: (domain, core) the thread left, good: True for the fast case (green outline and a tick),
    False for the slow case (red outline and a cross).
    Returns where each domain and its memory are. Call domain_labels() after drawing the arrows."""
    colour = GREEN if good else RED
    svg.text(x, y - 9, title, size=14.5, weight="bold")
    svg.rect(x, y, BW, BH, BUILDING_FILL, colour, sw=2.5, rx=8)
    svg.text(x + BP, y + 21, "One Genoa socket", size=13, fill=MUTED)
    # the verdict, in the top right corner: a tick or a cross, and words, so it doesn't rely on colour
    words = "Good: fast" if good else "Bad: slower"
    pw = 36 + len(words) * 6.4
    px, py = x + BW - BP - pw, y + 6
    svg.rect(px, py, pw, 20, colour, rx=10)
    ix, iy = px + 10, py + 5.5
    if good:
        svg.path(f"M{ix:g},{iy + 4.5:g} L{ix + 3.5:g},{iy + 8:g} L{ix + 9.5:g},{iy + 0.5:g}", "#FFFFFF", sw=2.2)
    else:
        svg.path(f"M{ix + 0.5:g},{iy + 0.5:g} L{ix + 8.5:g},{iy + 8.5:g} "
                 f"M{ix + 8.5:g},{iy + 0.5:g} L{ix + 0.5:g},{iy + 8.5:g}", "#FFFFFF", sw=2.2)
    svg.text(px + 26, py + 14.5, words, size=12.5, weight="bold", fill="#FFFFFF")
    geo = {"labels": []}
    for d in range(4):
        row, col = divmod(d, 2)
        rx, ry = x + BP + col * (RW + RG), y + BL + row * (RH + RG)
        fill, stroke = ROOMS[(row + col) % 2]
        svg.rect(rx, ry, RW, RH, fill, stroke, sw=1.8, rx=6)
        geo["labels"].append((rx + 9, ry + 19, f"NUMA domain {d}", fill))
        for i in range(21):
            cx, cy = core_xy(rx, ry, i)
            svg.rect(cx, cy, CORE_S, CORE_S, TEXT if i in job.get(d, []) else CORE, rx=1.5)
        bx, by = rx + MEM_X, ry + MEM_Y
        svg.rect(bx, by, MEM_W, MEM_H, MEM_FILL, MEM_STROKE, sw=1.5, rx=3)
        for k in range(data.get(d, 0)):
            svg.rect(bx + (MEM_W - DATA_W) / 2, by + DATA_Y + k * DATA_P, DATA_W, DATA_H, MEM_STROKE, rx=1.5)
        geo[d] = (rx, ry, bx, by)
    if ghost:
        gx, gy = core_xy(geo[ghost[0]][0], geo[ghost[0]][1], ghost[1])
        svg.rect(gx - 2.5, gy - 2.5, CORE_S + 5, CORE_S + 5, "none", TEXT, sw=1.4, rx=2, dash="3 2")
    return geo


def fetch(svg, geo, src, dst, k=0, bend=-14):
    """Arrow from core src = (domain, core) to block k of the data in domain dst's memory:
    green and solid from the core's own domain, orange and dashed from another domain."""
    sx, sy = core_xy(geo[src[0]][0], geo[src[0]][1], src[1])
    sx, sy = sx + CORE_S / 2, sy + CORE_S / 2
    bx, by = geo[dst][2], geo[dst][3]
    ey = by + DATA_Y + k * DATA_P + DATA_H / 2
    if sx < bx:                                        # the last piece points straight into the memory
        ex, px = bx - 3, bx - 12
    else:
        ex, px = bx + MEM_W + 3, bx + MEM_W + 12
    mx, my = (sx + px) / 2, (sy + ey) / 2 + bend
    colour, dash, marker = (GREEN, None, "ah-green") if src[0] == dst else (ORANGE, "7 4", "ah-orange")
    svg.path(f"M{sx:g},{sy:g} Q{mx:g},{my:g} {px:g},{ey:g} L{ex:g},{ey:g}", colour, dash=dash, marker=marker)


def domain_labels(svg, geo):
    """The NUMA domain labels, on top of the arrows, outlined in the domain's colour."""
    for lx, ly, words, bg in geo["labels"]:
        svg.add(f'<text x="{lx:g}" y="{ly:g}" font-size="13.5" font-weight="bold" fill="{bg}" '
                f'stroke="{bg}" stroke-width="5" stroke-linejoin="round">{esc(words)}</text>')
        svg.text(lx, ly, words, size=13.5, weight="bold")


def caption(svg, x, lines):
    for k, words in enumerate(lines):
        svg.text(x, CAPTION_Y + k * 18, words, size=13)


def when_key(svg, columns):
    """The key, in two columns that line up with the two sockets. Each column is a list of (kind, words)."""
    for col, items in enumerate(columns):
        x = M + col * (BW + GAP)
        for row, (kind, words) in enumerate(items):
            y = KEY_Y + row * 26
            if kind == "job":
                svg.rect(x + 8.5, y - 10, CORE_S, CORE_S, TEXT, rx=1.5)
            elif kind == "data":
                svg.rect(x + 5, y - 8.5, DATA_W, DATA_H, MEM_STROKE, rx=1.5)
            elif kind == "ghost":
                svg.rect(x + 6, y - 12.5, CORE_S + 5, CORE_S + 5, "none", TEXT, sw=1.4, rx=2, dash="3 2")
            else:
                colour, dash, sw = {"fast": (GREEN, None, 2.5), "slow": (ORANGE, "7 4", 2.5),
                                    "move": (MUTED, None, 2)}[kind]
                svg.line(x, y - 4.5, x + 28, y - 4.5, colour, sw=sw, dash=dash)
            svg.text(x + 40, y, words, size=13)


def when_figure(title, heading, desc, key_rows):
    """A figure with a heading, room for two sockets side by side with captions, and a key of key_rows rows.
    Returns the figure and the left edges of the two sockets."""
    svg = Svg(W, KEY_Y + (key_rows - 1) * 26 + 16, title, desc)
    svg.text(M, 28, heading, size=17, weight="bold")
    return svg, M, M + BW + GAP


FAST = ("fast", "fetch from its own NUMA domain (fast)")
SLOWER = ("slow", "fetch from another NUMA domain (slower)")


def fig_cores_spread():
    svg, xl, xr = when_figure(
        "A job's cores spread over several NUMA domains",
        "1. The job's cores are spread over several NUMA domains",
        "Each picture shows one Genoa socket with 4 NUMA domains. A job with all its cores in one NUMA domain "
        "fetches its data from close by, which is fast. The same job spread over three NUMA domains has to "
        "fetch some of its data from another domain, which is slower.", key_rows=2)
    g = genoa_socket(svg, xl, WHEN_TOP, "All in one NUMA domain", {0: [0, 1, 2, 3]}, {0: 3})
    fetch(svg, g, (0, 1), 0, k=0, bend=-12)
    fetch(svg, g, (0, 3), 0, k=2, bend=10)
    domain_labels(svg, g)
    caption(svg, xl, ["All the job's cores are in one domain,", "so its data is close by."])
    g = genoa_socket(svg, xr, WHEN_TOP, "Spread over three NUMA domains", {0: [0, 1], 1: [8], 3: [9]},
                     {0: 3, 1: 1, 3: 1}, good=False)
    fetch(svg, g, (0, 1), 0, k=0, bend=-12)
    fetch(svg, g, (1, 8), 0, k=1, bend=-12)
    fetch(svg, g, (3, 9), 0, k=2, bend=20)
    domain_labels(svg, g)
    caption(svg, xr, ["Its cores are in three domains, so some", "fetches go to another domain."])
    when_key(svg, [[("job", "a core your job is using"), ("data", "your job's data, in memory")], [FAST, SLOWER]])
    return svg


def fig_thread_moves():
    svg, xl, xr = when_figure(
        "A thread that moves to another NUMA domain",
        "2. A thread moves to another NUMA domain",
        "Each picture shows one Genoa socket with 4 NUMA domains. A thread first uses its data in domain 0, "
        "so the data is stored in domain 0's memory and every fetch is fast. Then the operating system moves "
        "the thread to domain 1, and from then on every fetch of that data comes from another domain, "
        "which is slower.", key_rows=3)
    g = genoa_socket(svg, xl, WHEN_TOP, "Before", {0: [15]}, {0: 2})
    fetch(svg, g, (0, 15), 0, bend=-12)
    domain_labels(svg, g)
    caption(svg, xl, ["The thread first uses its data here,", "so the data is stored in domain 0."])
    g = genoa_socket(svg, xr, WHEN_TOP, "After the thread moves", {1: [15]}, {0: 2}, ghost=(0, 15), good=False)
    # the move: an arrow under the bottom row of cores and domain 0's memory, ending straight up into the new core
    (ox, oy), (nx, ny), h = core_xy(*g[0][:2], 15), core_xy(*g[1][:2], 15), CORE_S / 2
    svg.path(f"M{ox + h:g},{oy + CORE_S + 4:g} Q{(ox + nx) / 2 + h:g},{oy + 53:g} {nx + h:g},{ny + CORE_S + 12:g} "
             f"L{nx + h:g},{ny + CORE_S + 4:g}", MUTED, sw=2, marker="ah-grey")
    fetch(svg, g, (1, 15), 0, bend=-18)
    domain_labels(svg, g)
    caption(svg, xr, ["The operating system moves the thread.", "Its data stays in domain 0."])
    when_key(svg, [[("job", "the core running the thread"), ("data", "the thread's data, in memory"),
                    ("ghost", "where the thread was before it moved")],
                   [FAST, SLOWER, ("move", "the operating system moves the thread")]])
    return svg


if __name__ == "__main__":
    out = Path(sys.argv[1] if len(sys.argv) > 1 else "docs/assets/images")
    for name, fig in (("NUMA_Domains_Lab_Story.svg", fig_lab_story),
                      ("NUMA_Domains_Milan_Node.svg", fig_milan_node),
                      ("NUMA_Domains_Genoa_Node.svg", fig_genoa_node),
                      ("NUMA_Domains_Desktop_vs_Genoa.svg", fig_desktop_vs_genoa),
                      ("NUMA_Domains_Cores_Spread.svg", fig_cores_spread),
                      ("NUMA_Domains_Thread_Moves.svg", fig_thread_moves)):
        (out / name).write_text(fig().render(), encoding="utf-8")
        print("wrote", out / name)
