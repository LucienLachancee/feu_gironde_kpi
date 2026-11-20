import re, sys
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.units import mm
from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import (SimpleDocTemplate, Paragraph, Spacer, Table,
                                TableStyle, KeepTogether)
from reportlab.graphics.shapes import Drawing, Rect, String, Line
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

F = "/usr/share/fonts/truetype/dejavu/"
pdfmetrics.registerFont(TTFont("DV", F + "DejaVuSans.ttf"))
pdfmetrics.registerFont(TTFont("DVB", F + "DejaVuSans-Bold.ttf"))
pdfmetrics.registerFont(TTFont("DVI", F + "DejaVuSans-Oblique.ttf"))
pdfmetrics.registerFont(TTFont("DVBI", F + "DejaVuSans-BoldOblique.ttf"))
from reportlab.pdfbase.pdfmetrics import registerFontFamily
registerFontFamily("DV", normal="DV", bold="DVB", italic="DVI", boldItalic="DVBI")

INK = colors.HexColor("#1f2933")
ACC = colors.HexColor("#b45309")
GRID = colors.HexColor("#c9ced6")
HEAD = colors.HexColor("#f1f3f5")

st = {
    "h1": ParagraphStyle("h1", fontName="DVB", fontSize=17, leading=21, textColor=INK, spaceAfter=4),
    "h2": ParagraphStyle("h2", keepWithNext=1, fontName="DVB", fontSize=13, leading=17, textColor=ACC, spaceBefore=12, spaceAfter=6),
    "h3": ParagraphStyle("h3", keepWithNext=1, fontName="DVB", fontSize=10.5, leading=14, textColor=INK, spaceBefore=8, spaceAfter=4),
    "p": ParagraphStyle("p", fontName="DV", fontSize=9, leading=12.5, textColor=INK, spaceAfter=5),
    "sub": ParagraphStyle("sub", fontName="DV", fontSize=9, leading=12, textColor=colors.HexColor("#6b7280"), spaceAfter=8),
    "cell": ParagraphStyle("cell", fontName="DV", fontSize=7.6, leading=9.6, textColor=INK),
    "hcell": ParagraphStyle("hcell", fontName="DVB", fontSize=7.6, leading=9.6, textColor=INK),
    "li": ParagraphStyle("li", fontName="DV", fontSize=9, leading=12.5, textColor=INK, leftIndent=12, bulletIndent=2, spaceAfter=2),
}

def inline(t):
    t = t.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
    t = re.sub(r"\[([^\]]+)\]\(([^)]+)\)", r'<link href="\2" color="#1d4ed8">\1</link>', t)
    t = re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", t)
    t = re.sub(r"~~(.+?)~~", r"<strike>\1</strike>", t)
    return t

def tree():
    W, H = 170 * mm, 172
    d = Drawing(W, H)
    def box(x, y, w, h, title, sub, dashed=False, strong=False):
        r = Rect(x, y, w, h, rx=4, ry=4, strokeColor=ACC if strong else INK,
                 strokeWidth=1.4 if strong else 0.8,
                 fillColor=colors.HexColor("#fdf3e7") if strong else colors.white)
        if dashed:
            r.strokeDashArray = [3, 2]
        d.add(r)
        d.add(String(x + w / 2, y + h - 12, title, fontName="DVB", fontSize=7.6, fillColor=INK, textAnchor="middle"))
        for i, s in enumerate(sub):
            d.add(String(x + w / 2, y + h - 23 - 9 * i, s, fontName="DV", fontSize=6.6, fillColor=INK, textAnchor="middle"))
    def link(x1, y1, x2, y2, dashed=False):
        l = Line(x1, y1, x2, y2, strokeColor=colors.HexColor("#6b7280"), strokeWidth=0.7)
        if dashed:
            l.strokeDashArray = [3, 2]
        d.add(l)
    # niveau 1
    bw, bh = 150, 34
    box(W / 2 - bw / 2, H - bh - 2, bw, bh, "KPI de décision : K1", ["Départs par jour, juin ÷ juillet-août"], strong=True)
    # niveau 2
    cw, ch = 88, 34
    xs = [4, 98, 192, 286, 380]
    lv2 = [("K2 (pilotage)", ["Surface brûlée/jour", "juin ÷ juillet-août"], False),
           ("K4 (pilotage)", ["Part des feux > 1 ha", "juin vs juillet-août"], False),
           ("Pilotage", ["Bâtiments détruits", "par les feux de juin"], False),
           ("K3 (contexte)", ["Jours de danger élevé", "juin ÷ juillet-août"], True),
           ("Contexte", ["Date du 10e départ", "de l'année"], True)]
    y2 = H - bh - 2 - 30 - ch
    top_mid_y = H - bh - 2
    for x, (t, s, dsh) in zip(xs, lv2):
        box(x, y2, cw, ch, t, s, dashed=dsh)
        link(W / 2, top_mid_y, x + cw / 2, y2 + ch, dashed=dsh)
    # niveau 3 sous K2
    y3 = y2 - 30 - ch
    for i, (t, s) in enumerate([("Opérationnel", ["Effectif saisonnier", "présent en juin*"]),
                                ("Opérationnel", ["Délai d'arrivée", "sur feu en juin*"])]):
        x = 4 + i * 94
        box(x, y3, cw, ch, t, s)
        link(xs[0] + cw / 2, y2, x + cw / 2, y3 + ch)
    d.add(String(200, y3 + 20, "Pointillés : indicateurs de contexte (non pilotés).", fontName="DV", fontSize=6.8, fillColor=INK))
    d.add(String(200, y3 + 9, "* à collecter auprès du SDIS : non publics.", fontName="DV", fontSize=6.8, fillColor=INK))
    return d

def table(rows):
    data = []
    for i, r in enumerate(rows):
        data.append([Paragraph(inline(c), st["hcell"] if i == 0 else st["cell"]) for c in r])
    n = len(rows[0])
    total = 174 * mm
    plans = {2: (45,), 3: (60, 40), 4: (30, 48, 48), 6: (7, 62, 22, 18, 22)}
    fixed = [w * mm for w in plans.get(n, ())]
    widths = fixed + [(total - sum(fixed)) / (n - len(fixed))] * (n - len(fixed))
    t = Table(data, colWidths=widths, repeatRows=1)
    t.setStyle(TableStyle([
        ("GRID", (0, 0), (-1, -1), 0.4, GRID),
        ("BACKGROUND", (0, 0), (-1, 0), HEAD),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("LEFTPADDING", (0, 0), (-1, -1), 4), ("RIGHTPADDING", (0, 0), (-1, -1), 4),
        ("TOPPADDING", (0, 0), (-1, -1), 3), ("BOTTOMPADDING", (0, 0), (-1, -1), 3),
    ]))
    return t

def build(src, out):
    lines = open(src, encoding="utf-8").read().split("\n")
    story, i = [], 0
    while i < len(lines):
        ln = lines[i]
        if ln.startswith("**Arbre de KPIs**"):
            story += [Paragraph("<b>Arbre de KPIs.</b>", st["p"]), tree(), Spacer(1, 6)]
            i += 1
            while i < len(lines) and (lines[i].strip() == "" or lines[i].lstrip().startswith("- ")):
                i += 1
            continue
        if ln.startswith("# "):
            story.append(Paragraph(inline(ln[2:]), st["h1"]))
            if i + 2 < len(lines) and lines[i + 2] and not lines[i + 2].startswith("#"):
                story.append(Paragraph(inline(lines[i + 2]), st["sub"])); i += 3; continue
        elif ln.startswith("## "):
            story.append(Paragraph(inline(ln[3:]), st["h2"]))
        elif ln.startswith("### "):
            story.append(Paragraph(inline(ln[4:]), st["h3"]))
        elif ln.startswith("|"):
            rows = []
            while i < len(lines) and lines[i].startswith("|"):
                cells = [c.strip() for c in lines[i].strip().strip("|").split("|")]
                if not all(re.fullmatch(r":?-+:?", c) for c in cells):
                    rows.append(cells)
                i += 1
            story += [KeepTogether(table(rows)), Spacer(1, 6)]
            continue
        elif ln.lstrip().startswith("- "):
            depth = (len(ln) - len(ln.lstrip())) // 4
            s = ParagraphStyle("l", parent=st["li"], leftIndent=12 + 12 * depth, bulletIndent=2 + 12 * depth)
            story.append(Paragraph(inline(ln.lstrip()[2:]), s, bulletText="•"))
        elif ln.strip():
            story.append(Paragraph(inline(ln), st["p"]))
        i += 1
    doc = SimpleDocTemplate(out, pagesize=A4, leftMargin=18 * mm, rightMargin=18 * mm,
                            topMargin=16 * mm, bottomMargin=16 * mm,
                            title="Atelier 1 : de la décision au premier chiffre")
    doc.build(story)

if __name__ == "__main__":
    build(sys.argv[1], sys.argv[2])
