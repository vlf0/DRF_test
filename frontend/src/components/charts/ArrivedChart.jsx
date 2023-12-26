import React, { useState, useEffect, useRef } from 'react';
import { useSpring, animated } from 'react-spring';
import { Line } from 'react-chartjs-2';
// import 'chartjs-plugin-annotation';
import { Bar } from 'react-chartjs-2';
import Chart from 'chart.js/auto';
import AnnotationPlugin from 'chartjs-plugin-annotation';
import current_date from '../dates/DatesFormat';
import "./arrived_chart.css";

Chart.register(AnnotationPlugin);


Chart.defaults.font.size = 12;
Chart.defaults.color = '#090b1f';  


const ArrivedChart = () => {

    // const chartRef = useRef();

    // useEffect(() => {
    //   if (chartRef.current) {
    //     const chartInstance = chartRef.current.chartInstance;
  
    //     if (chartInstance) {
    //       chartInstance.annotation.elements.push({
    //         type: 'line',
    //         mode: 'horizontal',
    //         scaleID: 'y-axis-0',
    //         value: 60,
    //         borderColor: 'rgb(255, 99, 132)',
    //         borderWidth: 2,
    //         label: {
    //           content: 'Annotation at 60',
    //           enabled: true,
    //           position: 'end',
    //         },
    //       });
  

    //     chartInstance.update(); // Update the chart to apply the changes
    //   }
    // }
    // }, []);


    const arrived_data = {
        labels: [
            current_date-6, current_date-5, current_date-4,
            current_date-3, current_date-2, current_date-1, current_date
        ],
        datasets: [
            {
                label: 'label',
                data: [80, 73, 84, 66, 69, 76, 92],//data ? [data.data, data.data, data.data] : [10,20,10],
                backgroundColor: ['#2d8587', '#2d8587', '#2d8587'],
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

                // grid: {
                //     display: true, // Display default grid lines
                //     color: (context) => {
                //         if (context.tick.value === 80) {
                //             return '#a90000'; // Customize the color of the custom grid lines
                //         } else {
                //             return '#3e3e3e54'; // Default tick color
                //         }
                //     },
                // },
                
                ticks: {
                    color: (context) => {
                        if (context.tick.value === 60) {
                            return '#860000'; // Customize the color of the custom grid lines
                        } else {
                            return '#090b1f'; // Default tick color
                        }
                    },
                    callback: (value, index, values) => {
                        // Customize the tick value
                        if (value === 60) {
                            return 'план 60'; // Change the tick label for the value 60
                        } else {
                            return value; // Use the default tick label for other values
                        }
                    },
                    font: {weight: 'bold'},
                },
            },
        },
        barThickness: 'flex',
        // maxBarThickness: 30,  
        barPercentage: 0.9, // Adjust the space between columns (0.8 means 80% of the available space)
        categoryPercentage: 0.7,
        plugins: {
            annotation: {
                    annotations: {
                      line1: {
                        type: 'line',
                        yMin: 60,
                        yMax: 60,
                        borderColor: '#ff6384',
                        borderWidth: 2,
                      },
                    //   label1: {
                    //     type: 'label',
                    //     color: 'black',
                    //     padding: 1,
                    //     xValue: 6.23,
                    //     yValue: 60,
                    //     backgroundColor: '#ff6384',
                    //     content: 'план',
                    //     font: {
                    //       size: 12,
                    //     }
                    //   }
                    },
              },
            legend: {
                display: false,
            },
            title: {
                display: true,
                text: 'Динамика обращений за неделю',
                color: '#090b1f',
            },
        },
    };

    // Chart component
    return (
        <div className='arrived_chart'>
          <Bar  data={arrived_data} options={chartOptions} />
          {/* <div style={{ position: 'absolute', top: 137, left: 218, color: '#a90000', fontWeight: 'bold', fontSize: 13 }}>
            план
          </div> */}
        </div>

        // Code for animation chart itself
        // <animated.div className='arrived_chart' style={props}>
        //     <Bar data={arrived_data} options={chartOptions} />
        // </animated.div>
    );
};

export default ArrivedChart;
