import React, { useState } from "react";
import { useSpring, animated } from "react-spring";
import OARDetailTable from "./OARDetailTable";


const OARDetailBoard = ({dept, values}) => {

    const [isOARTableVisible, setIsOARTableVisible] = useState(false);
    const toggleDeadTableVisibility = () => {
        setIsOARTableVisible(!isOARTableVisible);
    };

    // Spring effect ofappearance
    const springProps = useSpring({
      transform: `scale(${isOARTableVisible ? 1 : 0})`,
      height: isOARTableVisible ? "auto" : 0,
      opacity: isOARTableVisible ? 1 : 0,
      config: { tension: 200, friction: 25 },
      delay: isOARTableVisible ? 30 : 0,
      width: '-webkit-fill-available',
    });

    return (
        <>
        <span className='detail_block_header'> {dept} </span> 
        <div className='blocks_container'>
          <div 
            className='separated_detail_block_X'
            onClick={toggleDeadTableVisibility}
            > Поступило новых пациентов <br /><br /> {values[0]} </div>
          <div 
            className='separated_detail_block_X'
            onClick={toggleDeadTableVisibility}
            > Переводы из отделений <br /><br /> {values[1]} </div>
          <div             
            className='separated_detail_block_X'
            onClick={toggleDeadTableVisibility}> Находятся на лечении <br /><br /> {values[2]} </div>
        </div>
        <animated.div style={springProps}>
          {isOARTableVisible && <OARDetailTable />}
        </animated.div>

        </>

    );
}

export default OARDetailBoard;