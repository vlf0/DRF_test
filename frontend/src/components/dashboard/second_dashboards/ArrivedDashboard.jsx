import React from 'react';
import { useSpring, animated } from 'react-spring';
import "../../parent.css" 


function ArrivedDashboard() {

  const props = useSpring({
    from: { opacity: 0 },
    to: { opacity: 1 },
    config: { duration: 1200 },
  });

  return (
    <>  
      <h1>test</h1>
    </>
  );
}

export default ArrivedDashboard;
