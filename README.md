# CABANA FISH

Premium B2B seafood export website for CABANA FISH, a Mauritanian supplier serving international importers, distributors, processors, retailers, and food-service companies.

## Pages

- `index.html` - Main corporate website and product catalog
- `quote.html` - Dedicated professional quotation request page

## Features

- Responsive desktop, tablet, and mobile layout
- Official CABANA FISH branding
- Fresh seafood-only product imagery
- Filterable seafood product catalog
- Quality standards and export capabilities sections
- Animated global export map
- Dedicated quotation request workflow
- Direct sales contact by email
- Scroll, hover, route, and hero animations
- Reduced-motion accessibility support

## Product Catalog

- Poulpe / Octopus
- Calamar
- Choco
- Thierny
- Bengoua
- Roubio
- Mongo
- Tako

## Contact

Sales email: [contact@cabanafish.com](mailto:contact@cabanafish.com)

## Project Structure

```text
CabanaFish/
|-- assets/
|   |-- cabanafish-header-logo.png
|   |-- cabanafish-logo-tight.png
|   |-- cabanafish-logo.jpeg
|   |-- fresh-cephalopods.png
|   |-- fresh-fish.png
|   `-- fresh-seafood-hero.png
|-- index.html
|-- quote.html
|-- script.js
|-- styles.css
`-- README.md
```

## Run Locally

The website can be opened directly by opening `index.html`.

For a local HTTP server, run:

```powershell
python -m http.server 4173
```

Then open:

```text
http://localhost:4173
```

## Customization

- Main website content: `index.html`
- Quotation form content: `quote.html`
- Colors, layout, responsiveness, and animations: `styles.css`
- Product filters, form behavior, and header interactions: `script.js`
- Logos and seafood photography: `assets/`

## Brand Colors

- Navy Blue: `#092647`
- Ocean Teal: `#259FA2`
- White: `#FDFDFD`
- Silver: `#96A1AE`

## Deployment

This is a static website with no build step or external framework. It can be deployed to any static hosting provider.

The quotation form currently displays a confirmation message in the browser. Connect it to a backend, email service, or form provider before production deployment.
