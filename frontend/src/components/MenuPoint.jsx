import React, { useState } from 'react';
import { useSpring, animated } from 'react-spring';


function MenuPoint() {
    
  return (
    <ul className='point_menu'>
      <li className='point_m'>SAO</li>
      <li className='point_m'>ZAO</li>
      <li className='point_m'>SVAO</li>
    </ul>
  );
}

export default MenuPoint;