SnoutSketch - Overview
SnoutSketch is a webapp that turns your dog’s nose into a unique piece of art. It’s perfect for dog lovers who want to celebrate their pup’s individuality and tech enthusiasts who dig image processing. You upload a close-up photo of your dog’s snout, and the app analyzes its ridges—those patterns are as unique as fingerprints—to create a custom, one-of-a-kind artwork. Choose from four styles: Vibrant (bright, bold colors), Surreal (dreamy, warped designs), Geometric (clean, modern shapes), or Line Art (sleek, sketch-like lines). It’s built with React for the frontend, FastAPI for the backend, OpenCV for image analysis, and Pillow for resizing outputs. Whether you’re here for the fun of seeing your dog’s nose as art or the nitty-gritty of how it works, SnoutSketch has you covered!

What It Does
For the non-technical crowd, SnoutSketch is a blast—it takes something simple like your dog’s nose and turns it into a masterpiece you can frame, share, or just smile at. Imagine snapping a pic of your pup’s snout and getting back a colorful explosion or an elegant line drawing that’s totally unique to them. You upload the photo, pick a style, and download the art in 1080p or 4K. It’s like unlocking your dog’s hidden artist vibes! Technically, it’s a cool mix of tools: the app grayscales your image, runs Canny edge detection to find the nose ridges, pulls out contour points, and maps them into art based on the style you choose. Each style tweaks the output differently—Vibrant uses random bright colors, Surreal plays with funky patterns, and so on.

How to Set It Up
Getting SnoutSketch running is straightforward. You’ll need Node.js (v16 or higher), Python (3.9 or higher), and Git installed. Clone the repo with "git clone https://github.com/yourusername/SnoutSketch.git" and move into the folder with "cd SnoutSketch". For the frontend, go "cd frontend" and run "npm install" to grab the React dependencies. For the backend, go "cd ../backend" and run "pip install fastapi uvicorn opencv-python pillow python-multipart" to set up FastAPI and the image processing libraries. That’s it—dependencies are ready!

How to Run It
Start the backend first: go "cd backend" and run "python main.py". It’ll fire up on http://localhost:8000. Then, in a new terminal, start the frontend with "cd frontend" and "npm start"—it’ll open at http://localhost:3000. Head to that URL in your browser, upload a close-up dog nose photo, pick one of the four styles, and hit "Generate Art". You’ll get download links for your pup’s artwork in two resolutions. Keep both terminals running to use the app!

Technical Details
The frontend is React, handling the UI where you upload photos and see results—it’s smooth and user-friendly. The backend uses FastAPI to manage requests, like receiving your image and sending back art URLs. OpenCV does the heavy lifting: it processes the image, detects edges (those nose ridges), and extracts points from contours. Pillow then takes the generated art and scales it to 1080p or 4K for downloads. Right now, art generation is basic—plotting ridge points as colored pixels or lines—but it’s solid for an MVP. The styles (Vibrant, Surreal, Geometric, Line Art) each apply different rules to those points, like color randomness or line toggling.

Future Plans
This is an MVP, so there’s room to grow! Plans include real-time previews (see the art before downloading), custom options (pick your own colors or tweak intensity), and a “share to X” feature to post your pup’s art online. The art could get fancier too—think connecting points with dynamic lines, adding shapes, or layering effects. It’s all about making SnoutSketch more fun and flexible.

License and Contact
SnoutSketch is under the MIT license—use it, tweak it, share it, just give a nod to the project. I built this with a love for dogs and a passion for coding. 
