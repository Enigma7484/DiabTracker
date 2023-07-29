import React, { useState, useEffect } from 'react';
import axios from 'axios';

const App = () => {
  const [output, setOutput] = useState('');
  const BACKEND_URL = process.env.REACT_APP_BACKEND_URL;

  useEffect(() => {
    // Make the API request to your Flask backend
    axios.get(BACKEND_URL)
      .then(response => {
        setOutput(response.data);
      })
      .catch(error => {
        console.error('Error fetching data:', error);
      });
  }, []);

  return (
    <div>
      <h1>Below is the data that is read from the .csv file I have in my repo and the prediction based on the data whether the person has Diabetes or not is at the very bottom. I had worked on the backend of this project and could only get the result in the terminal. I recently worked on the project so that the output can be presented on the browser.</h1>
      
      <pre>{output}</pre>
    </div>
  );
};

export default App;
