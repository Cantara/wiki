# Cantara Wiki

Archive of the Cantara open source community wiki, originally hosted at wiki.cantara.no (Confluence).

Content recovered from the [Wayback Machine](https://web.archive.org/) snapshot (last captured 2022).

**Live site:** https://cantara.github.io/wiki/

## Spaces

- **Whydah** – IAM/SSO open source project
- **Platform Engineering** – Community events, JavaZone, IASA
- **Open Web Services & SOA** – SOA patterns and governance
- **Enterprise Architecture** – EA models and patterns
- **Agile Development** – Agile practices and methodology
- **EDR** – Enterprise Domain Repository
- And more…

## Local development

```bash
pip install mkdocs mkdocs-material
mkdocs serve
```

## How this was built

Pages were fetched from the Wayback Machine CDX API and converted from Confluence HTML
to Markdown using BeautifulSoup + markdownify. See the [archive scripts](https://github.com/Cantara/wiki/tree/main).
