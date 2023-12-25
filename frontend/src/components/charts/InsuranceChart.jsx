import React, { useState, useEffect } from 'react';
import { useSpring, animated } from 'react-spring';
import { Bar } from 'react-chartjs-2';
import Chart from 'chart.js/auto';
import "./arrived_chart.css";


Chart.defaults.font.size = 12;
Chart.defaults.color = '#090b1f';  


const InsuranceChart = () => {

    const insurance_data = {
        labels: ['Вчера', 'Сегодня'],
        datasets: [
            {
                label: 'Москва',
                data: [32, 27],//data ? [data.data, data.data, data.data] : [10,20,10],
                backgroundColor: ['#00aeff', '#00aeff'],
                borderColor: '#090b1f',
                // borderWidth: 1,
                // barThickness: 30
            },
            {
                label: 'НИД',
                data: [54, 62],//data ? [data.data, data.data, data.data] : [10,20,10],
                backgroundColor: ['#c40176', '#c40176'],
                borderColor: '#090b1f',
                // borderWidth: 1,
                // barThickness: 30
            }
            ,{
                label: 'МО',
                data: [29, 34],//data ? [data.data, data.data, data.data] : [10,20,10],
                backgroundColor: ['#929200', '#929200'],
                borderColor: '#090b1f',
                // borderWidth: 1,
                // barThickness: 30
            },
            {
                label: 'Иногородний',
                data: [14, 16],//data ? [data.data, data.data, data.data] : [10,20,10],
                backgroundColor: ['#1a1b9c', '#1a1b9c'],
                borderColor: '#090b1f',
                // borderWidth: 1,
                // barThickness: 30
            },
            {
                label: 'ЗЛ',
                data: [17, 8],//data ? [data.data, data.data, data.data] : [10,20,10],
                backgroundColor: ['#00821b', '#00821b'],
                borderColor: '#090b1f',
                // borderWidth: 1,
                // barThickness: 30
            }
        ]
    };

    const chartOptions = {
        scales: {
            x: {
                grid: {
                    display: false
                },
                ticks: {
                    beginAtZero: true,
                    color: '#090b1f',   
                    font: {
                        // size: 14,
                        weight: 'bold' // Set the font weight to bold
                        
                    },
                },
            },
            y: {
                // min: -20, // Set the minimum value
                // max: 150, // Set the maximum value
                grid: {
                    // display: false,
                },
                ticks: {
                    beginAtZero: true,
                    color: '#090b1f',
                    stepSize: 20, // Set the interval between ticks
                    font: {
                        // size: 14,
                        weight: 'bold' // Set the font weight to bold
                        
                    },
                }
            },
        },
        barThickness: 'flex',
        // maxBarThickness: 30,  
        barPercentage: 0.9, // Adjust the space between columns (0.8 means 80% of the available space)
        categoryPercentage: 0.6,
        borderWidth: 1,
        plugins: {
            legend: {
                display: true,
            },
            title: {
                display: true,
                text: 'Отношение госпитализированных к отказным',
                color: '#090b1f',
            },
        },
    };

    // Chart component
    return (
        <div className='arrived_chart'>
          <Bar data={insurance_data} options={chartOptions} />
        </div>

        // Code for animation chart itself
        // <animated.div className='arrived_chart' style={props}>
        //     <Bar data={arrived_data} options={chartOptions} />
        // </animated.div>
    );

}

export default InsuranceChart;