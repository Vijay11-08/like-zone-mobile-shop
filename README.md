# Like Zone Mobile Shop — Web Application

A modern, premium, fully responsive static web application for **Like Zone Mobile Shop**, a local mobile phone and accessories store located in Tramba, Rajkot, Gujarat.

---

## Business Information

| Detail       | Info                                              |
|--------------|---------------------------------------------------|
| Shop Name    | Like Zone Mobile Shop                             |
| Location     | Kasturba Dham, Tramba, Rajkot, Gujarat – 360020  |
| Phone        | +91 99046 40764                                   |
| WhatsApp     | +91 99046 40764                                   |
| Google Rating| 4.2 ⭐ (22 Google Reviews)                        |

---

## Tech Stack

- **HTML5** — Semantic markup
- **CSS3** — Glassmorphism design, CSS variables, animations
- **JavaScript (Vanilla)** — Chatbot, scroll reveal, WhatsApp integration
- **Bootstrap 5** — Responsive grid and components
- **Bootstrap Icons** — Icon library
- **Google Fonts** — Poppins & Inter

No backend, no framework, no database — fully static.

---

## File Structure

```
like-zone-mobile-shop/
│
├── index.html          # Main HTML file (all sections)
│
├── css/
│   └── style.css       # Glassmorphism theme, all styles
│
├── js/
│   └── script.js       # Chatbot, WhatsApp, animations
│
├── images/             # Place shop/product images here
│   ├── logo.png
│   ├── shop.jpg
│   ├── team-1.jpg
│   ├── team-2.jpg
│   ├── team-3.jpg
│   └── team-4.jpg
│
└── README.md
```

---

## Sections

1. **Navbar** — Sticky glass navbar with hamburger menu on mobile
2. **Hero** — Full-screen hero with phone mockup, floating cards, CTA buttons
3. **Quick Actions** — 4 quick-access cards (Mobiles, Accessories, Services, WhatsApp)
4. **About** — Shop info, stats, icon grid
5. **Mobile Phones** — 6 brand cards (Samsung, Apple, Redmi, Realme, Vivo, Oppo)
6. **Accessories** — 6 accessory cards with WhatsApp enquiry buttons
7. **Services** — 6 service cards with glowing icons
8. **Why Choose Us** — 6 reason cards
9. **Team** — 4 placeholder team member cards (replace names when available)
10. **Reviews** — Bootstrap carousel with sample placeholder reviews
11. **Location** — Google Maps embed + address card
12. **Contact** — Call, WhatsApp, and Visit cards
13. **WhatsApp CTA** — Full-width WhatsApp call-to-action banner
14. **Footer** — Links, contact info, social buttons, copyright
15. **Floating Buttons** — Fixed WhatsApp + Call buttons (bottom-right)
16. **Chatbot** — Rule-based JS chatbot with quick replies

---

## Customisation Guide

### 1. Update Team Member Names
In `index.html`, search for `[Team Member Name]` and replace with actual names.

### 2. Update Google Maps Embed
In `index.html`, find the `<iframe>` inside `.map-container` and replace the `src` with the actual Google Maps embed URL for the shop.

### 3. Add Images
Place actual images in the `images/` folder and update `src` attributes in `index.html`.

### 4. Update Reviews
Replace the sample review text in the `#reviews` section with actual customer reviews.

### 5. WhatsApp Number
The WhatsApp number `919904640764` is used throughout. To change it, search and replace in both `index.html` and `js/script.js`.

---

## Features

- ✅ Glassmorphism UI with `backdrop-filter: blur()`
- ✅ Fully responsive (mobile, tablet, desktop)
- ✅ One-click WhatsApp integration
- ✅ One-click phone call integration
- ✅ Rule-based JavaScript chatbot (no API)
- ✅ Scroll reveal animations (Intersection Observer)
- ✅ Floating WhatsApp + Call buttons
- ✅ Bootstrap 5 carousel for reviews
- ✅ Sticky glass navbar with active link tracking
- ✅ SEO meta tags
- ✅ Accessible HTML (ARIA labels, semantic tags)
- ✅ No console errors
- ✅ No external dependencies beyond CDN links

---

## How to Run

Simply open `index.html` in any modern web browser. No build step or server required.

```
like-zone-mobile-shop/index.html
```

Or serve with any static file server:

```bash
# Python
python -m http.server 8080

# Node.js (npx)
npx serve .
```

---

## License

This project is created for **Like Zone Mobile Shop** for business use.

© 2026 Like Zone Mobile Shop. All Rights Reserved.