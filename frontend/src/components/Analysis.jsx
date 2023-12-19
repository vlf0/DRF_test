import React, { useState, useEffect } from 'react';
import { useLocation } from 'react-router-dom';
import { useSpring, animated } from 'react-spring';
import "./menu_styles.css"
import "./parent.css"


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
  }, []); // Empty dependency array ensures useEffect runs only once (on mount)

  // Rising top effect #1
  // const props = useSpring({
  //   from: { top: '0%' },
  //   to: { top: data ? '-10%' : '0%' },
  //   config: { duration: 1000 },
  // });

  // Rising top effect #2
  // const props = useSpring({
  //   from: { transform: 'translateY(100%)' },
  //   to: { transform: data ? 'translateY(0%)' : 'translateY(100%)' },
  //   config: { duration: 1000 },
  // });


  const props = useSpring({
    from: { opacity: 0 },
    to: { opacity: data ? 1 : 0 },
    config: { duration: 1000 },
  });

  return (
    <>
      {data ? (
      <animated.div className='day_arrived' style={props}>
        <p className='text_data'>Поступивших {data.data}</p>
        {/* Add more properties as needed */}
      </animated.div>
      ) : (
        <p>Loading...</p>
      )}
    </>
  );
}

export default GetAnalysis;
