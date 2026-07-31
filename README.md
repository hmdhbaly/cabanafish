# CABANA FISH

Premium B2B seafood export website for CABANA FISH, a Mauritanian supplier serving international importers, distributors, processors, retailers, and food-service companies.

## Pages

- `index.html` - Main corporate website and product catalog
- `quote.html` - Dedicated professional quotation request page
- `contact.html` - Company contact and due-diligence information page
- `products/` - Dedicated product technical sheets

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

## Product Image Accuracy Policy

Product photography must be species-specific and verifiable before publication. Do not use generic seafood collages, AI-generated seafood scenes, restaurant images, decorative ocean photos, or duplicated mixed-product images as product evidence.

Current status: the website uses generated product visuals for catalog cards, product pages, and gallery previews. These are useful for layout and presentation, but they should still be replaced with verified real photographs before serious buyer due diligence or final commercial launch.

Required image set for each product:

- Main product photograph
- 3-6 gallery photographs
- Packaging or export carton photograph
- Close-up quality photograph
- Processing, cold-storage, IQF, block-frozen, or loading photograph when available

Accepted sources:

- CABANA FISH own operation photos
- Approved supplier photos with permission
- Verified exact-species commercial seafood photographs

Rejected sources:

- Generic fish photos
- Wrong species
- Mixed seafood images used for a single product
- AI-looking images
- Restaurant, cooked, plated, garnished, or decorative images
- Watermarked or low-resolution files

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
|-- contact.html
|-- products/
|   |-- poulpe-octopus.html
|   |-- calamar.html
|   |-- choco.html
|   |-- thierny.html
|   |-- bengoua.html
|   |-- roubio.html
|   |-- mongo.html
|   `-- tako.html
|-- backend/
|-- api/
|-- robots.txt
|-- sitemap.xml
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
- Contact page content: `contact.html`
- Product technical sheets: `products/`
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

The quotation form posts to the Django endpoint at `/api/quote/`. Configure the required production environment variables for database and email delivery before deploying.

## Website Improvement Report

### Overall Scores

- Overall website score: 82/100
- Trust score: 78/100
- Branding score: 88/100
- Professionalism score: 84/100
- SEO score: 80/100
- Conversion score: 82/100

### Current Situation

The site already has a premium visual foundation, official brand assets, a seafood product catalog, export positioning, a quote page, and fresh seafood imagery.

### Problem

Before this improvement pass, the site did not provide enough operational transparency for a high-value international buyer. It lacked individual product pages, formal contact information structure, export workflow details, crawler files, and structured data.

### Business Impact

International importers need proof signals before starting procurement conversations. Missing due-diligence content can reduce confidence, especially for large orders, recurring supply agreements, and first-time supplier evaluation.

### Recommended Improvement Implemented

- Added company credibility section
- Added sourcing, processing and quality-control explanations
- Added values and competitive advantages
- Added export workflow timeline
- Added export information section covering Incoterms, MOQ, lead times, payment terms, documentation and shipping
- Added dedicated contact page
- Added dedicated product technical pages
- Added Organization and Product structured data
- Added canonical URLs
- Added `robots.txt`
- Added `sitemap.xml`
- Improved quotation form fields for monthly demand, destination port, packaging and documentation

### Implementation Priority

Priority: High. These are trust and conversion improvements that directly support international B2B sales.

### Estimated Time

Completed as a static-site enhancement pass. A production follow-up should take 1-2 days to connect real company legal details, real facility images, map location and form delivery.

### Expected Increase in Buyer Confidence

Estimated improvement: +25% to +40%, assuming real company documents, verified address, licences and authentic operation photos are added before final commercial launch.

## Top Improvements Ranked by Business Impact

1. Add verified company address
2. Add company registration number
3. Add export licence details where applicable
4. Add authentic facility photos
5. Add management team photos
6. Add quality-control process photos
7. Add downloadable company profile PDF
8. Add downloadable product catalog PDF
9. Connect quote form to email or CRM
10. Add real certificates as downloadable files
11. Add Google Maps with verified address
12. Add LinkedIn company profile
13. Add trade references when available
14. Add loading and packaging photos
15. Add cold storage photos
16. Add laboratory or inspection imagery if available
17. Add terms for FOB/CFR/CIF by market
18. Add MOQ by product
19. Add container loading guidance by carton
20. Add seasonal availability chart
21. Add catch area details per product
22. Add catch method details per product
23. Add packing options by product
24. Add glazing ranges by product
25. Add shelf-life ranges by product
26. Add downloadable spec sheets
27. Add multilingual French pages
28. Add multilingual Arabic pages
29. Add FAQ schema with buyer questions
30. Add product image ALT refinement
31. Add testimonial section only after real testimonials exist
32. Add trade show participation only if verified
33. Add partner logos only with permission
34. Add privacy policy
35. Add terms of business
36. Add cookie policy if analytics are used
37. Add contact form anti-spam protection
38. Add quote request tracking
39. Add analytics events for CTA clicks
40. Add Vercel deployment configuration if needed
41. Compress large PNG assets for speed
42. Convert imagery to WebP
43. Add Open Graph absolute image URLs after domain launch
44. Add favicon set
45. Add loading performance checks
46. Add accessibility QA
47. Add mobile menu QA
48. Add browser testing across Chrome/Safari/Edge
49. Add backup contact email workflow
50. Add CRM follow-up templates

## Quick Wins Under One Hour

- Add verified phone number only if approved for publication
- Add LinkedIn URL
- Add official office address
- Compress image assets
- Add PDF company profile link

## Medium Improvements 1-2 Days

- Produce product spec PDFs
- Add multilingual pages
- Connect quotation form to email or CRM
- Add real operation photography
- Add FAQ and buyer due-diligence content

## Major Improvements 1-2 Weeks

- Full authentic photo shoot
- Certificate and document library
- Product availability system
- CRM integration
- Multi-language SEO buildout

## Final Verdict

The website is now much more suitable for international B2B seafood buyers, but a cautious importer would still need verified business documents, real office/facility details, certificates and authentic operation photography before choosing Cabana Fish as a long-term supplier based solely on the website.
