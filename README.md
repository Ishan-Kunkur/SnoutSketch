# SnoutSketch

SnoutSketch is a webapp that transforms close-up images of dog noses into unique, AI-generated artwork. Using the ridges and patterns of a dog's nose (like a fingerprint!), it creates one-of-a-kind pieces in various styles. Originally built with basic programmatic art, it now leverages **Neural Style Transfer (NST)** for wild, crazy outputs that turn your pup’s snout into something extraordinary.

## Features
- **Upload**: Drop a close-up dog nose image.
- **Styles**: Choose from basic styles (pixel-based) or enhanced, AI-driven styles.
- **Download**: Get your artwork in low (1080p) and high (4K) resolutions.

## Current Enhancements (March 2025)
We’ve upgraded SnoutSketch with **crazier NST styles** using a pre-trained VGG19 model. These enhancements take your nose image and blend it with wild style images for insane, artistic results:
- **Nebula Frenzy** (replaces Cosmic Canine): Nose ridges explode into a neon-charged cosmic nebula—think psychedelic chaos with glowing swirls.
- **Scream of the Void** (replaces Echoes of the Snout): A surreal, warped nightmare—your nose melts into a glitchy, howling void inspired by "The Scream."
- **Digital Meltdown** (replaces Snout Circuit): A cyberpunk fever dream—nose lines fry into a neon-drenched circuit overload.
- **Mad Weaver’s Labyrinth** (replaces Nose Tapestry): A frantic, dripping scribble-fest—nose lost in a chaotic Pollock-style weave.

These styles use higher style weights (2000–5000), custom VGG19 layers, and more iterations for maximum madness, all while keeping the nose’s unique ridges as the base.

## Setup
### Prerequisites
- **Node.js**: For the React frontend (LTS recommended, e.g., 20.x).
- **Python 3.9+**: For the FastAPI backend.
- **Dependencies**:
  - Frontend: `npm install` in `frontend/`.
  - Backend: `pip install fastapi uvicorn opencv-python pillow python-multipart torch torchvision` in `backend/`.

### Project Structure
dog-nose-art/
├── frontend/
│   ├── src/
│   │   ├── App.js      # React UI with style dropdown
│   │   └── App.css     # Basic styling
├── backend/
│   ├── main.py         # FastAPI server
│   ├── process.py      # NST and basic art generation
│   └── styles/         # Style images (e.g., nebula_frenzy.jpg)
└── README.md           # This file

