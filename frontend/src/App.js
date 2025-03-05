// frontend/src/App.js
import React, { useState } from 'react';
import './App.css';

function App() {
  const [file, setFile] = useState(null);
  const [preview, setPreview] = useState(null);
  const [style, setStyle] = useState('vibrant');
  const [artUrls, setArtUrls] = useState({});

  const handleFileChange = (e) => {
    const selectedFile = e.target.files[0];
    setFile(selectedFile);
    setPreview(URL.createObjectURL(selectedFile));
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    if (!file) return;
  
    const formData = new FormData();
    formData.append('image', file);
    formData.append('style', style);
  
    try {
      const response = await fetch('http://localhost:8000/generate', {
        method: 'POST',
        body: formData,
      });
      if (!response.ok) throw new Error(`HTTP error! Status: ${response.status}`);
      const data = await response.json();
      setArtUrls(data.urls);
    } catch (error) {
      console.error('Fetch error:', error);
      alert('Failed to generate art: ' + error.message);
    }
  };

  return (
    <div className="app">
      <h1>Dog Nose Art Generator</h1>
      <form onSubmit={handleSubmit}>
        <input type="file" accept="image/*" onChange={handleFileChange} />
        {preview && <img src={preview} alt="Preview" className="preview" />}
        <select value={style} onChange={(e) => setStyle(e.target.value)}>
          <option value="vibrant">Vibrant</option>
          <option value="surreal">Surreal</option>
          <option value="geometric">Geometric</option>
          <option value="lineart">Line Art</option>
        </select>
        <button type="submit">Generate Art</button>
      </form>
      {Object.keys(artUrls).length > 0 && (
        <div className="downloads">
          <h2>Download Your Art</h2>
          <a href={artUrls.low} download="dog_nose_low_res.png">Low Res (1080p)</a>
          <a href={artUrls.high} download="dog_nose_high_res.png">High Res (4K)</a>
        </div>
      )}
    </div>
  );
}

export default App;