#!/usr/bin/env python3
"""
Capture fresh Slurm Composer (OpenComposer, /oc/) screenshots from your
authenticated NeSI OnDemand session, matching the existing docs images in
docs/assets/images/Slurm_Composer_*.png.

You log in manually in the browser window that opens (SSO + 2FA); this script
only handles consistent sizing, correct filenames and best-effort navigation.
It writes into a staging folder (default: ./_oc_screenshots_new) so nothing in
the repo is overwritten until the results have been reviewed.

Run:
    python3 capture_oc_screenshots.py                 # all 10 shots
    python3 capture_oc_screenshots.py --only Slurm_Composer_home,Slurm_Composer_gpu
    python3 capture_oc_screenshots.py --out /tmp/oc   # different staging folder

Requirements (already present on this machine):
    - playwright (python) + chromium browser
    - Pillow (optional; only used to print captured dimensions)

At each step the browser is left fully interactive while the script waits on
your keypress in THIS terminal, so you can click around to reach the exact view
before it is captured.

When the pass finishes the browser STAYS OPEN and logged in, so you can
re-capture any shot(s) on demand without going through SSO again. It only closes
when you type 'q' at the re-capture prompt.
"""

import argparse
import re
import sys
from pathlib import Path

try:
    from playwright.sync_api import sync_playwright
except Exception as exc:  # pragma: no cover
    sys.exit(
        "Could not import playwright.\n"
        f"  {exc}\n"
        "Install with:  python3 -m pip install playwright  &&  python3 -m playwright install chromium"
    )

try:
    from PIL import Image
except Exception:
    Image = None  # dimensions summary just gets skipped

BASE = "https://ondemand.nesi.org.nz/pun/sys/dashboard/oc/"
SCALE = 2                 # existing images are 2x HiDPI (1400 CSS -> 2800 px)
WIDE = {"width": 1400, "height": 900}     # full-length page views (height auto-fits content)
MODAL = {"width": 1400, "height": 1000}   # window/modal views (wide so the dialog isn't squeezed; cropped to the dialog)
VP_MAX_H = 20000          # sanity bound on viewport height for extremely long pages (CSS px)

# Expected pixel dimensions of the current images (width is the thing to match;
# height varies with page content). Used only for the end-of-run summary.
EXPECT = {
    "Slurm_Composer_home": (2800, 1800),
    "Slurm_Composer_form": (2800, 2230),
    "Slurm_Composer_advanced": (2800, 3254),
    "Slurm_Composer_gpu": (2800, 2444),
    "Slurm_Composer_load_from_disk": (2800, 1800),
    "Slurm_Composer_new_script": (2800, 1800),
    "Slurm_Composer_new_template": (2800, 1794),
    "Slurm_Composer_history": (2800, 1794),
    "Slurm_Composer_script": (1600, 1602),
    "Slurm_Composer_efficiency": (1600, 1602),
}

MODAL_SELECTORS = [
    '[role="dialog"]',
    ".modal.show .modal-dialog",
    ".modal-dialog",
    ".modal-content",
    ".oc-window",
    ".window",
]


# Matches the normal CPU tile "Job Script (Slurm)" but NOT "GPU Job Script (Slurm)"
# (anchored at the start, so the leading "GPU " on the other tile excludes it).
NORMAL_JOB_RE = re.compile(r"^\s*Job Script \(Slurm\)")


def click_text(page, text, timeout=4000, exact=False):
    """Best-effort click on a link/button/text; returns True on success.

    `text` may be a string (matched using `exact`) or a compiled regex (matched
    as-is). A regex lets us target the normal 'Job Script (Slurm)' tile without
    also matching 'GPU Job Script (Slurm)'.
    """
    if isinstance(text, re.Pattern):
        locators = (
            page.get_by_role("link", name=text),
            page.get_by_role("button", name=text),
            page.get_by_text(text),
        )
    else:
        locators = (
            page.get_by_role("link", name=text, exact=exact),
            page.get_by_role("button", name=text, exact=exact),
            page.get_by_text(text, exact=exact),
        )
    for locator in locators:
        try:
            locator.first.click(timeout=timeout)
            return True
        except Exception:
            continue
    return False


def nav_none(page):
    pass


def nav_home(page):
    page.goto(BASE, wait_until="domcontentloaded")


def nav_form(page):
    page.goto(BASE, wait_until="domcontentloaded")
    click_text(page, NORMAL_JOB_RE)  # the normal (CPU) Job Script form, NOT the GPU one


def nav_advanced(page):
    # Open the normal (CPU) Job Script form fresh, then reveal advanced options,
    # so this never inherits the GPU form from a previous step.
    page.goto(BASE, wait_until="domcontentloaded")
    click_text(page, NORMAL_JOB_RE)
    click_text(page, "Show advanced options")


def nav_gpu(page):
    page.goto(BASE, wait_until="domcontentloaded")
    click_text(page, "GPU Job Script (Slurm)")


def nav_load(page):
    page.goto(BASE, wait_until="domcontentloaded")
    click_text(page, "Load or Create a Script from Disk")


def nav_new_script(page):
    # Assumes the file browser (load_from_disk) is open (previous shot).
    click_text(page, "New Script")


def nav_new_template(page):
    page.goto(BASE, wait_until="domcontentloaded")
    click_text(page, "New Custom Template")


def nav_history(page):
    page.goto(BASE, wait_until="domcontentloaded")
    click_text(page, "History")


# name, capture mode, viewport, best-effort nav, what YOU should make visible
SHOTS = [
    ("Slurm_Composer_home", "page", WIDE, nav_home,
     "HOME page (Selected Templates), showing the Slurm Submit Templates and nav bar."),
    ("Slurm_Composer_form", "page", WIDE, nav_form,
     "The NORMAL (CPU) 'Job Script (Slurm)' form — NOT the GPU one. "
     "Form on the left, live Script Content on the right."),
    ("Slurm_Composer_advanced", "page", WIDE, nav_advanced,
     "The NORMAL (CPU) 'Job Script (Slurm)' form with 'Show advanced options' TICKED "
     "(Testing/Profiling/SSD/...). NOT the GPU form."),
    ("Slurm_Composer_gpu", "page", WIDE, nav_gpu,
     "GPU 'GPU Job Script (Slurm)' form, including the 'Type of GPU' selector."),
    ("Slurm_Composer_load_from_disk", "page", WIDE, nav_load,
     "The 'Load or Create a Script from Disk' file browser (full-page)."),
    ("Slurm_Composer_new_script", "page", WIDE, nav_new_script,
     "The template picker shown after clicking 'New Script'."),
    ("Slurm_Composer_new_template", "page", WIDE, nav_new_template,
     "The '+ New Custom Template' page."),
    ("Slurm_Composer_history", "page", WIDE, nav_history,
     "The HISTORY page listing submitted jobs with their status."),
    ("Slurm_Composer_script", "element", MODAL, nav_none,
     "On History, click a job's SCRIPT NAME so the 'Job Script' window/modal is open."),
    ("Slurm_Composer_efficiency", "element", MODAL, nav_none,
     "On History, click a FINISHED job's Job ID so the 'Job Details' window is open, "
     "scrolled to the 'Job Efficiency (seff)' section."),
]


def dims(path):
    if Image is None:
        return None
    try:
        with Image.open(path) as im:
            return im.size
    except Exception:
        return None


def wait_for_images(page, timeout=15000, idle_timeout=3000):
    """Block until the page's images have actually loaded and decoded.

    Navigation here uses wait_until="domcontentloaded", which fires BEFORE
    images finish downloading. Several OC views (notably 'New Custom Template')
    render tiles whose thumbnail <img>s arrive over the network a moment later,
    so a screenshot taken too early catches the page with some — or all — of
    those images still blank. This waits for them so captures are consistent.

    Every step is best-effort/guarded so a slow asset, a stray broken image, or
    a dashboard that never goes fully network-idle can't wedge the capture.
    """
    # 1. Let in-flight image/asset requests settle. Kept short: some OC pages
    #    poll in the background and never reach a strict idle, and we don't want
    #    to pay that full wait on every shot — step 2 is the real guarantee.
    try:
        page.wait_for_load_state("networkidle", timeout=idle_timeout)
    except Exception:
        pass
    # 2. Wait until every DISPLAYED <img> is decoded (complete + non-zero
    #    naturalWidth). Off-layout/hidden images are ignored so a stray broken
    #    decorative asset can't hold the whole capture hostage; a page with no
    #    displayed images (e.g. a plain form) simply passes straight through.
    try:
        page.wait_for_function(
            """() => {
                const imgs = Array.from(document.images || []);
                const shown = imgs.filter(img => {
                    const r = img.getBoundingClientRect();
                    return r.width > 0 && r.height > 0;
                });
                return shown.every(img => img.complete && img.naturalWidth > 0);
            }""",
            timeout=timeout,
        )
    except Exception:
        pass
    # 3. Give decode() a chance to finish so the pixels are ready to paint.
    try:
        page.evaluate(
            """async () => {
                const imgs = Array.from(document.images || []);
                await Promise.all(imgs.map(img =>
                    img.decode ? img.decode().catch(() => {}) : Promise.resolve()
                ));
            }"""
        )
    except Exception:
        pass


def fit_browser_to_page(page, width, max_h=VP_MAX_H, max_passes=4):
    """Resize the browser window (viewport) to be the SAME SIZE AS THE PAGE.

    The page can then be saved in one shot that is exactly the page — no scroll
    stitching, no cut-off, no sticky/fixed navbar duplication.

    1. Scroll top->bottom so any lazy-loaded / virtualised content renders.
    2. Grow the viewport height to the page's content height, re-measuring until
       it stops changing. Re-measuring handles layouts whose height depends on
       the window itself (e.g. a min-height:100vh wrapper), which shift when the
       window is resized.

    Returns (height_css, stable): the settled content height in CSS px (or None),
    and whether it converged. If it did not converge (a genuinely
    viewport-height-driven layout), the caller should fall back to a stitched
    full-page capture at a normal window height.
    """
    try:
        page.evaluate(
            """async () => {
                const sleep = ms => new Promise(r => setTimeout(r, ms));
                const step = Math.max(300, Math.floor(window.innerHeight * 0.8));
                const H = () => document.documentElement.scrollHeight;
                for (let y = 0; y < H(); y += step) { window.scrollTo(0, y); await sleep(60); }
                window.scrollTo(0, 0);
                await sleep(150);
            }"""
        )
    except Exception:
        pass

    # Images requested during the scroll above download asynchronously (and are
    # slow to arrive from remote OnDemand instances like Mahuika); wait for them
    # before measuring/capturing so height is correct and no tile is left blank.
    wait_for_images(page)

    natural, last, stable = None, None, False
    for _ in range(max_passes):
        try:
            natural = page.evaluate("() => Math.ceil(document.documentElement.scrollHeight)")
        except Exception:
            break
        if not natural:
            break
        page.set_viewport_size({"width": width, "height": min(natural, max_h)})
        try:
            page.wait_for_timeout(150)  # let layout settle at the new window height
        except Exception:
            pass
        if last is not None and abs(natural - last) <= 2:
            stable = True  # window height now matches the page and holds steady
            break
        last = natural
    return natural, stable


def capture_element(page, path):
    """Screenshot the whole modal/dialog element; fall back to viewport.

    element.screenshot captures the element's full bounding box even if it is
    taller than the viewport, so a long dialog is captured in full. Selectors are
    ordered outermost-first so we grab the entire dialog, not an inner piece.
    """
    try:
        page.wait_for_timeout(150)  # let the dialog finish opening/animating
    except Exception:
        pass
    wait_for_images(page)  # don't shoot a modal whose images haven't arrived
    for sel in MODAL_SELECTORS:
        try:
            loc = page.locator(sel).first
            if loc.is_visible(timeout=1000):
                loc.scroll_into_view_if_needed(timeout=1000)
                loc.screenshot(path=str(path))
                return f"element {sel}"
        except Exception:
            continue
    page.screenshot(path=str(path), full_page=False)
    return "viewport fallback (no modal element found)"


def print_summary(results, out):
    print("=" * 72)
    print("Saved to:", out)
    if results:
        print("Summary (width should match; height varies with content):")
        for name, got, exp in results:
            g = f"{got[0]}x{got[1]}" if got else "?"
            e = f"{exp[0]}x{exp[1]}" if exp else "?"
            flag = "" if (got and exp and got[0] == exp[0]) else "  <-- check"
            print(f"  {name:34s} {g:>11s}  (was {e}){flag}")


def capture_shots(page, out, shots):
    """Run one capture pass over `shots`, printing progress and a summary.

    Returns the list of (name, got_dims, exp_dims) for the shots captured.
    """
    results = []
    for i, (name, mode, viewport, nav, tell) in enumerate(shots, 1):
        page.set_viewport_size(viewport)
        print(f"[{i}/{len(shots)}] {name}")
        print(f"      Need: {tell}")
        try:
            nav(page)
            print("      (attempted best-effort navigation)")
        except Exception as exc:
            print(f"      (auto-nav skipped: {exc})")
        ans = input("      Position the view, then press Enter to capture "
                    "(or type 's' + Enter to skip): ").strip().lower()
        if ans == "s":
            print("      skipped\n")
            continue

        path = out / f"{name}.png"
        try:
            if mode == "element":
                how = capture_element(page, path)
            else:
                natural, stable = fit_browser_to_page(page, viewport["width"])
                if natural and stable and natural <= VP_MAX_H:
                    # window is now exactly the page size: one clean, un-stitched shot
                    page.screenshot(path=str(path))
                    how = f"page-sized window (~{natural}px tall)"
                else:
                    # height didn't settle (viewport-driven layout) or is huge:
                    # reset to a normal window and let Playwright stitch the page
                    page.set_viewport_size(viewport)
                    page.screenshot(path=str(path), full_page=True)
                    how = (f"full page, stitched (~{natural}px tall)" if natural
                           else "full page, stitched")
                if natural and natural > 8000:
                    how += "  [very long page — double-check it captured fully]"
        except Exception as exc:
            print(f"      ERROR capturing: {exc}\n")
            continue

        got = dims(path)
        exp = EXPECT.get(name)
        note = ""
        if got and exp:
            wmatch = "ok" if got[0] == exp[0] else f"WIDTH {got[0]} vs {exp[0]}"
            note = f" | {got[0]}x{got[1]} (expected ~{exp[0]}x{exp[1]}) [{wmatch}]"
        print(f"      saved {path.name} [{how}]{note}\n")
        results.append((name, got, exp))
    print_summary(results, out)
    return results


def main():
    global BASE
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--out", default=str(Path(__file__).resolve().parent / "_oc_screenshots_new"))
    ap.add_argument("--base", default=BASE)
    ap.add_argument("--only", default="", help="comma-separated shot names to (re)capture")
    args = ap.parse_args()

    BASE = args.base

    out = Path(args.out)
    out.mkdir(parents=True, exist_ok=True)

    wanted = {s.strip() for s in args.only.split(",") if s.strip()}
    shots = [s for s in SHOTS if not wanted or s[0] in wanted]
    if wanted:
        unknown = wanted - {s[0] for s in SHOTS}
        if unknown:
            sys.exit(f"Unknown shot name(s): {', '.join(sorted(unknown))}")

    print(f"Staging folder: {out}")
    print(f"Capturing {len(shots)} shot(s). A browser window will open.\n")

    with sync_playwright() as pw:
        browser = pw.chromium.launch(headless=False)
        context = browser.new_context(viewport=WIDE, device_scale_factor=SCALE)
        page = context.new_page()

        page.goto(BASE, wait_until="domcontentloaded")
        print("=" * 72)
        print("LOG IN NOW in the browser window (SSO + 2FA).")
        print("When the Slurm Composer home page is visible, come back here and")
        input("press Enter to begin capturing... ")
        print("=" * 72 + "\n")

        # ---- first capture pass -------------------------------------------
        capture_shots(page, out, shots)

        # ---- keep the browser open for repeat captures --------------------
        # The session stays logged in, so any view can be re-shot without going
        # through SSO again. The browser closes only when you type 'q'.
        valid = {s[0] for s in SHOTS}
        while browser.is_connected():
            print("\n" + "-" * 72)
            print("Browser is still open and logged in.")
            sel = input(
                "Re-capture? Enter shot name(s) comma-separated, 'all' for every "
                "shot,\n  or 'q' to finish and close the browser: "
            ).strip()
            if sel.lower() in ("q", "quit", "exit"):
                break
            if not sel:
                continue
            if sel.lower() == "all":
                again = list(SHOTS)
            else:
                names = {s.strip() for s in sel.split(",") if s.strip()}
                unknown = names - valid
                if unknown:
                    print("  unknown shot(s):", ", ".join(sorted(unknown)))
                    print("  valid names   :", ", ".join(sorted(valid)))
                    continue
                again = [s for s in SHOTS if s[0] in names]
            try:
                capture_shots(page, out, again)
            except Exception as exc:
                print("  capture pass stopped:", exc)
                if not browser.is_connected():
                    print("  (the browser window was closed)")
                    break

        try:
            browser.close()
        except Exception:
            pass

    print("=" * 72)
    print("Done. Images are in:", out)
    print("Tell Claude to integrate them (copy into docs/assets/images/,")
    print("verify the doc renders, and clean up this staging folder + script).")


if __name__ == "__main__":
    main()
