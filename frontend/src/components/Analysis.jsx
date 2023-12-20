import React, { useState, useEffect } from 'react';
import { useLocation } from 'react-router-dom';
import InBlockInfo from './InBlockInfo'; // Adjust the path based on your project structure
import OutBlockInfo from './OutBlockInfo';
import TopBlock from './TopBlock';
import "./info_blocks.css"
import "./parent.css" 
import "./block_texts.css"

function GetAnalysis() {
  const location = useLocation();
  const userData = location.state?.userData;
  const [data, setData] = useState(null);

  useEffect(() => {
    const fetchData = async () => {
      try {
        const response = await fetch('http://localhost:8000/api/v1/hospdata/dbkis/');
        const jsonData = await response.json();
        setData(jsonData);
        console.log(jsonData)
      } catch (error) {
        console.error('Error fetching data:', error);
      }
    };

    fetchData();
  }, []);

  return (
    <>
      <TopBlock />
      {data ? (
        [<InBlockInfo data={data} />, <OutBlockInfo data={data} />]
      ) : (
        <p>Loading...</p>
      )}
      
    </>
  );
}

export default GetAnalysis;
