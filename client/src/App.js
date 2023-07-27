import React, { useState, useEffect } from 'react';
import axios from 'axios';

const App = () => {
  const [output, setOutput] = useState('');

  useEffect(() => {
    // Make the API request to your Flask backend
    axios.get('https://diab-tracker.onrender.com')
      .then(response => {
        setOutput(response.data);
      })
      .catch(error => {
        console.error('Error fetching data:', error);
      });
  }, []);

  return (
    <div>
      <h1>Output from Flask backend:</h1>
      <pre>{output}</pre>
    </div>
  );
};

export default App;
