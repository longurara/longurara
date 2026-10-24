"""Generate the README SVG assets (header + DontStarveWasm card) in Catppuccin Mocha/Latte.

Usage: python scripts/gen_assets.py assets
"""
import random
import sys
from pathlib import Path

OUT = Path(sys.argv[1])
OUT.mkdir(parents=True, exist_ok=True)

MOCHA = dict(
    sky_top="#11111b", sky_bot="#1e1e2e", star="#cdd6f4", moon="#f9e2af", moon_glow="#f9e2af",
    wave1="#cba6f7", wave2="#f5c2e7", wave3="#89b4fa", title="#cdd6f4", sub="#a6adc8",
    accent="#cba6f7", card="#181825", border="#313244", chip="#313244", chip_text="#cdd6f4",
    muted="#7f849c", green="#a6e3a1", peach="#fab387", blue="#89b4fa", pink="#f5c2e7",
)
LATTE = dict(
    sky_top="#dce0e8", sky_bot="#eff1f5", star="#7287fd", moon="#df8e1d", moon_glow="#df8e1d",
    wave1="#8839ef", wave2="#ea76cb", wave3="#1e66f5", title="#4c4f69", sub="#5c5f77",
    accent="#8839ef", card="#e6e9ef", border="#ccd0da", chip="#ccd0da", chip_text="#4c4f69",
    muted="#8c8fa1", green="#40a02b", peach="#fe640b", blue="#1e66f5", pink="#ea76cb",
)

SANS = "'Segoe UI', -apple-system, Helvetica, Arial, sans-serif"
MONO = "Consolas, 'SF Mono', Menlo, monospace"


def header(p, light):
    rnd = random.Random(7)
    stars = []
    for i in range(46):
        x, y = rnd.uniform(10, 990), rnd.uniform(8, 150)
        r = rnd.choice([0.8, 1, 1.2, 1.6])
        dur = rnd.uniform(2.4, 5.5)
        delay = rnd.uniform(0, 4)
        stars.append(
            f'<circle class="tw" cx="{x:.0f}" cy="{y:.0f}" r="{r}" '
            f'style="animation-duration:{dur:.1f}s;animation-delay:-{delay:.1f}s"/>'
        )
    star_opacity = "0.55" if light else "0.9"
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="1000" height="230" viewBox="0 0 1000 230" role="img" aria-label="Lê Hoàng Long (@longurara)">
  <defs>
    <linearGradient id="sky" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0" stop-color="{p['sky_top']}"/>
      <stop offset="1" stop-color="{p['sky_bot']}"/>
    </linearGradient>
    <linearGradient id="w" x1="0" y1="0" x2="1" y2="0">
      <stop offset="0" stop-color="{p['wave1']}"/>
      <stop offset="0.5" stop-color="{p['wave2']}"/>
      <stop offset="1" stop-color="{p['wave3']}"/>
    </linearGradient>
    <radialGradient id="glow">
      <stop offset="0" stop-color="{p['moon_glow']}" stop-opacity="0.35"/>
      <stop offset="1" stop-color="{p['moon_glow']}" stop-opacity="0"/>
    </radialGradient>
    <mask id="crescent">
      <circle cx="880" cy="62" r="26" fill="#fff"/>
      <circle cx="893" cy="53" r="23" fill="#000"/>
    </mask>
    <clipPath id="frame"><rect width="1000" height="230" rx="16"/></clipPath>
  </defs>
  <style>
    .tw {{ fill: {p['star']}; opacity: {star_opacity}; animation: tw ease-in-out infinite alternate; }}
    @keyframes tw {{ from {{ opacity: 0.1; }} to {{ opacity: {star_opacity}; }} }}
    .wave {{ animation: drift linear infinite; }}
    @keyframes drift {{ from {{ transform: translateX(0); }} to {{ transform: translateX(-500px); }} }}
    .moon {{ animation: bob 6s ease-in-out infinite alternate; }}
    @keyframes bob {{ from {{ transform: translateY(0); }} to {{ transform: translateY(5px); }} }}
    .title {{ font: 700 44px {SANS}; fill: {p['title']}; }}
    .handle {{ font: 600 18px {MONO}; fill: {p['accent']}; }}
    .sub {{ font: 400 16px {SANS}; fill: {p['sub']}; }}
    @media (prefers-reduced-motion: reduce) {{ .tw, .wave, .moon {{ animation: none; }} }}
  </style>
  <g clip-path="url(#frame)">
    <rect width="1000" height="230" fill="url(#sky)"/>
    {''.join(stars)}
    <g class="moon">
      <circle cx="880" cy="62" r="70" fill="url(#glow)"/>
      <rect x="850" y="32" width="60" height="60" fill="{p['moon']}" mask="url(#crescent)"/>
    </g>
    <g class="wave" style="animation-duration:22s" opacity="0.35">
      <path fill="url(#w)" d="M0 186 Q125 160 250 186 T500 186 T750 186 T1000 186 T1250 186 T1500 186 V230 H0 Z"/>
    </g>
    <g class="wave" style="animation-duration:14s" opacity="0.6">
      <path fill="url(#w)" d="M0 200 Q125 182 250 200 T500 200 T750 200 T1000 200 T1250 200 T1500 200 V230 H0 Z"/>
    </g>
    <text x="60" y="92" class="title">Lê Hoàng Long</text>
    <text x="62" y="124" class="handle">@longurara</text>
    <text x="62" y="152" class="sub">Software Engineering @ FPT University · building cozy, local-first things after midnight ☕</text>
  </g>
</svg>
'''


def dst_card(p):
    def box(x, y, w, h, label, sub, color):
        return (
            f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="10" fill="{p["chip"]}" stroke="{color}" stroke-width="1.5"/>'
            f'<text x="{x + w / 2}" y="{y + 24}" class="b" text-anchor="middle" fill="{color}">{label}</text>'
            f'<text x="{x + w / 2}" y="{y + 42}" class="s" text-anchor="middle">{sub}</text>'
        )

    def chip(x, label, color):
        w = 32 + len(label) * 7.2
        return (
            f'<rect x="{x}" y="232" width="{w:.0f}" height="24" rx="12" fill="{p["chip"]}"/>'
            f'<circle cx="{x + 12}" cy="244" r="4" fill="{color}"/>'
            f'<text x="{x + 21}" y="248.5" class="c">{label}</text>'
        ), x + w + 8

    chips, x = [], 24
    for label, color in [("C++17", p["blue"]), ("Lua 5.1", p["accent"]), ("WebGL2", p["peach"]), ("IndexedDB", p["green"]), ("WebRTC", p["pink"])]:
        c, x = chip(x, label, color)
        chips.append(c)

    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="508" height="270" viewBox="0 0 508 270" role="img" aria-label="DontStarveWasm architecture">
  <style>
    .t {{ font: 700 15px {MONO}; fill: {p['title']}; }}
    .b {{ font: 700 13px {MONO}; }}
    .s {{ font: 400 11px {SANS}; fill: {p['muted']}; }}
    .c {{ font: 600 11px {MONO}; fill: {p['chip_text']}; }}
    .flow {{ stroke-dasharray: 4 5; animation: flow 1.2s linear infinite; }}
    @keyframes flow {{ to {{ stroke-dashoffset: -18; }} }}
    @media (prefers-reduced-motion: reduce) {{ .flow {{ animation: none; }} }}
  </style>
  <rect x="0.5" y="0.5" width="507" height="269" rx="14" fill="{p['card']}" stroke="{p['border']}"/>
  <g transform="translate(14 0)">
  <circle cx="24" cy="24" r="5" fill="#f38ba8"/><circle cx="40" cy="24" r="5" fill="#f9e2af"/><circle cx="56" cy="24" r="5" fill="#a6e3a1"/>
  <text x="76" y="29" class="t">dont-starve.wasm</text>
  {box(150, 48, 180, 50, "Browser main thread", "WebGL2 · OffscreenCanvas", p['accent'])}
  <g fill="none" stroke="{p['muted']}" stroke-width="1.5">
    <path class="flow" d="M240 98 V114 H80 V128"/>
    <path class="flow" d="M240 98 V128"/>
    <path class="flow" d="M240 98 V114 H400 V128"/>
  </g>
  {box(24, 128, 120, 50, "Client", "WASM Worker", p['blue'])}
  {box(180, 128, 120, 50, "Master", "WASM Worker", p['green'])}
  {box(336, 128, 120, 50, "Caves", "WASM Worker", p['peach'])}
  <text x="240" y="200" class="s" text-anchor="middle">4,030 Lua scripts → 16 SHA-256 verified bundles</text>
  <text x="240" y="216" class="s" text-anchor="middle">atomic IndexedDB checkpoints · P2P over RTCDataChannel</text>
  {''.join(chips)}
  </g>
</svg>
'''


(OUT / "header.svg").write_text(header(MOCHA, False), encoding="utf-8")
(OUT / "header-light.svg").write_text(header(LATTE, True), encoding="utf-8")
(OUT / "dontstarvewasm.svg").write_text(dst_card(MOCHA), encoding="utf-8")
(OUT / "dontstarvewasm-light.svg").write_text(dst_card(LATTE), encoding="utf-8")
print("ok")
