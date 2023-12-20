import React, { useState, useEffect } from 'react';
import { Bar } from 'react-chartjs-2';
import Chart from 'chart.js/auto';
import "./arrived_chart.css";

const ArrivedChart = () => {
    console.log('ArrivedChart rendered');

    const [data, setData] = useState(null);

    useEffect(() => {
        const fetchData = async () => {
            try {
                const response = await fetch('http://localhost:8000/api/v1/hospdata/dbkis/');
                const jsonData = await response.json();
                setData(jsonData);
            } catch (error) {
                console.error('Error fetching data:', error);
            }
        };

        fetchData(); // Fetch data when the component mounts
    }, []);

    if (data !== null) {
        console.log([data.data, data.data, data.data]);
    };


    const arrived_data = {
        labels: ['СМП', 'План', 'Самотек'],
        datasets: [
            {
                label: 'обратившиеся',
                data: [15,38,22],//data ? [data.data, data.data, data.data] : [10,20,10],
                backgroundColor: ["#289c22", '#3461a8', '#c49735'],
                borderColor: "#f44345",
                borderWidth: 1,
                barThickness: 30
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
                }
            },
            y: {
                grid: {
                    display: false,
                },
                ticks: {
                    beginAtZero: true,
                    color: '#090b1f',
                }
            },
        },
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
        <div>
            <Bar data={arrived_data} options={chartOptions} />
        </div>
    );
};

export default ArrivedChart;
