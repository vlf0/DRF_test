import React from 'react';
import { useLocation } from 'react-router-dom';
import { useSpring, animated } from 'react-spring';
import ArrivedChart from './charts/ArrivedChart';
import TopBlock from './TopBlock';
import "./info_blocks.css"
import "./parent.css" 
import "./block_texts.css"

function GetAnalysis() {
console.log('GetAnalysis rendered');

  const location = useLocation();
  const userData = location.state?.userData;

  const props = useSpring({
    from: { opacity: 0 },
    to: { opacity: 1 },
    config: { duration: 1200 },
  });

  return (
    <>  
      <TopBlock />
      <animated.div className='dashboard' style={props}>
        <div className='chart_themes'>
          <p className='theme_lables'>Обратившиеся</p>
          <ArrivedChart />
        </div>
      </animated.div>
    </>
  );
}

export default GetAnalysis;
