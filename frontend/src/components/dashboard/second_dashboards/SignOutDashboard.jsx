import React from 'react';
import { useSpring, animated } from 'react-spring';
import "../../parent.css" 


function SignOutDashboard() {

  const props = useSpring({
    from: { opacity: 0 },
    to: { opacity: 1 },
    config: { duration: 1200 },
  });

  return (
    <>  
      <p>test</p>
    </>
  );
}

export default SignOutDashboard;
