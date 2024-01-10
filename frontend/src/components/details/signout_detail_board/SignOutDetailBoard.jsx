import React from "react";
import DeadsChartDetail from "./DeadsChartDetail";
import SignOutDetailTable from "./SignOutDetailTable";
import '../signIn_detail_board/detail_blocks.css'


const signOutCount = 63
const deadCount = 9
const moveCount = 18



const SignOutDetailBoard = ({ combinedData, profiles }) => {
    return (
        <div className='detail_block'>

          <span className='detail_block_header'> Исходы </span>
          <div className='blocks_container'>
            <div className='separated_detail_block'> Перевод в другую МО <br></br><br></br> {moveCount} </div>
            <div className='separated_detail_block'> Смерть <br></br><br></br> {deadCount} </div>
            <div className='separated_detail_block'> Выписка <br></br><br></br> {signOutCount} </div>
          </div>
          <span className='detail_block_header'> Выписка по отделениям </span>
          <DeadsChartDetail profiles={profiles}/>
          <span className='detail_block_header'> Детализация по умершим </span>
          <SignOutDetailTable />
            

        </div>

    );
}

export default SignOutDetailBoard;