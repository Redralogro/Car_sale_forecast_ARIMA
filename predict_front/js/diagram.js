//customer_lifetime_chart
var ctx = document.getElementById('myChart').getContext('2d');
var myChart = new Chart(ctx, {
    type: 'bar',
    data: {
        labels: ['All', 'Cluster1', 'Cluster2'],
        datasets: [{
            label: 'Customer Lifetime Value',
            data: [8004.94, 6136.06, 24291.275],
            backgroundColor: 'blue'
        }],
        borderWidth: 2
    },
    options: {
        scales: {
            yAxes: [{
                ticks: {
                    beginAtZero: true
                }
            }]
        }
    }
});
//Pie_chart
var chart = document.getElementById('cluster_pie').getContext('2d');
var pie_chart = new Chart(chart, {
    type: 'pie',
    data: {
        labels: ['Cluster1', 'Cluster2'],
        datasets: [{
                label: 'Diagram',
                backgroundColor: ['yellow', '#462d49'],
                data: [10.2, 89.8]
            }

        ]
    }
});
//total_claim_amount
var claim = document.getElementById('total_claim_amount').getContext('2d');
var claim_Chart = new Chart(claim, {
    type: 'bar',
    data: {
        labels: ['All', 'Cluster1', 'Cluster2'],
        datasets: [{
            label: 'total_claim_amount',
            data: [434.088, 420.16, 555.496],
            backgroundColor: 'green'
        }],
        borderWidth: 2
    },
    options: {
        scales: {
            yAxes: [{
                ticks: {
                    beginAtZero: true
                }
            }]
        }
    }
});
//Monthly_Premium_Auto_chart
var Premium_Auto = document.getElementById('Monthly_Premium_Auto').getContext('2d');
var Premium_Auto_Chart = new Chart(Premium_Auto, {
    type: 'bar',
    data: {
        labels: ['All', 'Cluster1', 'Cluster2'],
        datasets: [{
            label: 'Monthly_Premium_Auto',
            data: [93.219, 90.28, 118.8],
            backgroundColor: 'gray'
        }],
        borderWidth: 2
    },
    options: {
        scales: {
            yAxes: [{
                ticks: {
                    beginAtZero: true
                }
            }]
        }
    }
});