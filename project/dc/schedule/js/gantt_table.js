// Interactive Chronological Gantt Timeline & P6 Task Schedule Table for DC36-T3
// Institutional Primavera P6 CPM Visualizer

(function() {
    window.DC36_GANTT = {};

    let schedule = null;
    let currentTimestamp = 0;
    let onJumpCallback = null;

    let activeFilter = {
        search: '',
        wbs: 'all',
        criticalOnly: false,
        inProgressOnly: false
    };

    const WBS_COLORS = {
        '110': '#64748b', // PM
        '120': '#818cf8', // ENG
        '130': '#fbbf24', // PROC
        '140': '#a16207', // CIVIL
        '141': '#ca8a04', // SUB
        '142': '#b45309', // SUPER
        '143': '#78350f', // ENVEL
        '150': '#0284c7', // MEP
        '151': '#0284c7', // ELEC
        '152': '#d97706', // GEN
        '153': '#0ea5e9', // MECH
        '154': '#06b6d4', // WS
        '155': '#14b8a6', // ICT
        '160': '#f97316', // CX
        '161': '#f97316',
        '162': '#ea580c',
        '163': '#c2410c',
        '164': '#9a3412',
        '170': '#10b981'  // COD
    };

    window.DC36_GANTT.init = function(schedData, jumpFn) {
        schedule = schedData;
        onJumpCallback = jumpFn;
        currentTimestamp = schedule.min_timestamp;

        renderGanttChart();
        renderTaskTable();
        setupFilters();
    };

    // Update playhead and table rows on timeline tick
    window.DC36_GANTT.updateTime = function(ts) {
        currentTimestamp = ts;
        updatePlayhead(ts);
        updateTableRowStatuses(ts);
    };

    // 1. Gantt Chart Rendering
    function renderGanttChart() {
        const container = document.getElementById('gantt-chart-container');
        if (!container) return;

        const totalSpan = schedule.max_timestamp - schedule.min_timestamp;
        const totalDays = schedule.total_calendar_days;

        // Generate Time Header (Quarters & Months)
        let headerHtml = `<div class="gantt-time-header">`;
        const startYear = 2027;
        const endYear = 2029;
        const quarters = [
            '2027 Q1', '2027 Q2', '2027 Q3', '2027 Q4',
            '2028 Q1', '2028 Q2', '2028 Q3', '2028 Q4',
            '2029 Q1', '2029 Q2', '2029 Q3', '2029 Q4'
        ];
        quarters.forEach(q => {
            headerHtml += `<div class="gantt-q-block">${q}</div>`;
        });
        headerHtml += `</div>`;

        // Generate Rows for each activity
        let rowsHtml = `<div class="gantt-rows-wrapper" id="gantt-rows-wrapper">`;
        
        // Red synchronized playhead line
        rowsHtml += `<div class="gantt-playhead" id="gantt-playhead"></div>`;

        schedule.activities.forEach(act => {
            const startOffset = Math.max(0, (act.startTimestamp - schedule.min_timestamp) / totalSpan);
            const durationFrac = Math.max(0.004, (act.finishTimestamp - act.startTimestamp) / totalSpan);

            const leftPct = (startOffset * 100).toFixed(2);
            const widthPct = (durationFrac * 100).toFixed(2);
            const color = WBS_COLORS[act.wbs_id] || '#38bdf8';
            const isMile = (act.type === 'TT_Mile' || act.type === 'TT_FinMile');

            rowsHtml += `
                <div class="gantt-row ${act.is_critical ? 'critical-row' : ''}" data-code="${act.code}">
                    <div class="gantt-label">
                        <span class="gantt-code">${act.code}</span>
                        <span class="gantt-name" title="${act.name}">${act.name}</span>
                    </div>
                    <div class="gantt-track">
                        ${isMile ? `
                            <div class="gantt-diamond" style="left: ${leftPct}%; border-color: ${color};" title="${act.code}: ${act.name}"></div>
                        ` : `
                            <div class="gantt-bar ${act.is_critical ? 'crit-bar' : ''}" 
                                 style="left: ${leftPct}%; width: ${widthPct}%; background-color: ${color};"
                                 title="${act.code}: ${act.name} (${act.duration}d) [${act.start} to ${act.finish}]">
                            </div>
                        `}
                    </div>
                </div>
            `;
        });

        rowsHtml += `</div>`;
        container.innerHTML = headerHtml + rowsHtml;

        // Wire bar click to jump 3D simulation
        container.querySelectorAll('.gantt-row').forEach(row => {
            row.addEventListener('click', () => {
                const code = row.getAttribute('data-code');
                const act = schedule.activities.find(a => a.code === code);
                if (act && onJumpCallback) {
                    onJumpCallback(act.startTimestamp, code);
                    highlightRow(code);
                }
            });
        });
    }

    // Update synchronized red vertical hairline cursor
    function updatePlayhead(ts) {
        const playhead = document.getElementById('gantt-playhead');
        if (!playhead || !schedule) return;

        const totalSpan = schedule.max_timestamp - schedule.min_timestamp;
        const progress = Math.max(0, Math.min(1, (ts - schedule.min_timestamp) / totalSpan));
        // Offset for sticky left label column (260px) + track percentage
        playhead.style.left = `calc(260px + (100% - 260px) * ${progress})`;
    }

    // 2. P6 Task Table Rendering
    function renderTaskTable() {
        const tbody = document.getElementById('task-table-body');
        if (!tbody) return;

        const filtered = schedule.activities.filter(act => {
            if (activeFilter.search) {
                const s = activeFilter.search.toLowerCase();
                if (!act.code.toLowerCase().includes(s) && 
                    !act.name.toLowerCase().includes(s) && 
                    !act.wbs_code.toLowerCase().includes(s)) {
                    return false;
                }
            }
            if (activeFilter.wbs !== 'all') {
                if (!act.wbs_code.startsWith(activeFilter.wbs) && act.wbs_id !== activeFilter.wbs) {
                    return false;
                }
            }
            if (activeFilter.criticalOnly && !act.is_critical) return false;
            return true;
        });

        tbody.innerHTML = filtered.map(act => {
            const status = getTaskStatus(act, currentTimestamp);
            return `
                <tr class="table-row ${act.is_critical ? 'crit-row' : ''}" id="row-${act.code}" data-code="${act.code}">
                    <td class="cell-code">${act.code}</td>
                    <td class="cell-wbs">${act.wbs_code}</td>
                    <td class="cell-name">${act.name}</td>
                    <td class="cell-dur">${act.duration}d</td>
                    <td class="cell-date">${act.start}</td>
                    <td class="cell-date">${act.finish}</td>
                    <td class="cell-float ${act.total_float === 0 ? 'crit-val' : ''}">${act.total_float}d</td>
                    <td class="cell-status"><span class="status-pill status-${status.class}">${status.label}</span></td>
                    <td class="cell-action">
                        <button class="tbl-jump-btn" data-code="${act.code}"><i class="fas fa-crosshairs"></i> Jump</button>
                    </td>
                </tr>
            `;
        }).join('');

        // Wire jump buttons in table
        tbody.querySelectorAll('.tbl-jump-btn').forEach(btn => {
            btn.addEventListener('click', (e) => {
                e.stopPropagation();
                const code = btn.getAttribute('data-code');
                const act = schedule.activities.find(a => a.code === code);
                if (act && onJumpCallback) {
                    onJumpCallback(act.startTimestamp, code);
                    highlightRow(code);
                }
            });
        });
    }

    function getTaskStatus(act, ts) {
        if (ts >= act.finishTimestamp) {
            return { label: 'COMPLETED', class: 'completed' };
        } else if (ts >= act.startTimestamp && ts < act.finishTimestamp) {
            const span = act.finishTimestamp - act.startTimestamp;
            const pct = Math.floor(((ts - act.startTimestamp) / span) * 100);
            return { label: `ACTIVE ${pct}%`, class: 'active' };
        } else {
            return { label: 'NOT STARTED', class: 'pending' };
        }
    }

    function updateTableRowStatuses(ts) {
        const tbody = document.getElementById('task-table-body');
        if (!tbody) return;

        schedule.activities.forEach(act => {
            const row = document.getElementById(`row-${act.code}`);
            if (row) {
                const statusCell = row.querySelector('.cell-status');
                if (statusCell) {
                    const status = getTaskStatus(act, ts);
                    statusCell.innerHTML = `<span class="status-pill status-${status.class}">${status.label}</span>`;
                }
            }
        });
    }

    function highlightRow(code) {
        document.querySelectorAll('.table-row.selected').forEach(r => r.classList.remove('selected'));
        const row = document.getElementById(`row-${code}`);
        if (row) {
            row.classList.add('selected');
            row.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
        }
    }

    function setupFilters() {
        const searchInput = document.getElementById('table-search-input');
        const wbsSelect = document.getElementById('table-wbs-filter');
        const critBtn = document.getElementById('filter-crit-btn');

        if (searchInput) {
            searchInput.addEventListener('input', (e) => {
                activeFilter.search = e.target.value;
                renderTaskTable();
            });
        }

        if (wbsSelect) {
            wbsSelect.addEventListener('change', (e) => {
                activeFilter.wbs = e.target.value;
                renderTaskTable();
            });
        }

        if (critBtn) {
            critBtn.addEventListener('click', () => {
                activeFilter.criticalOnly = !activeFilter.criticalOnly;
                critBtn.classList.toggle('active', activeFilter.criticalOnly);
                renderTaskTable();
            });
        }
    }
})();
