import React from 'react';
import { useLocation } from 'react-router-dom';
// import axios from 'axios';


export function GetAnalysis() {
    const location = useLocation();
    const userData = location.state?.userData;

    return (
        <>
        <p>User Data:</p>
        <pre>{JSON.stringify(userData, null, 2)}</pre>
        </>
    );
}