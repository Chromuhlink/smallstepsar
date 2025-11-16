# Small Steps AR

WebAR demo for presentation purposes. Point your camera at a target image to see a 3D object appear and interact with it.

## Demo

1. Open on mobile: `https://your-domain/index.html`
2. Allow camera access
3. Point camera at the target image
4. Tap the 3D object to collect it (+20 appears)
5. Object respawns after 5 seconds

## Files

- `index.html` - Main AR app
- `30-3d-icon.glb` - 3D model
- `targets.mind` - Compiled image target
- `dtg-mccarren-park-track-field-open-2019-03-01-bk02_z.webp` - Target image

## Setup

Requires HTTPS for camera access. Use GitHub Pages or any HTTPS server.

## Tech

- MindAR.js for image tracking
- A-Frame for 3D rendering
