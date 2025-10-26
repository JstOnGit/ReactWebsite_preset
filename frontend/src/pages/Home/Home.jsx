import { useState, useEffect } from 'react';
import './Home.css';

function Home() {
  const [text, setText] = useState('Loading...');

  useEffect(() => {
    fetch('/api/test')
      .then(response => response.json())
      .then(data => {
        const record = data.find(item => item.id === 0);
        setText(record ? record.text : 'No record with id 0 found');
      })
      .catch(error => {
        setText(`Error: ${error.message}`);
      });
  }, []);

  return (
    <div>
      <h1>Test Data</h1>
      <p>{text}</p>
    </div>
  );
}

export default Home;