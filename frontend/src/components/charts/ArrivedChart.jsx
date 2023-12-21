import React, { useState, useEffect } from 'react';
import { useSpring, animated } from 'react-spring';
import { Bar } from 'react-chartjs-2';
import Chart from 'chart.js/auto';
import "./arrived_chart.css";

// Chart.defaults.font.size = 12;
// Chart.defaults.color = "blue";  

const ArrivedChart = () => {
    console.log('ArrivedChart rendered');

    // const [data, setData] = useState(null);

    // Props for <animated.div> chart itself
    // const props = useSpring({
    //   from: { opacity: 0 },
    //   to: { opacity: 1 },
    //   config: { duration: 1200 },
    // });

    //Getting data by API
    // useEffect(() => {
    //     const fetchData = async () => {
    //         try {
    //             const response = await fetch('http://localhost:8000/api/v1/hospdata/dbkis/');
    //             const jsonData = await response.json();
    //             setData(jsonData);
    //         } catch (error) {
    //             console.error('Error fetching data:', error);
    //         }
    //     };

    //     fetchData(); // Fetch data when the component mounts
    // }, []);

    // if (data !== null) {
    //     console.log([data.data, data.data, data.data]);
    // };


    const arrived_data = {
        labels: ['СМП', 'План', 'Самотек'],
        datasets: [
            {
                label: 'обратившиеся',
                data: [45,160,100],//data ? [data.data, data.data, data.data] : [10,20,10],
                backgroundColor: ["#289c22", '#3461a8', '#c49735'],
                borderColor: "#f44345",
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
                max: 200, // Set the maximum value
                grid: {
                    display: false,
                },
                ticks: {
                    beginAtZero: true,
                    color: '#090b1f',
                    stepSize: 50, // Set the interval between ticks
                    font: {
                        // size: 14,
                        weight: 'bold' // Set the font weight to bold
                        
                    },
                }
            },
        },
        // barThickness: 'flex',
        // maxBarThickness: 30,  
        barPercentage: 0.8, // Adjust the space between columns (0.8 means 80% of the available space)
        categoryPercentage: 0.8,
        plugins: {
            legend: {
                display: false,
            },
            title: {
                display: true,
                text: 'Каналы обращения',
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
