import React, { useState, useEffect } from 'react';
import { useSpring, animated } from 'react-spring';
import { Line } from 'react-chartjs-2';
import 'chartjs-plugin-annotation';
import { Bar } from 'react-chartjs-2';
import Chart from 'chart.js/auto';
import "./arrived_chart.css";


Chart.defaults.font.size = 12;
Chart.defaults.color = '#090b1f';  

const ArrivedChart = () => {
    console.log('ArrivedChart rendered');


    const arrived_data = {
        labels: ['Вчера', 'Сегодня'],
        datasets: [
            {
                label: 'СМП',
                data: [65,20],//data ? [data.data, data.data, data.data] : [10,20,10],
                backgroundColor: ['#1b2c8d', '#1b2c8d', '#1b2c8d'],
                borderColor: '#090b1f',
                borderWidth: 1,
                // barThickness: 30
            },
            {
                label: 'План',
                data: [42,96],//data ? [data.data, data.data, data.data] : [10,20,10],
                backgroundColor: ['#6000a2', '#6000a2', '#6000a2'],
                borderColor: '#090b1f',
                borderWidth: 1,
                // barThickness: 30
            },
            {
                label: 'Самотек',
                data: [112,39],//data ? [data.data, data.data, data.data] : [10,20,10],
                backgroundColor: ['#00a279', '#00a279', '#00a279'],
                borderColor: '#090b1f',
                borderWidth: 1,
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
                    display: true, // Display default grid lines
                    color: (context) => {
                        if (context.tick.value === 40) {
                            return '#ff0000'; // Customize the color of the custom grid lines
                        } else {
                            return '#3e3e3e54'; // Default tick color
                        }
                    },
                },
                
                ticks: {
                    color: (context) => {
                        if (context.tick.value === 40) {
                            return '#ff0000'; // Customize the color of the custom grid lines
                        } else {
                            return '#090b1f'; // Default tick color
                        }
                    },
                },
            },
        },
        barThickness: 'flex',
        // maxBarThickness: 30,  
        barPercentage: 0.9, // Adjust the space between columns (0.8 means 80% of the available space)
        categoryPercentage: 0.7,
        plugins: {
            legend: {
                display: true,
            },
            title: {
                display: true,
                text: 'Количество обратившихся по каналам обращения',
                color: '#090b1f',
            },
        },
    };

    // Chart component
    return (
        <div className='arrived_chart'>
          <Bar data={arrived_data} options={chartOptions} />
        </div>

        // Code for animation chart itself
        // <animated.div className='arrived_chart' style={props}>
        //     <Bar data={arrived_data} options={chartOptions} />
        // </animated.div>
    );
};

export default ArrivedChart;
