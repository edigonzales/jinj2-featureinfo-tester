import json
from pathlib import Path
from jinja2 import Environment, BaseLoader, select_autoescape


# ============================================================
# INPUTS
# ============================================================

JSON_FIELD_AS_STRING = r'''
[
  {
    "Wert": "geschützt",
    "@type": "SO_ARP_Solaranlagen_Bewilligungsverfahren_20260313.Objektinformation",
    "Thema": "Denkmalschutz",
    "Bezeichnung": "Schutzstatus"
  },
  {
    "Wert": "geschützt",
    "@type": "SO_ARP_Solaranlagen_Bewilligungsverfahren_20260313.Objektinformation",
    "Thema": "Denkmalschutz",
    "Bezeichnung": "Schutzstatus"
  },
  {
    "Wert": "geschützt",
    "@type": "SO_ARP_Solaranlagen_Bewilligungsverfahren_20260313.Objektinformation",
    "Thema": "Denkmalschutz",
    "Bezeichnung": "Schutzstatus"
  },
  {
    "Wert": "geschützt",
    "@type": "SO_ARP_Solaranlagen_Bewilligungsverfahren_20260313.Objektinformation",
    "Thema": "Denkmalschutz",
    "Bezeichnung": "Schutzstatus"
  },
  {
    "Wert": "Jesuitenkirche",
    "@type": "SO_ARP_Solaranlagen_Bewilligungsverfahren_20260313.Objektinformation",
    "Thema": "Denkmalschutz",
    "Bezeichnung": "Objektname"
  },
  {
    "Wert": "Haus Hauptgasse 62",
    "@type": "SO_ARP_Solaranlagen_Bewilligungsverfahren_20260313.Objektinformation",
    "Thema": "Denkmalschutz",
    "Bezeichnung": "Objektname"
  },
  {
    "Wert": "Schulhaus Kollegium",
    "@type": "SO_ARP_Solaranlagen_Bewilligungsverfahren_20260313.Objektinformation",
    "Thema": "Denkmalschutz",
    "Bezeichnung": "Objektname"
  },
  {
    "Wert": "Steinmuseum",
    "@type": "SO_ARP_Solaranlagen_Bewilligungsverfahren_20260313.Objektinformation",
    "Thema": "Denkmalschutz",
    "Bezeichnung": "Objektname"
  },
  {
    "Wert": "https://geo.so.ch/docs/ch.so.ada.denkmalschutz/objektblatt/100003229.pdf",
    "@type": "SO_ARP_Solaranlagen_Bewilligungsverfahren_20260313.Objektinformation",
    "Thema": "Denkmalschutz",
    "Bezeichnung": "Objektblatt"
  },
  {
    "Wert": "https://geo.so.ch/docs/ch.so.ada.denkmalschutz/objektblatt/100003357.pdf",
    "@type": "SO_ARP_Solaranlagen_Bewilligungsverfahren_20260313.Objektinformation",
    "Thema": "Denkmalschutz",
    "Bezeichnung": "Objektblatt"
  },
  {
    "Wert": "https://geo.so.ch/docs/ch.so.ada.denkmalschutz/objektblatt/100005252.pdf",
    "@type": "SO_ARP_Solaranlagen_Bewilligungsverfahren_20260313.Objektinformation",
    "Thema": "Denkmalschutz",
    "Bezeichnung": "Objektblatt"
  },
  {
    "Wert": "https://geo.so.ch/docs/ch.so.ada.denkmalschutz/objektblatt/100005671.pdf",
    "@type": "SO_ARP_Solaranlagen_Bewilligungsverfahren_20260313.Objektinformation",
    "Thema": "Denkmalschutz",
    "Bezeichnung": "Objektblatt"
  },
  {
    "@type": "SO_ARP_Solaranlagen_Bewilligungsverfahren_20260313.Objektinformation",
    "Thema": "Denkmalschutz",
    "Dokumente": [
      {
        "Link": "https://geo.so.ch/docs/ch.so.ada.denkmalschutz/rechtsvorschrift/100255709.pdf",
        "@type": "SO_ARP_Solaranlagen_Bewilligungsverfahren_20260313.Dokument",
        "Datum": "1939-03-14",
        "Titel": "Stadt Solothurn: Amtliches Inventar der unter öffentlichem Schutz stehenden Altertümer des Kantons Solothurn",
        "Nummer": "1939/1187",
        "Abkuerzung": null,
        "Rechtsstatus": null
      }
    ],
    "Bezeichnung": "Dokumente"
  },
  {
    "@type": "SO_ARP_Solaranlagen_Bewilligungsverfahren_20260313.Objektinformation",
    "Thema": "Denkmalschutz",
    "Dokumente": [
      {
        "Link": "https://geo.so.ch/docs/ch.so.ada.denkmalschutz/rechtsvorschrift/100255746.pdf",
        "@type": "SO_ARP_Solaranlagen_Bewilligungsverfahren_20260313.Dokument",
        "Datum": "1983-09-27",
        "Titel": "Beitrag an die Restaurierung des AEK-Gebäudes, Hauptgasse 62, Solothurn",
        "Nummer": "1983/2755",
        "Abkuerzung": null,
        "Rechtsstatus": null
      }
    ],
    "Bezeichnung": "Dokumente"
  },
  {
    "@type": "SO_ARP_Solaranlagen_Bewilligungsverfahren_20260313.Objektinformation",
    "Thema": "Denkmalschutz",
    "Dokumente": [
      {
        "Link": "https://geo.so.ch/docs/ch.so.ada.denkmalschutz/rechtsvorschrift/100255799.pdf",
        "@type": "SO_ARP_Solaranlagen_Bewilligungsverfahren_20260313.Dokument",
        "Datum": "2009-10-20",
        "Titel": "Solothurn: Unterschutzstellung Kollegium-Schulhaus, Goldgasse 2, GB Nr. 512",
        "Nummer": "2009/1774",
        "Abkuerzung": null,
        "Rechtsstatus": null
      }
    ],
    "Bezeichnung": "Dokumente"
  },
  {
    "@type": "SO_ARP_Solaranlagen_Bewilligungsverfahren_20260313.Objektinformation",
    "Thema": "Denkmalschutz",
    "Dokumente": [
      {
        "Link": "https://geo.so.ch/docs/ch.so.ada.denkmalschutz/rechtsvorschrift/100255709.pdf",
        "@type": "SO_ARP_Solaranlagen_Bewilligungsverfahren_20260313.Dokument",
        "Datum": "1939-03-14",
        "Titel": "Stadt Solothurn: Amtliches Inventar der unter öffentlichem Schutz stehenden Altertümer des Kantons Solothurn",
        "Nummer": "1939/1187",
        "Abkuerzung": null,
        "Rechtsstatus": null
      }
    ],
    "Bezeichnung": "Dokumente"
  },
  {
    "Wert": "Lichthäuschen Hauptgasse 62",
    "@type": "SO_ARP_Solaranlagen_Bewilligungsverfahren_20260313.Objektinformation",
    "Thema": "Denkmalschutz",
    "Bezeichnung": "Objektname"
  },
  {
    "Wert": "geschützt",
    "@type": "SO_ARP_Solaranlagen_Bewilligungsverfahren_20260313.Objektinformation",
    "Thema": "Denkmalschutz",
    "Bezeichnung": "Schutzstatus"
  },
  {
    "Wert": "https://geo.so.ch/docs/ch.so.ada.denkmalschutz/objektblatt/100044714.pdf",
    "@type": "SO_ARP_Solaranlagen_Bewilligungsverfahren_20260313.Objektinformation",
    "Thema": "Denkmalschutz",
    "Bezeichnung": "Objektblatt"
  },
  {
    "@type": "SO_ARP_Solaranlagen_Bewilligungsverfahren_20260313.Objektinformation",
    "Thema": "Denkmalschutz",
    "Dokumente": [
      {
        "Link": "https://geo.so.ch/docs/ch.so.ada.denkmalschutz/rechtsvorschrift/100255746.pdf",
        "@type": "SO_ARP_Solaranlagen_Bewilligungsverfahren_20260313.Dokument",
        "Datum": "1983-09-27",
        "Titel": "Beitrag an die Restaurierung des AEK-Gebäudes, Hauptgasse 62, Solothurn",
        "Nummer": "1983/2755",
        "Abkuerzung": null,
        "Rechtsstatus": null
      }
    ],
    "Bezeichnung": "Dokumente"
  },
  {
    "Wert": "Solothurn",
    "@type": "SO_ARP_Solaranlagen_Bewilligungsverfahren_20260313.Objektinformation",
    "Thema": "ISOS-A",
    "Bezeichnung": "Objektname"
  },
  {
    "Wert": "1",
    "@type": "SO_ARP_Solaranlagen_Bewilligungsverfahren_20260313.Objektinformation",
    "Thema": "ISOS-A",
    "Bezeichnung": "Nummer"
  },
  {
    "Wert": "https://api.isos.bak.admin.ch/ob/3203/doc/ISOS_3203.pdf",
    "@type": "SO_ARP_Solaranlagen_Bewilligungsverfahren_20260313.Objektinformation",
    "Thema": "ISOS-A",
    "Bezeichnung": "Objektblatt"
  },
  {
    "Wert": "A - Kulturgut von nationaler Bedeutung",
    "@type": "SO_ARP_Solaranlagen_Bewilligungsverfahren_20260313.Objektinformation",
    "Thema": "KGS-Objekt",
    "Bezeichnung": "Kategorie"
  },
  {
    "Wert": "Jesuitenkirche mit Kollegium (Lapidarium)",
    "@type": "SO_ARP_Solaranlagen_Bewilligungsverfahren_20260313.Objektinformation",
    "Thema": "KGS-Objekt",
    "Bezeichnung": "Bezeichnung"
  },
  {
    "Wert": "N140_Kernzone",
    "@type": "SO_ARP_Solaranlagen_Bewilligungsverfahren_20260313.Objektinformation",
    "Thema": "Nutzungsplanung",
    "Bezeichnung": "Typ"
  },
  {
    "Wert": "Altstadtzone",
    "@type": "SO_ARP_Solaranlagen_Bewilligungsverfahren_20260313.Objektinformation",
    "Thema": "Nutzungsplanung",
    "Bezeichnung": "Bezeichnung"
  }
]
'''

ART_TXT = "Gebäude"
BEWILLIGUNGSVERFAHREN_TXT = "Baubewilligungsverfahren"


# ============================================================
# JINJA2 TEMPLATE
# ============================================================

TEMPLATE_STRING = r'''
<table class="attribute-list">
  <tbody>

  {% if feature.art_txt is defined and feature.art_txt is not none and feature.art_txt != '' %}
    <tr>
      <td class="identify-attr-title wrap"><i>Art</i></td>
      <td class="identify-attr-value wrap">{{ render_value(feature.art_txt) }}</td>
    </tr>
  {% endif %}

  {% if feature.bewilligungsverfahren_txt is defined and feature.bewilligungsverfahren_txt is not none and feature.bewilligungsverfahren_txt != '' %}
    <tr>
      <td class="identify-attr-title wrap"><i>Bewilligungsverfahren</i></td>
      <td class="identify-attr-value wrap">{{ render_value(feature.bewilligungsverfahren_txt) }}</td>
    </tr>
  {% endif %}

  {% set infos = feature.objektinformationen %}

  {% if infos and infos != '-' %}

    {% for themengruppe in infos|groupby('Thema') %}
      {% set thema = themengruppe.grouper %}
      {% set eintraege = themengruppe.list %}

      {% for eintrag in eintraege %}

        {% if eintrag.Bezeichnung is defined
              and eintrag.Bezeichnung is not none
              and eintrag.Wert is defined
              and eintrag.Wert is not none %}
          <tr>
            <td class="identify-attr-title wrap">
              <i>({{ thema }}) {{ eintrag.Bezeichnung }}</i>
            </td>
            <td class="identify-attr-value wrap">
              {{ render_value(eintrag.Wert) }}
            </td>
          </tr>
        {% endif %}

        {% if eintrag.Bezeichnung is defined
              and eintrag.Bezeichnung == 'Dokumente'
              and eintrag.Dokumente is defined
              and eintrag.Dokumente %}
          <tr>
            <td class="identify-attr-title wrap">
              <i>({{ thema }}) Dokumente</i>
            </td>
            <td class="identify-attr-value wrap" style="padding-left: 0; padding-right: 0.25em;">
              {% for dokument in eintrag.Dokumente %}
                <table class="attribute-list" style="width: 100%; margin-bottom: 0.5em;">
                  <tbody>
                    {% for key, value in dokument.items() %}
                      {% if key != '@type' and value is not none and value != '' %}
                        <tr>
                          <td class="identify-attr-title wrap" style="width: 35%;">
                            <i>{{ key }}</i>
                          </td>
                          <td class="identify-attr-value wrap">
                            {{ render_value(value) }}
                          </td>
                        </tr>
                      {% endif %}
                    {% endfor %}
                  </tbody>
                </table>
              {% endfor %}
            </td>
          </tr>
        {% endif %}

      {% endfor %}
    {% endfor %}

  {% endif %}

  </tbody>
</table>
'''


# ============================================================
# HELPERS
# ============================================================

def render_value(value):
    """
    Vereinfachte lokale Version von QWC render_value(...).

    - URLs werden als Links ausgegeben
    - andere Werte werden als String zurückgegeben
    """
    if value is None:
        return ""

    text = str(value)

    if text.startswith("http://") or text.startswith("https://"):
        return f'<a href="{text}" target="_blank" rel="noopener noreferrer">{text}</a>'

    return text


HTML_PAGE_TEMPLATE = """<!DOCTYPE html>
<html lang="de">
<head>
  <meta charset="utf-8">
  <title>QWC Feature Info Debug</title>
  <style>
    body {
      font-family: Arial, Helvetica, sans-serif;
      margin: 24px;
      color: #222;
    }
    h1 {
      font-size: 20px;
      margin-bottom: 16px;
    }
    table.attribute-list {
      border-collapse: collapse;
      width: 100%;
      max-width: 1100px;
      font-size: 14px;
    }
    table.attribute-list td {
      border: 1px solid #d0d0d0;
      padding: 6px 8px;
      vertical-align: top;
    }
    td.identify-attr-title {
      width: 32%;
      background: #f3f3f3;
      font-style: italic;
    }
    td.identify-attr-value {
      width: 68%;
      background: #fff;
    }
    .wrap {
      word-break: break-word;
      overflow-wrap: anywhere;
    }
    .container {
      max-width: 1200px;
    }
  </style>
</head>
<body>
  <div class="container">
    <h1>QWC Feature Info Debug</h1>
    {{ content | safe }}
  </div>
</body>
</html>
"""


# ============================================================
# MAIN
# ============================================================

def main():
    try:
        json_data = json.loads(JSON_FIELD_AS_STRING)
    except json.JSONDecodeError as exc:
        raise SystemExit(f"Fehler beim Parsen des JSON-Strings: {exc}")

    # Simuliertes feature-Objekt wie in QWC/Jinja
    feature = {
        "art_txt": ART_TXT,
        "bewilligungsverfahren_txt": BEWILLIGUNGSVERFAHREN_TXT,
        "objektinformationen": json_data,
    }

    env = Environment(
        loader=BaseLoader(),
        autoescape=select_autoescape(enabled_extensions=("html", "xml")),
    )

    template = env.from_string(TEMPLATE_STRING)
    rendered_fragment = template.render(feature=feature, render_value=render_value)

    page_template = env.from_string(HTML_PAGE_TEMPLATE)
    rendered_page = page_template.render(content=rendered_fragment)

    output_path = Path("qwc_featureinfo_debug.html")
    output_path.write_text(rendered_page, encoding="utf-8")

    print(f"HTML erfolgreich erzeugt: {output_path.resolve()}")


if __name__ == "__main__":
    main()