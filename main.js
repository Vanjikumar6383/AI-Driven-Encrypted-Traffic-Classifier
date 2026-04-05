// Sample Data
const alertsData = [
    {
        id: 1,
        timestamp: "2024-04-04 20:45:12",
        sourceIp: "192.168.1.104",
        destIp: "104.22.4.15",
        threatType: "Botnet Communication",
        severity: "critical",
        flowDuration: "1042ms",
        packetCount: 142,
        protocol: "HTTPS/TLS v1.3",
        confidence: 0.98,
        summary: "Suspicious beaconing activity detected in encrypted flow. High frequency connection patterns observed."
    },
    {
        id: 2,
        timestamp: "2024-04-04 20:58:33",
        sourceIp: "172.16.0.42",
        destIp: "23.1.55.8",
        threatType: "Data Exfiltration (Anomalous Flow)",
        severity: "high",
        flowDuration: "42050ms",
        packetCount: 12044,
        protocol: "HTTPS/TLS v1.2",
        confidence: 0.92,
        summary: "Abnormal flow duration and volume detected. Outbound data transfer significantly larger than baseline for this source."
    },
    {
        id: 3,
        timestamp: "2024-04-04 21:05:00",
        sourceIp: "192.168.1.55",
        destIp: "142.250.190.46",
        threatType: "Suspicious Metadata (Old TLS)",
        severity: "medium",
        flowDuration: "250ms",
        packetCount: 12,
        protocol: "TLS v1.0",
        confidence: 0.78,
        summary: "Use of deprecated TLS version detected. Flow metadata indicates potential legacy vulnerability or malformed traffic."
    }
];

// Initialize Dashboard
document.addEventListener('DOMContentLoaded', () => {
    updateClock();
    setInterval(updateClock, 1000);
    initTrafficChart();
    renderAlerts();
    setupEventListeners();
});

// Clock Function
function updateClock() {
    const now = new Date();
    document.getElementById('clock').innerText = now.toLocaleTimeString();
}

// Chart Initialization
function initTrafficChart() {
    const ctx = document.getElementById('trafficChart').getContext('2d');
    
    // Gradient for chart
    const gradient = ctx.createLinearGradient(0, 0, 0, 400);
    gradient.addColorStop(0, 'rgba(59, 130, 246, 0.4)');
    gradient.addColorStop(1, 'rgba(59, 130, 246, 0.0)');

    const data = {
        labels: ['20:00', '20:10', '20:20', '20:30', '20:40', '20:50', '21:00', '21:10'],
        datasets: [{
            label: 'Traffic Volume (MB/s)',
            data: [65, 59, 80, 81, 56, 120, 95, 105],
            fill: true,
            borderColor: '#3b82f6',
            backgroundColor: gradient,
            borderWidth: 2,
            tension: 0.4,
            pointRadius: 4,
            pointBackgroundColor: '#3b82f6'
        }]
    };

    const config = {
        type: 'line',
        data: data,
        options: {
            responsive: true,
            maintainAspectRatio: false,
            plugins: {
                legend: { display: false }
            },
            scales: {
                y: {
                    beginAtZero: true,
                    grid: { color: 'rgba(255,255,255,0.05)' },
                    ticks: { color: '#94a3b8' }
                },
                x: {
                    grid: { display: false },
                    ticks: { color: '#94a3b8' }
                }
            }
        }
    };

    new Chart(ctx, config);
}

// Render Alerts Table
function renderAlerts() {
    const tableBody = document.getElementById('alerts-table-body');
    tableBody.innerHTML = '';

    alertsData.forEach(alert => {
        const row = document.createElement('tr');
        row.innerHTML = `
            <td>${alert.timestamp.split(' ')[1]}</td>
            <td style="font-family: 'JetBrains Mono'">${alert.sourceIp}</td>
            <td style="font-family: 'JetBrains Mono'">${alert.destIp}</td>
            <td>${alert.threatType}</td>
            <td><span class="severity ${alert.severity}">${alert.severity}</span></td>
        `;
        row.onclick = () => showInspection(alert);
        tableBody.appendChild(row);
    });
}

// Show Threat Inspection
function showInspection(alert) {
    const panel = document.getElementById('inspection-details');
    panel.innerHTML = `
        <div class="inspection-data-grid">
            <div class="inspection-item"><div class="label">Source IP</div><div class="value">${alert.sourceIp}</div></div>
            <div class="inspection-item"><div class="label">Destination IP</div><div class="value">${alert.destIp}</div></div>
            <div class="inspection-item"><div class="label">Protocol</div><div class="value">${alert.protocol}</div></div>
            <div class="inspection-item"><div class="label">Flow Duration</div><div class="value">${alert.flowDuration}</div></div>
            <div class="inspection-item"><div class="label">Packets</div><div class="value">${alert.packetCount}</div></div>
            <div class="inspection-item"><div class="label">Severity</div><div class="value" style="color: ${alert.severity === 'critical' ? 'var(--accent-red)' : 'var(--accent-yellow)'}">${alert.severity.toUpperCase()}</div></div>
        </div>
        <div class="confidence-sec">
            <div class="label">AI Confidence Score: ${(alert.confidence * 100).toFixed(1)}%</div>
            <div class="confidence-bar"><div class="confidence-fill" style="width: ${alert.confidence * 100}%;"></div></div>
        </div>
        <div style="margin-top: 1rem; border-top: 1px solid var(--border-color); padding-top: 1rem;">
            <div class="label">Behavior Summary</div>
            <p style="font-size: 0.8rem; color: var(--text-secondary); line-height: 1.4;">${alert.summary}</p>
        </div>
    `;
}

// Setup Interaction
function setupEventListeners() {
    const sideItems = document.querySelectorAll('.sidebar li');
    sideItems.forEach(item => {
        item.addEventListener('click', () => {
            sideItems.forEach(i => i.classList.remove('active'));
            item.classList.add('active');
        });
    });
}
