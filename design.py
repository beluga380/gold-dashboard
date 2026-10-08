"""Design tokens shared by the app (and mirrored in the notebook).

Three fixed mappings, enforced everywhere:
  entity -> hue          (one colour per country on every panel)
  epistemic status -> line style  (solid = reported, dashed = estimated)
  data class -> mark     (lines = levels, bars = period changes, areas = composition)
"""

PAPER = "#fbfbf8"
INK   = "#1c1c18"
FAINT = "#8c8c84"
GHOST = "#d9d9d2"
GOLD  = "#a3780a"   # reserved for the price of gold itself
# Mid-grey for marks the original drew in INK. Black lines vanish when the
# reader switches Streamlit to its dark theme; this grey reads on both.
MARK  = "#8a8a82"
# Grid lines as a translucent grey, so they stay faint on light and dark.
GRID  = "rgba(128,128,128,0.18)"
# Event rules: translucent so they stay quiet on both light and dark pages.
RULE  = "rgba(128,128,128,0.45)"

HUES = {
    "China":     "#b3392e",
    "China + HK":"#b3392e",
    "Russia":    "#2e5fa3",
    "Iran":      "#2e7d5b",
    "India":     "#c98a1b",
    "Turkey":    "#8e4a8b",
    "UK + US":   "#5b6b7a",
    "West":      "#5b6b7a",
    "UAE + Gulf":"#b9b9b0",
    "other":     "#d9d9d2",
}
REST = "#b9b9b0"          # rest-of-world grey (figure-ground)

def hue(entity: str) -> str:
    return HUES.get(entity, REST)

SOLID = None              # plotly default dash
DASH  = "dash"            # estimated / inferred series

# Discrete, political demand shocks -- drawn as vertical rules on every time axis
EVENTS = [
    ("2022-02-28", "freeze"),
    ("2022-06-26", "G7 ban"),
    ("2025-06-13", "Iran war"),
    ("2025-11-01", "CBR sells"),
    ("2026-05-15", "escalation"),
]

# Mine replenishment reference rates, tonnes per month (USGS-derived, hand-entered yearly)
MINE_TOTAL_TPM   = 300    # ~3,600 t/yr global mine supply
MINE_WESTERN_TPM = 200    # ~2,400 t/yr that enters the Western circuit
