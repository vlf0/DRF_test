import React, { useState, useEffect, useRef } from 'react';
import { useSpring, animated } from 'react-spring';
import { Bar, Line } from 'react-chartjs-2';
import Chart from 'chart.js/auto';
import AnnotationPlugin from 'chartjs-plugin-annotation';
import ChartDataLabels from 'chartjs-plugin-datalabels';
import current_date from '../dates/DatesFormat';
import "./arrived_chart.css";

Chart.register(AnnotationPlugin);
Chart.register(ChartDataLabels);


Chart.defaults.font.size = 12;
Chart.defaults.color = '#090b1f';  


const ArrivedChart = () => {

    const plan = 60

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
              label: 'total',
              data: [80, 73, 84, 35, 69, 76, 92],//data ? [data.data, data.data, data.data] : [10,20,10],
              backgroundColor: ['#2d8587', '#2d8587', '#2d8587'],
              borderColor: '#090b1f',
              borderWidth: 1,
            },
        ],
    };

    const chartOptions = {
        barThickness: 'flex',
        barPercentage: 0.9, 
        categoryPercentage: 0.8,
        scales: {
            x: {
                // stacked: true,
                grid: { 
                  drawOnChartArea: false,
                  drawTicks: false
                },
                ticks: {
                    // display: false,
                    beginAtZero: true,
                    color: '#090b1f',   
                    font: {
                        // size: 14,
                        weight: 'bold' 
                },},
            },
            y: {
                // stacked: true,
                grid: {
                  drawOnChartArea: true,
                  drawTicks: false
                  },
             
                ticks: {
                    color: (context) => {
                        if (context.tick.value === plan) {
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

        plugins: { 
            datalabels: {
                display: true,
                labels: {
                    title: {
                        color: 'black',
                        font: {
                          size: 10,
                          weight: 'bold',
                          },
                        anchor: 'end',
                        align: 'end',
                        // formatter: title => {
                        //     const percernts = ((title / plan  * 100) - 100).toFixed(1);
                        //     return '\t' + percernts+'%';
                        // },
                    },
                    value: {
                        formatter: title => {
                            const percernts = ((title / plan  * 100) - 100).toFixed(1);
                            return '\t' + percernts+'%';
                        },
                        color: 'blue',
                        font: {
                          size: 10,
                          weight: 'bold',
                          },
                    },
                },

            },

            annotation: {
                    annotations: {
                      line1: {
                        type: 'line',
                        yMin: 60,
                        yMax: 60,
                        borderColor: '#ff6384',
                        borderWidth: 2,
                      },
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
          <Bar data={arrived_data} options={chartOptions} />
        </div>

        // Code for animation chart itself
        // <animated.div className='arrived_chart' style={props}>
        //     <Bar data={arrived_data} options={chartOptions} />
        // </animated.div>
    );
};

export default ArrivedChart;
