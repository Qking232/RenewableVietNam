# Press kit source

The press kit at <https://renewablevietnam.com/presskit/> is generated from the
`data.xml` files in this folder by [presskit.html](https://github.com/pixelnest/presskit.html).

- `data.xml` — the company page (site root of the press kit)
- `vietnam-map/data.xml` — the interactive map product page
- `images/` — logo, header banner and favicon

## Rebuild

```bash
npm install -g presskit          # once; needs Node.js 20.9+
presskit build presskit-src --pretty-links
rm -rf presskit && cp -R build presskit
```

The generated output is committed to `presskit/`, which is what GitHub Pages serves.
This folder is excluded from the Jekyll build via `exclude:` in `_config.yml`.
