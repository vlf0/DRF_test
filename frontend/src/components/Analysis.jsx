import React from 'react';
import { useLocation } from 'react-router-dom';
import TopBlock from './TopBlock';
import ArrivedChart from './charts/ArrivedChart';
import "./info_blocks.css"
import "./parent.css" 
import "./block_texts.css"

function GetAnalysis() {
console.log('GetAnalysis rendered');

  const location = useLocation();
  const userData = location.state?.userData;

  return (
    <>
      <TopBlock />
      <ArrivedChart />
    </>
  );
}

export default GetAnalysis;
